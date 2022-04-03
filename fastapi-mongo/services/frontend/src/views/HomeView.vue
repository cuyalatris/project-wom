<template>
  <div class="home">
    <!-- <ui-button @click="getUserData()">Test logged in</ui-button> -->
    <p>{{ store.access_token }}</p>
    <ui-button @click="getUserData()">Test</ui-button>
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import {store} from './../store.js';
import HelloWorld from '@/components/HelloWorld.vue'
import axios from 'axios'
axios.defaults.baseURL = 'http://0.0.0.0:5000/'
export default {
  name: 'HomeView',
  components: {
    HelloWorld
  },
  data() {
    return {
      store,
      current_access_token: '',
      current_user_data: {}
    }
  },
  methods: {
    getUserData() {
      this.current_access_token = store.get_access_token()
      this.current_user_data = axios.get('/user/users/me', {
        params: {
          token: this.current_access_token
        }
      })
        .then((response) => {
          console.log(response.data)
        })
      console.log(this.current_user_data)
    }
  }
}
</script>
