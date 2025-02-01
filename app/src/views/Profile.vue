<template>
    <div class="app">
        <main class="main-content">
            <section class="profile-section">
                <div class="profile-header">
                    <div class="profile-avatar">
                        <img src="{{ user.profile_pic }}&width=150&text=Avatar" alt="User Avatar" class="avatar" />

                    </div>
                    <div class="profile-details">
                        <h2>{{ user.first_name }}</h2>
                        <p class="user-handle">@{{ user.username }}</p>
                        <p class="user-bio">{{ user.bio }}</p>
                    </div>
                </div>
            </section>
            <section>
                <Star/>
            </section>
            <section class="stats-section">
                <div class="stat-item">
                    <h3>Movies Watched</h3>
                    <p>0</p>
                </div>
                <div class="stat-item">
                    <h3>Reviews</h3>
                    <p>0</p>
                </div>
                <div class="stat-item">
                    <h3>Watchlist</h3>
                    <p>0</p>
                </div>
            </section>

            <section class="watchlist-section">
                <div class="section-header">
                    <h3>My Watchlist</h3>
                    <button class="view-all-btn">View All</button>
                </div>
                <div class="movie-grid">
                    <div v-for="movie in watchlist" :key="movie.id" class="movie-card">
                        <img :src="movie.poster" :alt="movie.title" />
                        <div class="movie-info">
                            <h4>{{ movie.title }}</h4>
                            <p class="movie-year">{{ movie.year }}</p>
                            <button class="remove-button" @click="removeFromWatchlist(movie.id)">
                                <TrashIcon size="16" />
                                Remove
                            </button>
                        </div>
                    </div>
                </div>
            </section>

        </main>
    </div>
</template>

<script>
import { ref } from 'vue'
import {  TrashIcon, StarIcon, EyeIcon } from 'lucide-vue-next'

const preferredLanguage = ref('en')
const darkMode = ref(false)

const watchlist = ref([
    { id: 1, title: 'Inception', year: 2010, poster: '/placeholder.svg?height=300&width=200&text=Inception' },
    { id: 2, title: 'The Shawshank Redemption', year: 1994, poster: '/placeholder.svg?height=300&width=200&text=Shawshank' },
    { id: 3, title: 'Pulp Fiction', year: 1994, poster: '/placeholder.svg?height=300&width=200&text=Pulp Fiction' },
    { id: 4, title: 'The Dark Knight', year: 2008, poster: '/placeholder.svg?height=300&width=200&text=Dark Knight' },
])


const removeFromWatchlist = (id) => {
    watchlist.value = watchlist.value.filter(movie => movie.id !== id)
}


export default {
    props: {
        user: {
            type: Array,
            required: true
        }
    },
    components: {
        TrashIcon,
        StarIcon,
        EyeIcon
    }

}
</script>

<style scoped>
.app {
    font-family: Arial, sans-serif;
    background-color: #1a1a1a;
    color: white;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    position: relative;
}


.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
}

.main-content {
    padding: 2rem 1rem 5rem;
    flex-grow: 1;
    overflow-y: auto;
    max-width: 800px;
    margin: 0 auto;
    width: 345px;
}

.profile-section,
.stats-section,
.preferences-section,
.watchlist-section,
.recent-activity {
    background-color: #2c2c2c;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 2rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.profile-header {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;
}

.profile-avatar {
    position: relative;
    margin-right: 2rem;
}

.avatar {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    object-fit: cover;
}

.edit-avatar-btn {
    position: absolute;
    bottom: 0;
    right: 0;
    background-color: #e50914;
    border: none;
    border-radius: 50%;
    padding: 0.5rem;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.edit-avatar-btn:hover {
    background-color: #ff0f22;
}

.profile-details {
    flex-grow: 1;
}

.profile-details h2 {
    margin: 0;
    font-size: 1.8rem;
}

.user-handle {
    color: #b3b3b3;
    margin: 0.25rem 0;
}

.user-bio {
    margin: 0.5rem 0;
}

.edit-profile-btn {
    display: inline-flex;
    align-items: center;
    background-color: transparent;
    border: 1px solid #e50914;
    color: #e50914;
    padding: 0.5rem 1rem;
    border-radius: 20px;
    cursor: pointer;
    transition: all 0.3s ease;
    margin-top: 0.5rem;
}

.edit-profile-btn:hover {
    background-color: #e50914;
    color: white;
}

.edit-profile-btn svg {
    margin-right: 0.5rem;
}

.stats-section {
    display: flex;
    justify-content: space-around;
    text-align: center;
}

.stat-item h3 {
    font-size: 0.9rem;
    color: #b3b3b3;
    margin-bottom: 0.25rem;
}

.stat-item p {
    font-size: 1.5rem;
    font-weight: bold;
}

.preferences-section h3,
.watchlist-section h3,
.recent-activity h3 {
    margin-bottom: 1rem;
    font-size: 1.2rem;
}

.preference-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 1rem;
}

.preference-item {
    display: flex;
    flex-direction: column;
}

.preference-item label {
    margin-bottom: 0.5rem;
    color: #b3b3b3;
}

select {
    background-color: #4a4a4a;
    color: white;
    border: none;
    padding: 0.5rem;
    border-radius: 4px;
    font-size: 1rem;
}

.switch {
    position: relative;
    display: inline-block;
    width: 60px;
    height: 34px;
}

.switch input {
    opacity: 0;
    width: 0;
    height: 0;
}

.slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #4a4a4a;
    transition: .4s;
    border-radius: 34px;
}

.slider:before {
    position: absolute;
    content: "";
    height: 26px;
    width: 26px;
    left: 4px;
    bottom: 4px;
    background-color: white;
    transition: .4s;
    border-radius: 50%;
}

input:checked+.slider {
    background-color: #e50914;
}

input:checked+.slider:before {
    transform: translateX(26px);
}

.section-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
}

.view-all-btn {
    background: none;
    border: none;
    color: #e50914;
    cursor: pointer;
    font-size: 0.9rem;
}

.movie-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
    gap: 1rem;
}

.movie-card {
    background-color: #3a3a3a;
    border-radius: 8px;
    overflow: hidden;
    transition: transform 0.3s ease;
}

.movie-card:hover {
    transform: scale(1.05);
}

.movie-card img {
    width: 100%;
    height: 200px;
    object-fit: cover;
}

.movie-info {
    padding: 0.5rem;
}

.movie-info h4 {
    margin: 0 0 0.25rem 0;
    font-size: 0.9rem;
}

.movie-year {
    font-size: 0.8rem;
    color: #b3b3b3;
    margin-bottom: 0.5rem;
}

.remove-button {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    background-color: #e50914;
    color: white;
    border: none;
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.8rem;
    transition: background-color 0.3s ease;
}

.remove-button:hover {
    background-color: #ff0f22;
}

.remove-button svg {
    margin-right: 0.25rem;
}

.activity-list {
    list-style-type: none;
    padding: 0;
}

.activity-item {
    display: flex;
    align-items: center;
    padding: 0.75rem 0;
    border-bottom: 1px solid #3a3a3a;
}

.activity-item:last-child {
    border-bottom: none;
}

.activity-icon {
    margin-right: 1rem;
    color: #e50914;
}

.activity-content {
    flex-grow: 1;
}

.activity-content p {
    margin: 0;
}

.activity-date {
    font-size: 0.8rem;
    color: #b3b3b3;
}

@media (min-width: 768px) {
    .profile-header {
        align-items: flex-start;
    }

    .movie-grid {
        grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    }
    .main-content{
        width: 600px;
    }
}

@media (max-width: 600px) {
    .profile-header {
        flex-direction: column;
        text-align: center;
    }

    .profile-avatar {
        margin-right: 0;
        margin-bottom: 1rem;
    }

    .stats-section {
        flex-direction: column;
    }

    .stat-item {
        margin-bottom: 1rem;
    }

    .preference-grid {
        grid-template-columns: 1fr;
    }
}
</style>