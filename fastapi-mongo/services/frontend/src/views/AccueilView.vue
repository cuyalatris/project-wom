<template>
  <div>
    <h1>Accueil</h1>
    <AccueilComponent/>
  </div>
</template>

<script>
import AccueilComponent from "@/components/AccueilComponent.vue"
export default {
    inject: ["loggedin"],
    methods: {
        checkLoggedIn() {
            console.log(this.loggedin);
        }
    },
    components: { AccueilComponent }
}
</script>
