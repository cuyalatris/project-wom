<template>
  <div id="connexionInscription">
    <div v-if="alreadyUser" id="connexion">
      <ConnexionComponent/>
      <ui-button raised @click="changeForm()">Not a user yet ?</ui-button>
    </div>
    <div v-if="!alreadyUser" id="inscription">
      <InscriptionComponent/>
      <ui-button raised @click="changeForm()">Already a user ?</ui-button>
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
            alreadyUser: true
        }
    },
    methods: {
    changeForm() {
        this.alreadyUser = !this.alreadyUser
        console.log(this.loggedin)
        }
    }
})
</script>
