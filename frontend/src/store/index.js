import { createStore } from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import Cookies from "js-cookie"
import auth from './auth'

let inFifteenMinutes = new Date(new Date().getTime() + 60 * 60 * 1000)
const store = createStore({
    plugins:[
      createPersistedState({
        key: 'auth',
        storage: {
          getItem: key => Cookies.get(key),
          setItem: (key, value) => Cookies.set(key, value, {expires: inFifteenMinutes}),
          removeItem: key => Cookies.remove(key)
        }
      })
    ],
    modules:{
      auth
    }
})

export default store