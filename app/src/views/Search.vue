<template>
  <div class="search-page">
    <div class="search-container">
      <input 
        v-model="searchQuery" 
        @input="handleSearch" 
        type="text" 
        placeholder="Search for movies..."
        class="search-input"
      >
      <button @click="handleSearch" class="search-button">
        🔍 Search
      </button>
    </div>

    <div class="filters">
      <div class="filter-group">
        <label>Genre:</label>
        <select v-model="selectedGenre" @change="handleSearch">
          <option value="">All Genres</option>
          <option value="action">Action</option>
          <option value="drama">Drama</option>
          <option value="sci-fi">Sci-Fi</option>
          <option value="crime">Crime</option>
          <option value="comedy">Comedy</option>
          <option value="animation">Animation</option>
        </select>
      </div>

      <div class="filter-group">
        <label>Language:</label>
        <select v-model="selectedLanguage" @change="handleSearch">
          <option value="">All Languages</option>
          <option value="en">English</option>
          <option value="uz">Uzbek</option>
          <option value="ru">Russian</option>
        </select>
      </div>

      <div class="filter-group">
        <label>Year Range: {{ yearRange[0] }} - {{ yearRange[1] }}</label>
        <div class="year-slider">
          <input 
            type="range" 
            v-model.number="yearRange[0]" 
            :min="1900" 
            :max="2024" 
            @change="handleSearch"
          >
          <input 
            type="range" 
            v-model.number="yearRange[1]" 
            :min="1900" 
            :max="2024" 
            @change="handleSearch"
          >
        </div>
      </div>
    </div>

    <div v-if="loading" class="loading">Searching...</div>
    
    <div v-else class="movie-grid">
      <div v-for="movie in filteredMovies" :key="movie.id" class="movie-card">
        <img :src="movie.poster" :alt="movie.title" class="movie-poster">
        <div class="movie-info">
          <h3>{{ movie.title }}</h3>
          <div class="movie-meta">
            <span class="year">{{ movie.year }}</span>
            <span class="duration">{{ movie.duration }}</span>
            <span class="age-rating">{{ movie.ageRating }}</span>
          </div>
          <p class="genre">{{ movie.genre }}</p>
          <p class="language-tag">{{ getLanguageName(movie.language) }}</p>
          <div class="rating">
            <span class="stars">★★★★☆</span>
            <span class="rating-value">{{ movie.rating.toFixed(1) }}</span>
          </div>
          <p class="description">{{ truncateDescription(movie.description) }}</p>
          <p class="director">Director: {{ movie.director }}</p>
          <div class="action-buttons">
            <button @click="addToFavorites(movie)" class="btn favorite-btn">
              ❤ Favorite
            </button>
            <button @click="watchTrailer(movie)" class="btn trailer-btn">
              ▶ Trailer
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue'

export default {
  name: 'SearchPage',
  setup() {
    const searchQuery = ref('')
    const selectedGenre = ref('')
    const selectedLanguage = ref('')
    const yearRange = ref([1900, 2024])
    const loading = ref(false)

    // Language mapping for display
    const languageNames = {
      en: 'English',
      uz: 'Uzbek',
      ru: 'Russian'
    }

    const movies = ref([
      {
        id: 1,
        title: 'Home Alone',
        year: 1994,
        genre: 'Comedy',
        language: 'en',
        poster: 'https://i.postimg.cc/DwNfP0Sg/home.jpg',
        duration: '1h 43m',
        ageRating: 'PG',
        rating: 7.6,
        description: 'An eight-year-old troublemaker must protect his house from a pair of burglars when he is accidentally left home alone by his family during Christmas vacation.',
        director: 'Chris Columbus'
      },
      {
        id: 2,
        title: 'King kong',
        year: 2011,
        genre: 'Animation',
        language: 'en',
        poster: 'https://i.postimg.cc/Bn3hHxVR/king.jpg',
        duration: '1h 36m',
        ageRating: 'G',
        rating: 6.9,
        description: 'When Blu, a domesticated macaw from small-town Minnesota, meets the fiercely independent Jewel, he takes off on an adventure to Rio de Janeiro with the bird of his dreams.',
        director: 'Carlos Saldanha'
      },
      // Add more mock movies here
    ])

    const getLanguageName = (code) => {
      return languageNames[code] || code
    }

    const filteredMovies = computed(() => {
      return movies.value.filter(movie => {
        const matchesSearch = movie.title
          .toLowerCase()
          .includes(searchQuery.value.toLowerCase())
        const matchesGenre = !selectedGenre.value || movie.genre.toLowerCase() === selectedGenre.value
        const matchesLanguage = !selectedLanguage.value || movie.language === selectedLanguage.value
        const matchesYear = movie.year >= yearRange.value[0] && movie.year <= yearRange.value[1]
        
        return matchesSearch && matchesGenre && matchesLanguage && matchesYear
      })
    })

    const handleSearch = async () => {
      loading.value = true
      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 500))
      loading.value = false
    }

    const truncateDescription = (description, maxLength = 100) => {
      return description.length > maxLength
        ? description.slice(0, maxLength) + '...'
        : description
    }

    const addToFavorites = (movie) => {
      // Implement favorite functionality
      console.log(`Added ${movie.title} to favorites`)
    }

    const watchTrailer = (movie) => {
      // Implement trailer functionality
      console.log(`Opening trailer for ${movie.title}`)
    }

    return {
      searchQuery,
      selectedGenre,
      selectedLanguage,
      yearRange,
      loading,
      filteredMovies,
      handleSearch,
      getLanguageName,
      truncateDescription,
      addToFavorites,
      watchTrailer
    }
  }
}
</script>

<style scoped>
.search-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  min-height: 100vh;
  background-color: #1a1a1a;
  color: white;
}

.search-container {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.search-input {
  flex: 1;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #333;
  border-radius: 4px;
  background-color: #333;
  color: white; /* Fixed text color */
}

.search-input::placeholder {
  color: #999; /* Made placeholder text visible */
}

.search-button {
  padding: 10px 20px;
  background-color: #ff0000;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.search-button:hover {
  background-color: #cc0000;
}

.filters {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
  flex-wrap: wrap; /* Added for better mobile responsiveness */
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 5px;
  min-width: 150px; /* Ensure filters have enough width */
}

.filter-group select {
  padding: 8px;
  border-radius: 4px;
  background-color: #333;
  color: white;
  border: 1px solid #444;
  cursor: pointer;
}

.filter-group select:hover {
  border-color: #666;
}

.year-slider {
  width: 300px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.year-slider input[type="range"] {
  width: 100%;
  accent-color: #ff0000;
}

.movie-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
  padding: 20px 0;
}

.movie-card {
  background-color: #222;
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.2s;
  display: flex;
  flex-direction: column;
}

.movie-poster {
  width: 100%;
  height: 300px;
  object-fit: cover;
}

.movie-info {
  padding: 15px;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.movie-info h3 {
  margin: 0 0 10px 0;
  font-size: 1.2em;
}

.movie-meta {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
  font-size: 0.9em;
  color: #999;
}

.genre, .language-tag {
  margin: 5px 0;
  font-size: 0.9em;
  color: #999;
}

.language-tag {
  display: inline-block;
  background-color: #444;
  padding: 2px 8px;
  border-radius: 4px;
}

.rating {
  margin: 10px 0;
  display: flex;
  align-items: center;
}

.stars {
  color: #ffd700;
  margin-right: 5px;
}

.rating-value {
  font-weight: bold;
}

.description {
  margin: 10px 0;
  font-size: 0.9em;
  color: #ccc;
  flex-grow: 1;
}

.director {
  margin: 5px 0;
  font-size: 0.9em;
  color: #999;
}

.action-buttons {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}

.btn {
  padding: 8px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.9em;
  transition: background-color 0.2s;
}

.favorite-btn {
  background-color: #4CAF50;
  color: white;
}

.trailer-btn {
  background-color: #f44336;
  color: white;
}

.btn:hover {
  opacity: 0.9;
}

@media (max-width: 768px) {
  .filters {
    flex-direction: column;
    gap: 15px;
  }
  
  .year-slider {
    width: 100%;
  }
  
  .filter-group {
    width: 100%;
  }
  .movie-card {
    max-width: 300px;
    margin: 0 auto;
  }
}
</style>