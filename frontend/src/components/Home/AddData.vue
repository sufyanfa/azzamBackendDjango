<template>
<div class="mt-5 md:col-span-2 md:mt-0 py-16">
  <div class="overflow-hidden shadow sm:rounded-md">
    <div class="bg-white px-4 py-5 sm:p-6">
        <p class="font-bold py-4">بيانات الحدث</p>
        <div class="grid grid-cols-6 gap-6">
            <div class="col-span-6 sm:col-span-3">
            <label for="name" class="event__lebel">اسم الحدث</label>
            <Field type="text" name="name" id="name" autocomplete="name" v-model="name" class="event__input" />
            <ErrorMessage name="name" />
            <Field type="number" name="eventID" hidden v-model="eventID" />
            <ErrorMessage name="eventID" />
            </div>

            <div class="col-span-6 sm:col-span-3">
            <label for="organizetion" class="event__lebel">اسم الجهة</label>
            <Field type="text" name="organizetion" id="organizetion" autocomplete="organizetion" v-model="organizetion" class="event__input" />
            <ErrorMessage name="organizetion" />
            </div>

            <div class="col-span-6">
            <label for="description" class="event__lebel">وصف الحدث</label>
            <Field as="textarea" id="description" name="description" v-model="description" rows="3" class="mt-1 block w-full rounded-md border border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" />
            <ErrorMessage name="description" />
            </div>

            <div class="col-span-6">
            <label class="event__lebel"> صورة الحدث </label>
            <div class="mt-1 flex justify-center rounded-md border-2 border-dashed border-gray-300 px-6 pt-5 pb-6">
            <div class="space-y-1 text-center">
                <svg class="mx-auto h-12 w-12 text-gray-400" stroke="currentColor" fill="none" viewBox="0 0 48 48" aria-hidden="true">
                <path d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                </svg>
                <div class="flex text-sm text-gray-600">
                <label for="image" class="relative cursor-pointer rounded-md bg-white font-medium text-indigo-600 focus-within:outline-none focus-within:ring-2 focus-within:ring-indigo-500 focus-within:ring-offset-2 hover:text-indigo-500">
                    <span>Upload a file</span>
                    <input id="image" name="image" type="file" class="sr-only" />
                    <ErrorMessage name="image" />
                </label>
                <p class="pl-1">or drag and drop</p>
                </div>
                <p class="text-xs text-gray-500">PNG, JPG, GIF up to 10MB</p>
            </div>
            </div>
            <ErrorMessage name="description" />
            </div>

            <div class="col-span-6 sm:col-span-3">
                <div class="flex items-start">
                <div class="flex items-center h-5">
                <Field id="is_online" name="is_online" v-on:click="isOnline = !isOnline" type="checkbox" class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300 rounded" />
                </div>
                <div class="mr-3 text-sm">
                <label for="is_online" class="event_lebel">الحدث أونلاين</label>
                </div>
                <ErrorMessage name="is_online" />
                </div>
            </div>

            <div class="col-span-6 sm:col-span-3">
            <div class="flex items-start">
                <div class="flex items-center h-5">
                    <Field id="is_certified" name="is_certified" type="checkbox" class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300 rounded" />
                </div>
                <div class="mr-3 text-sm">
                    <label for="is_certified" class="event_lebel">يوجد شهادات</label>
                </div>
                <ErrorMessage name="is_certified" />
            </div>
            </div>

            <div class="col-span-6 sm:col-span-3" v-show="isOnline">
            <label for="city" class="event__lebel"> مدينة الحدث</label>
            <Field type="text" name="city" id="city" autocomplete="city" class="event__input" />
            <ErrorMessage name="city" />
            </div>

            <div class="col-span-6 sm:col-span-3" v-show="isOnline">
            <label for="address" class="event__lebel">عنوان الحدث</label>
            <Field type="text" name="address" id="address" autocomplete="address" class="event__input" />
            <ErrorMessage name="address" />
            </div>

            <div class="col-span-6" v-show="isOnline">
                <label class="event__lebel"> موقع الحدث </label>
                <div class="mt-1 flex justify-center rounded-md border-2 border-dashed border-gray-300 px-6 pt-5 pb-6">
                    <div class="space-y-1 text-center">
                        <svg class="mx-auto h-12 w-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7"></path></svg>
                        <div class="flex text-sm text-gray-600">
                            <label for="location" class="relative cursor-pointer rounded-md bg-white font-medium text-indigo-600 focus-within:outline-none focus-within:ring-2 focus-within:ring-indigo-500 focus-within:ring-offset-2 hover:text-indigo-500" />
                            <Field id="location" name="location" type="file" class="sr-only" />
                            <ErrorMessage name="location" />
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-span-6">
                <label for="num_of_attendees" class="event__lebel"> عدد الحضور</label>
                <Field type="number" name="num_of_attendees" id="num_of_attendees" autocomplete="num_of_attendees" class="event__input" />
                <ErrorMessage name="num_of_attendees" />
            </div>

            <div class="col-span-6 sm:col-span-3">
                <label for="start_date" class="event__lebel">بداية الحدث</label>
                <Field type="datetime-local" name="start_date" id="start_date" autocomplete="start_date" class="event__input" />
                <ErrorMessage name="start_date" />
            </div>

            <div class="col-span-6 sm:col-span-3">
                <label for="end_date" class="event__lebel">نهاية الحدث</label>
                <Field type="datetime-local" name="end_date" id="end_date" autocomplete="end_date" class="event__input" />
                <ErrorMessage name="end_date" />
            </div>
        </div>
    </div>
  </div>
</div>
</template>

<script>
import { Field, ErrorMessage } from "vee-validate";
import { reactive, toRefs } from "vue";

export default {
    data(){
        return{
            isOnline: true,
        }
    },
    components: {Field,ErrorMessage},
    setup() {
        const state = reactive({
            name : '',
            description : '',
            organizetion : '',
            eventID : 0,
            is_online : false,
            is_certified : false,
            city : '',
            address : '',
            num_of_attendees : '',
            start_date : '',
            end_date : '',
        }
    )

    return {
      ...toRefs(state),
    }
  }
}
</script>