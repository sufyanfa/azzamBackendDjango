<template>
    <nav class="hidden md:flex justify-between items-center bg-white px-8 shadow-md h-16">
        <div>
            <p class="font-bold">
                  أهلاُ بك
                {{ user.username ? user.username : 'زائر' }}
            </p>
        </div>
        <div class="flex items-center">
            <router-link :to="{name : 'MyAccount'}">
                <svg class="w-6 h-6 mx-2 text-gray-700 focus:outline-none" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
            </router-link>
            <button v-on:click="logout" class="mx-2 text-red-400 hover:text-red-600 focus:outline-none">
                <svg class="h-6" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        viewBox="0 0 24 24" stroke="currentColor">
                    <path
                        d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"></path>
                </svg>
            </button>
        </div>
    </nav>
</template>
<script>
import axios from 'axios'
import { useStore } from 'vuex'
export default {
    setup() {
        const store = useStore()
        const user = store.state.auth.user

        function logout() {
            axios.post('/logout/')
            .then(response => {
                store.dispatch('auth/logout')
            })
            .catch(error => {
              console.log(error)
            })
        }

        return{
            user,
            logout
        }

    },
    // mounted(){
    //     this.user = this.$store.state.user
    // },
    // methods:{
    //     ...mapActions({
    //         signOut:"auth/logout"
    //     }),
    //     async logout(){
    //         await axios.post('/logout/')
    //         .then(({data})=>{
    //             this.signOut()
    //         })
    //     }
    // }
}
</script>
