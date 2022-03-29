<template>
  <div>
    <h1>Accueil</h1>
  </div>
</template>

<script>
export default {
  inject: ['loggedin'],
  methods: {
    checkLoggedIn() {
      console.log(this.loggedin)
    }
  }
}
</script>
