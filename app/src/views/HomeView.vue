<template>
  <div class="home-page">
    <main class="main-content">
      <section class="featured-movies">
        <h2 class="section-title">Featured Movies</h2>
        <div class="carousel">
          <button class="carousel-button prev" @click="prevSlide" aria-label="Previous slide">❮</button>
          <div class="carousel-container" ref="carouselContainer">
            <div
              v-for="(movie, index) in featuredMovies"
              :key="movie.id"
              class="carousel-slide"
              :class="{ active: index === currentSlide }"
            >
              <img :src="movie.poster" :alt="movie.title" class="carousel-image" />
              <div class="carousel-caption">
                <h3>{{ movie.title }}</h3>
                <p>{{ movie.description }}</p>
                <button class="watch-button">Watch Now</button>
              </div>
            </div>
          </div>
          <button class="carousel-button next" @click="nextSlide" aria-label="Next slide">❯</button>
        </div>
      </section>

      <section class="popular-movies">
        <h2 class="section-title">Popular Movies</h2>
        <div class="movie-grid">
          <div v-for="movie in popularMovies" :key="movie.id" class="movie-card">
            <img :src="movie.poster" :alt="movie.title" class="movie-poster" />
            <div class="movie-info">
              <h3 class="movie-title">{{ movie.title }}</h3>
              <p class="movie-details">{{ movie.year }} • {{ movie.genre }}</p>
              <div class="movie-rating">
                <span class="star">★</span>
                <span>{{ movie.rating }}</span>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const featuredMovies = [
  { id: 1, title: 'Inception', description: 'A thief who enters the dreams of others to steal secrets from their subconscious.', poster: 'src/static/home.jpg?height=400&width=600&text=Inception' },
  { id: 2, title: 'The Shawshank Redemption', description: 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.', poster: 'src/static/rio.jpg?height=400&width=600&text=Shawshank' },
  { id: 3, title: 'The Dark Knight', description: 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.', poster: 'src/static/zorro.jpg??height=400&width=600&text=Dark+Knight' },
]

const popularMovies = [
  { id: 1, title: 'Pulp Fiction', year: 1994, genre: 'Crime', rating: 8.9, poster: 'src/static/rio.jpg??height=300&width=200&text=Pulp+Fiction' },
  { id: 2, title: 'Forrest Gump', year: 1994, genre: 'Drama', rating: 8.8, poster: 'src/static/king.jpg??height=300&width=200&text=Forrest+Gump' },
  { id: 3, title: 'The Matrix', year: 1999, genre: 'Sci-Fi', rating: 8.7, poster: 'src/static/puss.jpg??height=300&width=200&text=The+Matrix' },
  { id: 4, title: 'Goodfellas', year: 1990, genre: 'Crime', rating: 8.7, poster: 'src/static/home.jpg??height=300&width=200&text=Goodfellas' },
  { id: 5, title: 'The Silence of the Lambs', year: 1991, genre: 'Thriller', rating: 8.6, poster: 'src/static/rio.jpg?height=300&width=200&text=Silence+of+the+Lambs' },
  { id: 6, title: 'Schindler\'s List', year: 1993, genre: 'Biography', rating: 8.9, poster: 'src/static/my.jpg?height=300&width=200&text=Schindler\'s+List' },
]

const currentSlide = ref(0)
const carouselContainer = ref(null)
let autoSlideInterval

const nextSlide = () => {
  currentSlide.value = (currentSlide.value + 1) % featuredMovies.length
}

const prevSlide = () => {
  currentSlide.value = (currentSlide.value - 1 + featuredMovies.length) % featuredMovies.length
}

const startAutoSlide = () => {
  autoSlideInterval = setInterval(nextSlide, 5000)
}

const stopAutoSlide = () => {
  clearInterval(autoSlideInterval)
}

onMounted(() => {
  startAutoSlide()
  carouselContainer.value.addEventListener('mouseenter', stopAutoSlide)
  carouselContainer.value.addEventListener('mouseleave', startAutoSlide)
})

onUnmounted(() => {
  stopAutoSlide()
  if (carouselContainer.value) {
    carouselContainer.value.removeEventListener('mouseenter', stopAutoSlide)
    carouselContainer.value.removeEventListener('mouseleave', startAutoSlide)
  }
})
</script>

<style scoped>
.home-page {
  font-family: Arial, sans-serif;
  background-color: #1a1a1a;
  color: #ffffff;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.header {
  background-color: #2c2c2c;
  padding: 1rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  margin: 0;
}

.main-content {
  flex-grow: 1;
  padding: 1rem;
  overflow-y: auto;
}

.section-title {
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.carousel {
  position: relative;
  width: 100%;
  height: 300px;
  overflow: hidden;
  border-radius: 8px;
  margin-bottom: 2rem;
}

.carousel-container {
  width: 100%;
  height: 100%;
  position: relative;
}

.carousel-slide {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  transition: opacity 0.5s ease-in-out;
}

.carousel-slide.active {
  opacity: 1;
}

.carousel-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.carousel-caption {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 1rem;
  background: rgba(0, 0, 0, 0.7);
  color: #ffffff;
}

.carousel-caption h3 {
  margin: 0 0 0.5rem 0;
}

.carousel-caption p {
  margin: 0 0 1rem 0;
}

.carousel-button {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0, 0, 0, 0.5);
  color: #ffffff;
  border: none;
  font-size: 1.5rem;
  padding: 0.5rem;
  cursor: pointer;
  z-index: 10;
}

.carousel-button.prev {
  left: 10px;
}

.carousel-button.next {
  right: 10px;
}

.watch-button {
  background-color: #e50914;
  color: #ffffff;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
}

.movie-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
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

.movie-poster {
  width: 100%;
  height: 225px;
  object-fit: cover;
}

.movie-info {
  padding: 0.5rem;
}

.movie-title {
  margin: 0 0 0.5rem 0;
  font-size: 1rem;
}

.movie-details {
  font-size: 0.8rem;
  color: #b3b3b3;
  margin: 0 0 0.5rem 0;
}

.movie-rating {
  display: flex;
  align-items: center;
  font-size: 0.9rem;
}

.star {
  color: #ffd700;
  margin-right: 0.25rem;
}

.bottom-nav {
  display: flex;
  justify-content: space-around;
  background-color: #2c2c2c;
  padding: 0.5rem;
  position: sticky;
  bottom: 0;
}

.nav-button {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: none;
  border: none;
  color: #ffffff;
  cursor: pointer;
}

.nav-button.active {
  color: #e50914;
}

.nav-icon {
  font-size: 1.5rem;
  margin-bottom: 0.25rem;
}

.nav-label {
  font-size: 0.8rem;
}

@media (min-width: 768px) {
  .carousel {
    height: 400px;
  }

  .movie-grid {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  }

  .bottom-nav {
    display: none;
  }
}
</style>