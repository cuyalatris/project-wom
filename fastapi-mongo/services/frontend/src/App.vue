<template>
  <div class="header">
    <HeaderComponent/>
    <nav>
      <router-link to="/">Home</router-link> |
      <!-- <router-link to="/about">About</router-link> | -->
      <router-link to="/accueil">Accueil</router-link> |
      <router-link to="/connexion_inscription">Sign In/Log In</router-link>
    </nav>
  </div>
  <router-view/>
</template>

<script>
import HeaderComponent from '@/components/HeaderComponent.vue'

export default {
  components: {
    HeaderComponent
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
