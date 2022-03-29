import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import BalmUI from 'balm-ui'
import BalmUIPlus from 'balm-ui-plus'
import 'balm-ui-css'

const app = createApp(App)
app.use(router)
app.use(BalmUI)
app.use(BalmUIPlus)
app.provide('loggedin',false)
app.mount('#app')