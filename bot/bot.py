import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

# Set up logging
logging.basicConfig(level=logging.INFO)

# Database setup
Base = declarative_base()
engine = create_engine('sqlite:///bot.db')
Session = sessionmaker(bind=engine)
session = Session()

# Define User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    inviter_id = Column(Integer, ForeignKey('users.id'))
    points = Column(Integer, default=0)

    invited_users = relationship('User', backref='inviter', remote_side=[id])

Base.metadata.create_all(engine)

# Bot setup
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Handle /start command
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    user = session.query(User).filter_by(telegram_id=message.from_user.id).first()
    inviter_id = None

    if not user:
        args = message.get_args()
        if args.isdigit():
            inviter_id = int(args)

        user = User(telegram_id=message.from_user.id, inviter_id=inviter_id)
        session.add(user)
        session.commit()

        # Award points to inviter
        if inviter_id:
            inviter = session.query(User).filter_by(telegram_id=inviter_id).first()
            if inviter:
                inviter.points += 5
                session.commit()

        await bot.send_message(ADMIN_ID, f"New user started the bot: {message.from_user.full_name} (@{message.from_user.username})")

    await message.answer("Welcome to the bot! Use /invite to invite others and earn points.")

# Handle /invite command
@dp.message(Command("invite"))
async def invite_handler(message: types.Message):
    invite_link = f"https://t.me/{(await bot.get_me()).username}?start={message.from_user.id}"
    user = session.query(User).filter_by(telegram_id=message.from_user.id).first()
    invited_count = len(user.invited_users)

    await message.answer(f"Your invite link: {invite_link}\nYou've invited {invited_count} users and earned {user.points} points.")

# Handle admin broadcast
@dp.message(Command("broadcast"))
async def broadcast_handler(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return await message.answer("You are not authorized to use this command.")

    if message.reply_to_message:
        users = session.query(User).all()
        for user in users:
            try:
                if message.reply_to_message.photo:
                    photo = message.reply_to_message.photo[-1].file_id
                    await bot.send_photo(user.telegram_id, photo, caption=message.reply_to_message.caption)
                elif message.reply_to_message.video:
                    video = message.reply_to_message.video.file_id
                    await bot.send_video(user.telegram_id, video, caption=message.reply_to_message.caption)
                else:
                    await bot.send_message(user.telegram_id, message.reply_to_message.text)
            except Exception as e:
                logging.error(f"Failed to send message to {user.telegram_id}: {e}")

        await message.answer("Broadcast sent to all users.")
    else:
        await message.answer("Please reply to the message you want to broadcast.")

# Run the bot
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
