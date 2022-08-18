<template>
    
<div class="mt-5 md:col-span-2 md:mt-0">
    <form method="POST">
        <div class="overflow-hidden shadow sm:rounded-md">
        <div class="bg-white px-4 py-5 sm:p-6">
            <h2 class="pb-4 text-lg font-medium">تعديل الحدث</h2>

            <div class="grid grid-cols-6 gap-6">
            <div class="col-span-6 sm:col-span-3">
                <label for="name" class="event__lebel">اسم الحدث</label>
                <input type="text" name="name" id="name" autocomplete="name" v-model="event.name" class="event__input" />
            </div>

            <div class="col-span-6 sm:col-span-3">
                <label for="organizetion" class="event__lebel">اسم الجهة</label>
                <input type="text" name="organizetion" id="organizetion" autocomplete="organizetion" v-model="event.organizetion" class="event__input" />
            </div>

            <div class="col-span-6">
                <label for="description" class="event__lebel">وصف الحدث</label>
                <textarea id="description" name="description" v-model="event.description" rows="3" class="mt-1 block w-full rounded-md border border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"></textarea>
            </div>

            <div class="col-span-6">
                <label class="event__lebel"> صورة الحدث </label>
                <div class="mt-1 flex justify-center rounded-md border-2 border-dashed border-gray-300 px-6 pt-5 pb-6">
                <div class="space-y-1 text-center">
                    <svg class="mx-auto h-12 w-12 text-gray-400" stroke="currentColor" fill="none" viewBox="0 0 48 48" aria-hidden="true">
                    <path d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                    </svg>
                    <div class="flex text-sm text-gray-600">
                    <label for="file-upload" class="relative cursor-pointer rounded-md bg-white font-medium text-indigo-600 focus-within:outline-none focus-within:ring-2 focus-within:ring-indigo-500 focus-within:ring-offset-2 hover:text-indigo-500">
                        <span>Upload a file</span>
                        <input id="file-upload" name="file-upload" type="file" class="sr-only" />
                    </label>
                    <p class="pl-1">or drag and drop</p>
                    </div>
                    <p class="text-xs text-gray-500">PNG, JPG, GIF up to 10MB</p>
                </div>
                </div>
            </div>

            <div class="col-span-6 sm:col-span-3">
                <div class="flex items-start">
                    <div class="flex items-center h-5">
                    <input id="isonline" name="isonline" v-on:click="isOnline = !isOnline" v-model="event.is_online" type="checkbox" class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300 rounded">
                    </div>
                    <div class="mr-3 text-sm">
                    <label for="isonline" class="event_lebel">الحدث أونلاين</label>
                    </div>
                </div>
            </div>
            <div class="col-span-6 sm:col-span-3">
                <div class="flex items-start">
                    <div class="flex items-center h-5">
                    <input id="iscertified" name="iscertified" v-model="event.is_certified" type="checkbox" class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300 rounded">
                    </div>
                    <div class="mr-3 text-sm">
                    <label for="iscertified" class="event_lebel">يوجد شهادات</label>
                    </div>
                </div>
            </div>
            <div class="col-span-6 sm:col-span-3" v-show="isOnline">
                <label for="city" class="event__lebel"> مدينة الحدث</label>
                <input type="text" name="city" id="city" autocomplete="city" v-model="event.city" class="event__input" />
            </div>

            <div class="col-span-6 sm:col-span-3" v-show="isOnline">
                <label for="address" class="event__lebel">عنوان الحدث</label>
                <input type="text" name="address" id="address" autocomplete="address" v-model="event.address" class="event__input" />
            </div>

            <div class="col-span-6" v-show="isOnline">
                <label class="event__lebel"> موقع الحدث </label>
                <div class="mt-1 flex justify-center rounded-md border-2 border-dashed border-gray-300 px-6 pt-5 pb-6">
                <div class="space-y-1 text-center">
                    <svg class="mx-auto h-12 w-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7"></path></svg>
                    <div class="flex text-sm text-gray-600">
                    <label for="location" class="relative cursor-pointer rounded-md bg-white font-medium text-indigo-600 focus-within:outline-none focus-within:ring-2 focus-within:ring-indigo-500 focus-within:ring-offset-2 hover:text-indigo-500">
                        <input id="location" name="location" type="file" class="sr-only" />
                    </label>
                    </div>
                </div>
                </div>
            </div>

            <div class="col-span-6">
                <label for="numofattendees" class="event__lebel"> عدد الحضور</label>
                <input type="number" name="numofattendees" id="numofattendees" v-model="event.num_of_attendees" autocomplete="numofattendees" class="event__input" />
            </div>
            <div class="col-span-6 sm:col-span-3">
                <label for="startdate" class="event__lebel">بداية الحدث</label>
                <input type="text" name="startdate" id="startdate" autocomplete="startdate" v-model="event.start_date" class="event__input" />
            </div>

            <div class="col-span-6 sm:col-span-3">
                <label for="enddate" class="event__lebel">نهاية الحدث</label>
                <input type="text" name="enddate" id="enddate" autocomplete="enddate" v-model="event.end_date" class="event__input" />
            </div>
            </div>
        </div>
        <div class="bg-gray-50 px-4 py-3 text-right sm:px-6">
            <button type="submit" class="inline-flex justify-center rounded-md border border-transparent bg-indigo-600 py-2 px-4 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2">تعديل</button>
        </div>
        </div>
    </form>
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
            event: [],
            eventID: this.id,
            isOnline: false,
        }
    },
    created() {
        this.getEvent()
    },
    methods: {
        getEvent() {
            axios.post(`get-event-details/${this.id}/`)
            .then(response => {
                this.event = response.data.event
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