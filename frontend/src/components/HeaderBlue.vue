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
        <div class="w-auto hidden lg:block">
            <ul class="flex items-center mr-10 space-x-8 space-x-reverse">
            <li class="nav__item--des"><a href="#solution">الحلول</a></li>
            <li class="nav__item--des"><a href="#features">المميزات</a></li>
            <li class="nav__item--des"><a href="#contact">تواصل</a></li>
            </ul>
        </div>
        </div>
    </div>
    <div class="w-auto">
        <div class="flex flex-wrap items-center">
        <div class="w-auto hidden lg:block">
            <div class="flex flex-wrap items-center">
            <div class="w-auto">
                <router-link to="/login" class="block py-2 px-4 mr-4 font-medium text-gray-300 hover:text-gray-800 rounded-10">دخول</router-link>
            </div>
            <div class="w-auto">
                <router-link to="/signup">
                    <button class="button__primary">
                    التسجيل
                    </button>
                </router-link>
            </div>
            </div>
        </div>
        <div v-on:click="showMenu = !showMenu" class="w-auto lg:hidden">
            <a href="#">
            <svg class="navbar-burger text-gray-800" width="51" height="51" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect width="56" height="56" rx="28" fill="currentColor"></rect>
                <path d="M37 32H19M37 24H19" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            </svg>
            </a>
        </div>
        </div>
    </div>
    </div>
    <div v-if="showMenu" class="fixed top-0 left-0 bottom-0 w-4/6 sm:max-w-xs z-50">
    <div class="navbar-backdrop fixed inset-0 bg-gray-800 opacity-80"></div>
    <nav class="relative z-10 px-4 py-8 bg-gray-900 text-white h-full">
        <div class="flex flex-wrap justify-between h-full">
        <div class="w-full">
            <div class="flex items-center justify-between">
            <div class="w-auto">
                <router-link to="/" class="inline-block">
                <img src="../assets/images/azzamWithName.svg" alt="عزام">
                </router-link>
            </div>
            <div v-on:click="showMenu = !showMenu" class="w-auto">
                <a class="navbar-burger" href="#">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M6 18L18 6M6 6L18 18" stroke="#111827" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
                </svg>
                </a>
            </div>
            </div>
        </div>
        <div class="flex flex-col justify-center py-8 w-full">
            <ul>
            <li class="mb-12"><a class="nav__item-ph" href="#solution">الحلول</a></li>
            <li class="mb-12"><a class="nav__item-ph" href="#features">المميزات</a></li>
            <li class="mb-12"><a class="nav__item-ph" href="#contact">تواصل</a></li>
            </ul>
        </div>
        <div class="flex flex-col justify-center w-full">
            <div class="flex flex-wrap">
            <div class="w-full">
                <router-link to="/login" class="py-2 px-5 block w-full text-center text-lg border text-gray-100 font-medium rounded-10">
                    دخول
                </router-link>
            </div>
            <div class="w-full">
                <router-link to="/signup" class="py-2 mt-2 px-5 block w-full text-center text-lg border bg-primary text-gray-900 font-medium rounded-10">
                دخول
                </router-link>
            </div>
            </div>
        </div>
        </div>
    </nav>
    </div>
</header>
</template>
<script>

export default ({
    data() {
        return {
            showMenu :false
        };
    }
})
</script>
