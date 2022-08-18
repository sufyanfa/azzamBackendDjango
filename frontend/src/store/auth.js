import vuex from 'vuex'
import axios from 'axios'
import router from '../router'
export default {
    namespaced: true,
    state:{
        authenticated:false,
        token : "",
        user:{}
    },
    getters:{
        authenticated(state){
            return state.authenticated
        },
        token(state){
            return state.token
        },
        user(state){
            return state.user
        }
    },
    mutations:{
        SET_AUTHENTICATED (state, value) {
            state.authenticated = value
        },
        SET_TOKEN (state, value) {
            state.token = value
        },
        SET_USER (state, value) {
            state.user = value
        }
    },
    actions:{
        login({commit}, payload){
            if(payload.token){
                commit('SET_TOKEN',payload.token)
                commit('SET_USER',payload.user)
                commit('SET_AUTHENTICATED',true)
                router.push({name:'Home'})
            }else{
                commit('SET_AUTHENTICATED',false)
                commit('SET_TOKEN',null)
                commit('SET_USER',{})
                router.push({name:'LogIn'})
            }
        },
        logout({commit}){
            commit('SET_USER',{})
            commit('SET_TOKEN','')
            commit('SET_AUTHENTICATED',false)
            router.push({name:'LogIn'})
            axios.defaults.headers.post['Authorization'] = '';
        }
    }
}