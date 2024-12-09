<template>
  <div class="app">

    <!-- Main Content -->
    <main class="main-content">
      <!-- Featured Movie -->
      <section class="featured-movie">
        <h2>Featured Movie</h2>
        <div class="featured-movie-card">
          <img src="../static/home.jpg?height=100&width=200" alt="Featured Movie" />
          <div class="featured-movie-info">
            <h3>Puss In Buts</h3>
            <p>Action, Adventure | 2h 15min</p>
            <button class="watch-button">Watch Now</button>
          </div>
        </div>
      </section>

      <!-- Popular Movies -->
      <section class="popular-movies">
        <h2>Popular Movies</h2>
        <div class="movie-grid">
          <div v-for="i in 10" :key="i" class="movie-card">
            <img :src="`src/static/home.jpg?height=300&width=200&text=Movie ${i}`"
              :alt="`Movie ${i}`" />
            <div class="movie-info">
              <h3>Movie Title {{ i }}</h3>
              <div class="movie-meta">
                <span class="year">2023</span>
                <div class="rating">
                  <span class="star">⭐</span>
                  <span>{{ (Math.random() * 2 + 3).toFixed(1) }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>

    <!-- Navigation Panel -->

  </div>
</template>

<script setup>

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
  margin-left: auto;
  margin-right: auto;
  /* Added this line */
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

.header .container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.search-bar {
  display: flex;
}

.search-bar input {
  padding: 0.5rem;
  border: none;
  border-radius: 4px 0 0 4px;
}

.search-button {
  background-color: #4a4a4a;
  border: none;
  padding: 0.5rem;
  border-radius: 0 4px 4px 0;
  cursor: pointer;
}

.main-content {
  padding: 2rem 1rem 5rem;
  /* Increased bottom padding */
  flex-grow: 1;
  overflow-y: auto;
}

.featured-movie,
.popular-movies {
  margin-bottom: 2rem;
}

h2 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.featured-movie-card {
  position: relative;
  border-radius: 8px;
  overflow: hidden;
}

.featured-movie-card img {
  width: 100%;
  height: auto;
}

.featured-movie-info {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 1rem;
  background: linear-gradient(transparent, rgba(0, 0, 0, 0.8));
}

.watch-button {
  background-color: #e50914;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 0.5rem;
}

.movie-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
  gap: 1rem;
}

.movie-card {
  background-color: #2c2c2c;
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

.movie-meta {
  display: flex;
  justify-content: space-between;
  font-size: 0.8rem;
  color: #b3b3b3;
}


@media (min-width: 768px) {
  .movie-grid {
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  }
}

@media (max-width: 600px) {
  /* .app {
        width: 400px;
    } */
}

@media (max-width: 400px) {
    .app {
        width: 375px;
    }
}
</style>