<script>
import { RouterLink, RouterView } from 'vue-router'
import NavBar from './components/nav/NavBar.vue';
import axios from 'axios'

export default {
  components:{
    NavBar,
    RouterView
  },
  data() {
    return {
      user: {
        id: null,
        firstName: '',
        lastName: '',
        username: '',
        profile_pic: ''
      },
    }
  },

  mounted() {
    Telegram.WebApp.ready();
    Telegram.WebApp.expand();
    if (Telegram && Telegram.WebApp) {
      const tgUser = Telegram.WebApp.initDataUnsafe.user;
      this.user = {
        id: tgUser.id,
        firstName: tgUser.first_name,
        lastName: tgUser.last_name,
        username: tgUser.username,
        // profile_pic: tgUser.photo_url,
      };
      console.log(tgUser)
    }
    console.log(Telegram.WebApp.initDataUnsafe);
  },
}

</script>

<template>
  <div class="app">
    <div class="content">
      <RouterView :user="user"/>
      <NavBar />
    </div>
  </div>
</template>

<style scoped>
@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;
    padding: 1rem 0;
    margin-top: 1rem;
  }
}

/* 
.content {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
    width: 100%;
    background-color: #fff;
    margin: 0 auto;
    padding: 5rem 10px;
}

.app {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
} */


/* @media (max-width: 390px) {
    .content {
        width: 350px;
    }
} */
</style>
