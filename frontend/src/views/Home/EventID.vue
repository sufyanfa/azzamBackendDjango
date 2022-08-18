<template>
    
<div class="flex items-center bg-gray-100">
    <div class="container max-w-6xl px-5 mx-auto my-10">
        <div class="flex items-center justify-between">
            <p class="font-bold text-md py-4">{{event.name}}</p>
            <button @click="deleteEvent()" class="flex items-center bg-red-400 hover:bg-red-500 text-gray-800 font-medium px-2 pt-2.5 pb-2 rounded-md">
                <svg class="w-5 h-5 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>                                    حذف
            </button>
        </div>
        <p class="text-sm font-normal py-4">{{event.description}}</p>
        <div class="grid gap-7 grid-cols-2 lg:grid-cols-4">
            <div class="flex items-center justify-between p-5 bg-white rounded shadow-sm">
                <div>
                    <div class="text-sm text-gray-400 ">عدد المسجلين</div>
                    <div class="flex items-center pt-1">
                        <div class="text-xl font-medium text-secondary">{{total}}</div>
                    </div>
                </div>
                <div class="text-gray-300">
                    <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
                </div>
            </div>
            <div class="flex items-center justify-between p-5 bg-white rounded shadow-sm">
                <div>
                    <div class="text-sm text-gray-400 ">تأكيد</div>
                    <div class="flex items-center pt-1">
                        <div class="text-xl font-medium text-green-500 ">22</div>
                    </div>
                </div>
                <div class="text-green-500">
                    <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                </div>
            </div>
            <div class="flex items-center justify-between p-5 bg-white rounded shadow-sm">
                <div>
                    <div class="text-sm text-gray-400 ">إنتظار</div>
                    <div class="flex items-center pt-1">
                        <div class="text-xl font-medium text-yellow-400">8</div>
                    </div>
                </div>
                <div class="text-yellow-400">
                    <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                </div>
            </div>
            <div class="flex items-center justify-between p-5 bg-white rounded shadow-sm">
                <div>
                    <div class="text-sm text-gray-400 ">رفض</div>
                    <div class="flex items-center pt-1">
                        <div class="text-xl font-medium text-red-400 ">2</div>
                    </div>
                </div>
                <div class="text-red-400">
                    <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18.364 18.364A9 9 0 005.636 5.636m12.728 12.728A9 9 0 015.636 5.636m12.728 12.728L5.636 5.636"></path></svg>
                </div>
            </div>
        </div>
    </div>
</div>
            
</template>
<script>
import axios from 'axios'
import Aside from '../../components/Home/Aside.vue'
import Navbar from '../../components/Home/Navbar.vue'
export default {
    name: "EventID",
    props: ['id'],
    components: { Aside, Navbar },
    data() {
        return {
            eventID: this.id,
            event: [],
            attendences : [],
            count: 0,
            total : 0,
            satus: []
        }
    },
    created() {
        this.getEvent()
    },
    mounted() {
        document.title = `الحدث ${this.event.name} | عزام`
    },
    methods: {
        async getEvent() {
            axios.post(`get-event-details/${this.id}/`)
            .then(response => {
                this.event = response.data.event,
                this.attendences = response.data.attendences
                this.count = response.data.count_attendees_will_not_attend
                this.total = response.data.count
            }).catch(error => {
                console.log(error)
            })
        },
        deleteEvent() {
            axios.post(`delete-event/${this.id}/`)
            .then(response => {
                this.$router.push('/home')
            }).catch(error => {
                console.log(error)
            })
        }
    }

}
</script>