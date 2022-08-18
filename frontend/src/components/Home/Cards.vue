<template>
    <div class="relative mx-auto w-full">
        <div class="rounded-lg bg-white p-2 shadow">
        <div class="relative flex h-28 justify-center overflow-hidden rounded-lg">
            <div class="w-full transform transition-transform duration-500 ease-in-out hover:scale-110">
            <div class="absolute inset-0 bg-black opacity-75">
                <img src="https://images.unsplash.com/photo-1508997449629-303059a039c0?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80" alt="">
            </div>
            </div>

            <div class="absolute bottom-0 mb-2 flex justify-center">
            <div class="flex space-x-5 space-x-reverse overflow-hidden rounded-lg bg-white px-4 py-1 shadow">
                <p class="flex items-center">
                <svg class="ml-2 h-4 w-4 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                1
                </p>

                <p class="flex items-center">
                <svg class="ml-2 h-4 w-4 text-yellow-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                2
                </p>

                <p class="flex items-center">
                <svg class="ml-2 h-4 w-4 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                3
                </p>
            </div>
            </div>
        </div>

        <div class="mt-4">
            <h2 class="text-base font-medium text-gray-800 md:text-lg"> {{event.name}}</h2>
            <p class="mt-1 text-sm text-gray-800">{{event.description}}</p>
        </div>

        <div class="mt-4 grid grid-cols-2 grid-rows-2 gap-4">
            <p class="flex items-center text-gray-800">
            <svg class="ml-2 h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 15.546c-.523 0-1.046.151-1.5.454a2.704 2.704 0 01-3 0 2.704 2.704 0 00-3 0 2.704 2.704 0 01-3 0 2.704 2.704 0 00-3 0 2.704 2.704 0 01-3 0 2.701 2.701 0 00-1.5-.454M9 6v2m3-2v2m3-2v2M9 3h.01M12 3h.01M15 3h.01M21 21v-7a2 2 0 00-2-2H5a2 2 0 00-2 2v7h18zm-3-9v-2a2 2 0 00-2-2H8a2 2 0 00-2 2v2h12z"></path></svg>
            <span> دورة </span>
            </p>
            <p class="flex items-center text-gray-800">
            <svg class="ml-2 h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
            </svg>
            <span> {{event.city}} </span>
            </p>
            <p class="flex items-center text-gray-800">
            <svg class="ml-2 h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
            <span> {{event.num_of_attendees}} </span>
            </p>
            <p class="flex items-center text-gray-800">
            <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
            <span> 2 أيام</span>
            </p>
        </div>

        <div class="mt-4 w-full flex items-center justify-between space-x-2 space-x-reverse">
            <router-link :to="{name: 'EventID',params: {id: event.id}}" class="w-full rounded-md font-medium bg-primary py-2 text-center text-black"> عرض </router-link>
            <router-link :to="{name: 'EventEditID',params: {id: event.id}}" class="w-full rounded-md font-medium bg-gray-100 py-2 text-center text-secondary"> تعديل </router-link>
        </div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'Cards',
    props: {
        event: Object
    }
}
</script>