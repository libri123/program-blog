import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from 'store'
import 'bulma/css/bulma.css'

const app = createApp(App)
app.use(router, store)
app.mount('#app')