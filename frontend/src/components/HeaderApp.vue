<template>
    <header>
        <div class="flex items-center justify-between container py-4">
        <div class="w-auto">
            <div class="flex flex-wrap items-center">
            <div class="w-auto ml-14">
                <router-link to="/">
                <img src="../assets/images/azzamWithName.svg" alt="عزام">
                </router-link>
            </div>
            </div>
        </div>
        <div class="w-auto">
            <div class="flex flex-wrap items-center">
            <div class="w-auto block">
                <div class="flex flex-wrap items-center">
                <div class="w-auto" v-show="currentUrl==='/signup'">
                    <router-link to="/login">
                        <button class="button__primary">
                        دخول    
                        </button>
                    </router-link>
                </div>

                <div class="w-auto" v-show="currentUrl==='/login'">
                    <router-link to="/signup">
                        <button class="button__primary">
                        تسجيل
                        </button>
                    </router-link>
                </div>
                </div>
            </div>
            </div>
        </div>
        </div>
  </header>
</template>
<script>
export default {
    data () {
        return {
            currentUrl: " ",
        }
    },
    created() {
        this.currentUrl = window.location.pathname;
    }
}
</script>>