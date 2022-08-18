import { createApp } from 'vue'
import './app.css'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

createApp(App).use(store).use(router, axios).mount('#app')

axios.defaults.baseURL = import.meta.env.VITE_API_URL
axios.defaults.headers.post['Authorization'] = `Bearer ${store.state.auth.token}`;
