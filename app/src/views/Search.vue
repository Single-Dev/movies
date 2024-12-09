<template>
    <div class="search-panel">
      <main class="main-content">
        <div class="search-container">
          <div class="search-input-wrapper">
            <input
              v-model="searchQuery"
              type="text"
              placeholder="Search for movies..."
              class="search-input"
              @keyup.enter="handleSearch"
            />
            <button @click="handleSearch" class="search-button">
              <span class="search-icon">🔍</span>
              Search
            </button>
          </div>
  
          <div class="filters">
            <div class="filter-item">
              <label for="genre">Genre:</label>
              <select v-model="selectedGenre" id="genre" class="select-input">
                <option value="">All Genres</option>
                <option value="action">Action</option>
                <option value="comedy">Comedy</option>
                <option value="drama">Drama</option>
                <option value="sci-fi">Sci-Fi</option>
              </select>
            </div>
  
            <div class="filter-item">
              <label for="year-range">Year Range: {{ yearRange[0] }} - {{ yearRange[1] }}</label>
              <div class="range-slider">
                <input
                  type="range"
                  id="year-range-min"
                  v-model.number="yearRange[0]"
                  min="1900"
                  max="2023"
                  class="range-input"
                />
                <input
                  type="range"
                  id="year-range-max"
                  v-model.number="yearRange[1]"
                  min="1900"
                  max="2023"
                  class="range-input"
                />
              </div>
            </div>
          </div>
        </div>
  
        <div class="search-results" v-if="filteredMovies.length > 0">
          <div v-for="movie in filteredMovies" :key="movie.id" class="movie-card">
            <img :src="movie.poster" :alt="movie.title" class="movie-poster" />
            <div class="movie-info">
              <h3 class="movie-title">{{ movie.title }}</h3>
              <p class="movie-details">{{ movie.year }} • {{ movie.genre }}</p>
            </div>
          </div>
        </div>
  
        <p v-else class="no-results">No results found. Try adjusting your search criteria.</p>
      </main>

    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue'
  
  const searchQuery = ref('')
  const selectedGenre = ref('')
  const yearRange = ref([1900, 2024])
  
  const allMovies = [
    { id: 1, title: 'Home Alone', year: 1994, genre: 'Sci-Fi', poster: 'src/static/home.jpg?height=300&width=200&text=Inception' },
    { id: 2, title: 'Rio', year: 2022, genre: 'Drama', poster: '../static/rio.jpg?height=300&width=200&text=Shawshank' },
    { id: 3, title: 'Puss In Buts', year: 2008, genre: 'Action', poster: '../static/puss.jpg?height=300&width=200&text=Dark+Knight' },
    { id: 4, title: 'Beckzodiy', year: 2006, genre: 'Crime', poster: '../static/my.jpg?height=300&width=200&text=Pulp+Fiction' },
    { id: 5, title: 'King Kong', year: 2018, genre: 'Drama', poster: '../static/king.jpg?height=300&width=200&text=Forrest+Gump' },
    { id: 6, title: 'Zorro', year: 1999, genre: 'Sci-Fi', poster: '../static/zorro.jpg?height=300&width=200&text=The+Matrix' },
  ]
  
  const filteredMovies = computed(() => {
    return allMovies.filter(movie => {
      const matchesSearch = movie.title.toLowerCase().includes(searchQuery.value.toLowerCase())
      const matchesGenre = selectedGenre.value === '' || movie.genre.toLowerCase() === selectedGenre.value.toLowerCase()
      const matchesYear = movie.year >= yearRange.value[0] && movie.year <= yearRange.value[1]
      return matchesSearch && matchesGenre && matchesYear
    })
  })
  
  const handleSearch = () => {
    // The search is now handled automatically by the computed property
    // This function is kept for potential future use (e.g., analytics)
    console.log('Search performed:', searchQuery.value)
  }
  </script>
  
  <style scoped>
  .search-panel {
    font-family: Arial, sans-serif;
    background-color: #1a1a1a;
    color: #ffffff;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }
  
  .main-content {
    flex-grow: 1;
    padding: 1rem;
    overflow-y: auto;
  }
  
  .search-container {
    margin-bottom: 2rem;
  }
  
  .search-input-wrapper {
    display: flex;
    margin-bottom: 1rem;
  }
  
  .search-input {
    flex-grow: 1;
    padding: 0.5rem;
    font-size: 1rem;
    border: none;
    border-radius: 4px 0 0 4px;
  }
  
  .search-button {
    background-color: #e50914;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    font-size: 1rem;
    cursor: pointer;
    border-radius: 0 4px 4px 0;
    display: flex;
    align-items: center;
  }
  
  .search-icon {
    margin-right: 0.5rem;
  }
  
  .filters {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
  
  .filter-item {
    display: flex;
    flex-direction: column;
  }
  
  .filter-item label {
    margin-bottom: 0.5rem;
  }
  
  .select-input {
    padding: 0.5rem;
    font-size: 1rem;
    background-color: #2c2c2c;
    color: white;
    border: 1px solid #4a4a4a;
    border-radius: 4px;
  }
  
  .range-slider {
    display: flex;
    gap: 1rem;
  }
  
  .range-input {
    flex-grow: 1;
    /* -webkit-appearance: none; */
    width: 100%;
    height: 5px;
    background: #4a4a4a;
    outline: none;
    opacity: 0.7;
    transition: opacity 0.2s;
  }
  
  .range-input:hover {
    opacity: 1;
  }
  
  .range-input::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px;
    height: 20px;
    background: #e50914;
    cursor: pointer;
    border-radius: 50%;
  }
  
  .range-input::-moz-range-thumb {
    width: 20px;
    height: 20px;
    background: #e50914;
    cursor: pointer;
    border-radius: 50%;
  }
  
  .search-results {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    gap: 1rem;
  }
  
  .movie-card {
    background-color: #2c2c2c;
    border-radius: 4px;
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
    margin: 0;
  }
  
  .no-results {
    text-align: center;
    color: #b3b3b3;
    margin-top: 2rem;
  }
  
  
  @media (min-width: 768px) {
    .search-input-wrapper {
      max-width: 600px;
      margin: 0 auto 1rem;
    }
  
    .filters {
      flex-direction: row;
      justify-content: center;
      align-items: flex-end;
    }
  
    .filter-item {
      min-width: 200px;
    }
  
    .search-results {
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    }

  }
  </style>