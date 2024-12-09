<template>
    <div id="app">
        <button @click="buyStars">Buy Stars</button>
    </div>
</template>

<script>
export default {
    mounted() {
        const tg = window.Telegram.WebApp;
        tg.ready();
        tg.expand();
    },
    methods: {
        async buyStars() {
            try {
                const response = await fetch('/create-payment', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        chatId: this.user.id,
                        amount: 1000, // In cents
                        description: 'Purchase Stars',
                    }),
                });
                const result = await response.json();
                console.log('Payment created:', result);
            } catch (error) {
                console.error('Payment error:', error);
            }
        },
    },
};
</script>