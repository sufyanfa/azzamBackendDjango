<template>
<div class="w-full px-4 max-w-xl mx-auto mt-20">
    <div>
        <h2 class="mt-6 text-3xl font-extrabold text-neutral-600 text-center">إضافة البيانات الشخصية</h2>
    </div>

    <div class="mt-8">
        <div class="mt-6">
            <form @submit.prevent="personalInfo" class="space-y-6">
                <div>
                    <label for="organizetion" class="block text-sm font-medium text-neutral-600"> أسم الجهة </label>
                    <div class="mt-1">
                        <input v-model="info.name" id="organizetion" name="organizetion" type="text" autocomplete="organizetion" required="" placeholder="أسم الشركة , المؤسسة, النادي" class="block w-full px-5 py-3 text-base placeholder-gray-300 transition duration-500 ease-in-out transform border border-transparent rounded-lg text-neutral-600 bg-gray-50 focus:outline-none focus:border-transparent focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-300">
                    </div>
                </div>

                <div class="space-y-1">
                    <label for="phone" class="block text-sm font-medium text-neutral-600"> رقم الجوال </label>
                    <div class="mt-1">
                        <input v-model="info.phone" id="phone" name="phone" type="tel" autocomplete="current-password" required="" placeholder="رقم الجوال للجهة" class="block w-full px-5 py-3 text-base placeholder-gray-300 transition duration-500 ease-in-out transform border border-transparent rounded-lg text-neutral-600 bg-gray-50 focus:outline-none focus:border-transparent focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-300">
                    </div>
                </div>


                <div>
                    <button type="submit" class="flex items-center justify-center w-full px-10 py-4 text-base font-medium text-center text-white transition duration-500 ease-in-out transform bg-blue-600 rounded-xl hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">حفظ</button>
                </div>
            </form>
        </div>
    </div>
</div> 
</template>
<script>
import Aside from '../../components/Home/Aside.vue'
import Navbar from '../../components/Home/Navbar.vue'
import axios from 'axios'
import { update } from 'lodash'
export default {
    components: {
        Aside,
        Navbar
    },
    data() {
        return {
            info: {
                name: '',
                phone: ''
            }
        }
    },
    methods: {
        personalInfo() {
            axios.post('/user_update/', this.info)
            .then(response => {
                console.log(response)
            })
            .catch(error => {
                console.log(error)
            })
        }
    }
}
</script>