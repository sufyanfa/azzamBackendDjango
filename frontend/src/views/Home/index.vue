<template>
    <div v-if="isEvents" class="grid w-full grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
        <Cards v-for="event in events"
        v-bind:key="event.id"
        v-bind:event="event" 
        />
    </div>
    <NoEvents v-else />
    <div v-if="isEvents" class="flex space-x-2 justify-center absolute bottom-4 left-8">
        <div>
        <router-link :to="{name: 'EventCreate'}"  class="inline-block p-2 rounded-full bg-primary text-black shadow-md transition hover:scale-105 w-12 h-12">
            <svg class="mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path></svg>
        </router-link>
        </div>
    </div>
</template>
<script>
import {onMounted, ref } from 'vue'
import {useStore} from 'vuex'
import axios from 'axios'
import Aside from '../../components/Home/Aside.vue'
import Navbar from '../../components/Home/Navbar.vue'
import Cards from '../../components/Home/Cards.vue'
import NoEvents from '../../components/Home/NoEvents.vue'

export default {
    name: "Home",
    components: { Aside, Navbar, Cards, NoEvents },
    setup() {
        const events = ref([])
        const isEvents = ref(false)
        const errors = ref([])
        const store = useStore()

        const fetchEvents = async () => {
            try {
                if(store.state.auth.token) {
                    axios.defaults.headers.post['Authorization'] = `Bearer ${store.state.auth.token}`;
                    const { data } = await axios.post('/get-all-events-of-user-logged/')
                    events.value = data
                    if(data.length > 0) {
                        isEvents.value = true
                    }
                }
            } catch (error) {
                errors.value = 'حصل خطأ ما'
            }
        }

       
        fetchEvents()

        return {
            events,
            isEvents,
            errors,
            fetchEvents
        }
    }
}
</script>