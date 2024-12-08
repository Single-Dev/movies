<template>

    <nav class="nav-panel">
        <RouterLink to="/" class="nav-button">
            <HomeIcon />
            <span>Home</span>
        </RouterLink>
        <RouterLink to="/search" class="nav-button">
            <SearchIcon />
            <span>Search</span>
        </RouterLink>
        <RouterLink to="/profile" class="nav-button">
            <UserIcon />
            <span>Profile</span>
        </RouterLink>
    </nav>
</template>
<script setup>
import { HomeIcon, SearchIcon, UserIcon } from 'lucide-vue-next'
import { RouterLink } from 'vue-router';
</script>
<style scoped>
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

.nav-button:hover {
    color: #e50914;
}

.nav-button span {
    font-size: 0.8rem;
    margin-top: 0.25rem;
}

@media (min-width: 768px) {

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
</style>