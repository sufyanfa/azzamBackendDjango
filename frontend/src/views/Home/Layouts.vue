<template>
  <div class="flex flex-col md:flex-row">
    <Aside />
    <div class="w-full md:flex-1 relative">
      <Navbar />
      <main class="px-8 py-6">
        <router-view></router-view>
      </main>
    </div>
  </div>
</template>
<script>
import {mapActions} from 'vuex'
import axios from 'axios'
import Aside from '../../components/Home/Aside.vue'
import Navbar from '../../components/Home/Navbar.vue'
export default {
    name: "HomeLayouts",
    components: { Aside, Navbar},
    methods: {
        ...mapActions({
            signOut:"auth/logout"
        }),
        logout() {
            axios
            .post('/logout/')
                .then(response => {
                    this.signOut()
                    this.$router.push({name:"LogIn"})
                })
                .catch(error => {
                    this.$router.push({name:"Home"})
                }
            )
        }
    }
}
</script>