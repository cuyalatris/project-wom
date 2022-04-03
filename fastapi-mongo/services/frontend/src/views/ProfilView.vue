<template>
  <div>
    <ProfilComponent/>
    <div v-if="!changingPassword" id="connexion">
      <FavoriteComponent/>
      <ui-button raised @click="changeForm()">Change password</ui-button>
    </div>
    <div v-if="changingPassword" id="inscription">
      <ChangePasswordComponent/>
      <ui-button raised @click="changeForm()">Go Back</ui-button>
    </div>
  </div>
</template>

<script>
import ProfilComponent from '@/components/ProfilComponent.vue'
import ChangePasswordComponent from '@/components/ChangePasswordComponent.vue'
import FavoriteComponent from '@/components/FavoriteComponent.vue'

export default {
  name : "ProfilView",
  components: {
      ProfilComponent,
      ChangePasswordComponent,
      FavoriteComponent
  },
    data() {
        return {
            changingPassword: false
        }
    },
    methods: {
    changeForm() {
        this.changingPassword = !this.changingPassword
        this.loggedin = true
        console.log(this.loggedin)
        }
    }
}
</script>
