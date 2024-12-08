<template>
    <div class="app">

        <main class="main-content">
            <section class="profile-section">
                <div class="profile-header">
                    <img src="http://localhost:5173/src/static/my.jpg?height=100&width=100&text=Avatar" alt="User Avatar" class="avatar" />
                    <h2>John Doe</h2>
                </div>
                <div class="profile-info">
                    <p><strong>First name:</strong> Bekzod</p>
                    <p><strong>username:</strong> john.doe@example.com</p>
                </div>
            </section>

        </main>

    </div>
</template>

<script setup>
import { ref } from 'vue'
// import { HomeIcon, SearchIcon, UserIcon, TrashIcon } from 'lucide-vue-next'

const favoriteGenre = ref('action')
const emailNotifications = ref(true)
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

.header {
    background-color: #2c2c2c;
    padding: 1rem 0;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
}

.logo {
    font-size: 1.5rem;
    font-weight: bold;
}

.main-content {
    padding: 2rem 1rem 5rem;
    flex-grow: 1;
    overflow-y: auto;
}

.profile-section,
.preferences-section,
.watchlist-section {
    background-color: #2c2c2c;
    border-radius: 8px;
    padding: 1.5rem;
    margin-bottom: 2rem;
}

.profile-header {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;
}

.avatar {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    margin-right: 1rem;
}

.profile-info p {
    margin: 0.5rem 0;
}

h2,
h3 {
    margin-bottom: 1rem;
}

.preference-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
}

select,
input[type="checkbox"] {
    background-color: #4a4a4a;
    color: white;
    border: none;
    padding: 0.5rem;
    border-radius: 4px;
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
    height: auto;
}

.movie-info {
    padding: 0.5rem;
}

.movie-info h4 {
    margin: 0 0 0.5rem 0;
    font-size: 0.9rem;
}

.remove-button {
    display: flex;
    align-items: center;
    background-color: #e50914;
    color: white;
    border: none;
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.8rem;
}

.remove-button svg {
    margin-right: 0.25rem;
}

.nav-panel {
    display: flex;
    justify-content: space-around;
    background-color: #2c2c2c;
    padding: 0.5rem;
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 1000;
}

.nav-button {
    display: flex;
    flex-direction: column;
    align-items: center;
    background: none;
    border: none;
    color: white;
    cursor: pointer;
    padding: 0.5rem;
    transition: color 0.3s ease;
}

.nav-button:hover,
.nav-button.active {
    color: #e50914;
}

.nav-button span {
    font-size: 0.8rem;
    margin-top: 0.25rem;
}

@media (min-width: 768px) {
    .movie-grid {
        grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    }

    .nav-panel {
        padding: 1rem;
    }

    .nav-button {
        flex-direction: row;
    }

    .nav-button span {
        margin-top: 0;
        margin-left: 0.5rem;
    }
}

@media (max-width: 600px) {
    .profile-header {
        flex-direction: column;
        text-align: center;
    }

    .avatar {
        margin-right: 0;
        margin-bottom: 1rem;
    }

    .preference-item {
        flex-direction: column;
        align-items: flex-start;
    }

    .preference-item label {
        margin-bottom: 0.5rem;
    }
}
</style>