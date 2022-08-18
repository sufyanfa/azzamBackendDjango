<template>
    <aside class="w-full md:w-64 bg-gray-800 md:min-h-screen">
        <div class="flex items-center justify-between bg-gray-900 p-4 h-16">
            <a href="/home" class="flex items-center">
                <img src="../../assets/images/azzamWithName.svg" alt="عزام">
            </a>
            <div class="flex md:hidden">
                <button type="button" v-on:click="showMenu = !showMenu"
                        class="text-gray-300 hover:text-gray-500 focus:outline-none focus:text-gray-500">
                    <svg class="fill-current w-8" fill="none" stroke-linecap="round" stroke-linejoin="round"
                        stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
                        <path d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                </button>
            </div>
        </div>
        <div class="px-2 py-6" v-if="!showMenu">
            <ul>
                <li class="px-2 py-3 bg-gray-900 rounded">
                    <a href="/home" class="flex items-center">
                        <svg class="w-6 text-gray-500" fill="none" stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2"
                            viewBox="0 0 24 24" stroke="currentColor">
                            <path
                                d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path>
                        </svg>
                        <span class="mx-2 text-gray-300">الرئيسية</span>
                    </a>
                </li>
                <li class="px-2 py-3 hover:bg-gray-900 rounded mt-2">
                    <a href="/home" class="flex items-center">
                        <svg class="w-6 text-gray-500" fill="none" stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
                            <path
                                d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path>
                        </svg>
                        <span class="mx-2 text-gray-300">جهات الإتصال</span>
                    </a>
                </li>
                <li class="px-2 py-3 hover:bg-gray-900 rounded mt-2">
                    <router-link :to="{name : 'Events'}" class="flex items-center">
                        <svg class="w-6 text-gray-500" fill="none" stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
                            <path
                                d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
                        </svg>
                        <span class="mx-2 text-gray-300">الفعاليات</span>
                    </router-link>
                </li>
                <li class="px-2 py-3 hover:bg-gray-900 rounded mt-2">
                    <a href="/home" class="flex items-center">
                        <svg class="w-6 text-gray-500" fill="none" stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
                            <path
                                d="M16 8v8m-4-5v5m-4-2v2m-2 4h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
                        </svg>
                        <span class="mx-2 text-gray-300">التقارير</span>
                    </a>
                </li>
            </ul>
            <div class="border-t border-gray-700 -mx-2 mt-2 md:hidden"></div>
            <ul class="mt-6 md:hidden">
                <li class="px-2 py-3 hover:bg-gray-900 rounded mt-2">
                    <router-link :to="{name :'MyAccount'}" class="mx-2 text-gray-300">الإعدادات</router-link>
                </li>
                <li class="px-2 py-3 hover:bg-red-600 rounded mt-2">
                    <button class="mx-2 text-gray-300" @click="logout">خروج</button>
                </li>
            </ul>
        </div>
    </aside>
</template>
<script>
export default {
    data() {
        return {
            showMenu: false,
        }
    }
}
</script>