<template>
  <div id="connexionInscription">
    <div v-if="alreadyUser" id="connexion">
      <ConnexionComponent/>
      <button v-on:click="changeForm()">Pas encore inscrit ?</button>
    </div>
    <div v-if="!alreadyUser" id="connexioninscription">
      <InscriptionComponent/>
      <button @click="changeForm()">Déjà inscrit ?</button>
    </div>
  </div>
</template>

<script>
import ConnexionComponent from '@/components/ConnexionComponent.vue'
import InscriptionComponent from '@/components/InscriptionComponent.vue'

export default ({
    inject: ['loggedin'],
    components: {
        ConnexionComponent,
        InscriptionComponent
    },
    data() {
        return {
            alreadyUser: false
        }
    },
    methods: {
    changeForm() {
        this.alreadyUser = !this.alreadyUser
        this.loggedin = true
        console.log(this.loggedin)
        }
    }
})
</script>
