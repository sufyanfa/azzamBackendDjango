<template>
    <HeaderApp />
    <div class="form">
        <Form @submit="logIn" :validation-schema="schema" class="form__content">
          <h1 class="text-lg font-bold">دخول | نظام عزام</h1>
            <div class="form__box">
                <Field name="username" type="email" class="form__input focus:outline-none focus:border-black focus:ring-black" placeholder="البريد" />
                <label for="username" class="form__label">ادخل البريد</label>
                <div class="form__shadow"></div>
            </div>
            <ErrorMessage name="username" class="bg-red-100 rounded-md py-3 px-2 mb-3 text-base text-red-700 inline-flex items-center w-full" />


            <div class="form__box">
                <Field name="password" type="password" class="form__input focus:outline-none focus:border-black focus:ring-black" placeholder="كلمة المرور" />
                <label for="password" class="form__label">ادخل كلمة المرور</label>
                <div class="form__shadow"></div>
            </div>
            <ErrorMessage name="password"  class="bg-red-100 rounded-md py-3 px-2 mb-3 text-base text-red-700 inline-flex items-center w-full" />


            <div v-if="message" class="bg-red-100 rounded-md py-3 px-2 mb-3 text-base text-red-700 inline-flex items-center w-full" role="alert">
                <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="times-circle" class="w-4 h-4 ml-2 fill-current" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                    <path fill="currentColor" d="M256 8C119 8 8 119 8 256s111 248 248 248 248-111 248-248S393 8 256 8zm121.6 313.1c4.7 4.7 4.7 12.3 0 17L338 377.6c-4.7 4.7-12.3 4.7-17 0L256 312l-65.1 65.6c-4.7 4.7-12.3 4.7-17 0L134.4 338c-4.7-4.7-4.7-12.3 0-17l65.6-65-65.6-65.1c-4.7-4.7-4.7-12.3 0-17l39.6-39.6c4.7-4.7 12.3-4.7 17 0l65 65.7 65.1-65.6c4.7-4.7 12.3-4.7 17 0l39.6 39.6c4.7 4.7 4.7 12.3 0 17L312 256l65.6 65.1z"></path>
                </svg>
                <div>
                <p>{{ message }}</p>

                </div>
            </div>

  
            <div class="form__button">
                <input :disabled="processing" type="Submit" class="form__submit" :value="processing ? 'الرجاء الإنتظار' : 'دخول'">
            </div>
        </Form>
    </div>
</template>
<script>
import {ref } from 'vue'

import { Field, Form, ErrorMessage } from "vee-validate";
import * as Yup from "yup";

import HeaderApp from '../components/HeaderApp.vue'
import axios from 'axios'
import { useStore } from 'vuex'

export default {
    name: 'LogIn',
    components: {HeaderApp , Field, Form, ErrorMessage},
    setup() {
      const store =  useStore()
      const message = ref('')
      const processing = ref(false);
      const schema = Yup.object().shape({
        username: Yup.string().email("صيغة البريد غير صحيحة").required("يرجى كتابة الإيميل").label("البريد الإلكتروني"),
        password: Yup.string().min(8, "يرجى كتابة كلمة مرور لاتقل عن 8 أرقام وأحرف").required("يرجى كتابة كلمة مرور").label("كلمة المرور"),
      });

      function logIn(values) {
        processing.value = true;
        axios.post('/login/', values)
          .then(response => {
            store.dispatch('auth/login', response.data)
            processing.value = false
          })
          .catch(error => {
            processing.value = false
            message.value = 'يرجى التحقق من اسم المستخدم أو كلمة المرور الخاصة بك'
          });
      }

      return {
        schema,
        logIn,
        processing,
        message
      };
    },
}
</script>