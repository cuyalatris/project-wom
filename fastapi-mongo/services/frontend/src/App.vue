<template>
  <div class="header">
    <HeaderComponent/>
    <nav>
      <!-- <router-link to="/">Home</router-link> | -->
      <!-- <router-link to="/about">About</router-link> | -->
      <router-link v-if="store.get_access_token() !== ''" to="/accueil">Accueil | </router-link>
      <router-link v-if="store.get_access_token() == ''" to="/connexion_inscription">Sign In/Log In</router-link>
      <router-link v-if="store.get_access_token() !== ''" to="/profil">Profil</router-link>
    </nav>
  </div>
  <router-view/>
</template>

<script>
import HeaderComponent from '@/components/HeaderComponent.vue'
import { store } from './store.js'

export default {
  components: {
    HeaderComponent
  },
  data() {
    return {
      store
    }
  }
}

</script>


<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.header {
  margin: -10px;
  nav {
    padding: 30px;

    a {
      font-weight: bold;
      color: #2c3e50;

      &.router-link-exact-active {
        color: #42b983;
      }
    }
  }
}
</style>
