<template>
    <HeaderApp />
    <div class="form">
        <Form @submit="signUp" :validation-schema="schema" class="form__content">
          <p class="text-lg font-bold">تسجيل جديد | نظام عزام</p>
          <div v-if="success" class="bg-green-100 rounded-lg py-5 px-6 mb-3 text-base text-green-700 inline-flex items-center w-full" role="alert">
            <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="check-circle" class="w-4 h-4 ml-2 fill-current" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
              <path fill="currentColor" d="M504 256c0 136.967-111.033 248-248 248S8 392.967 8 256 119.033 8 256 8s248 111.033 248 248zM227.314 387.314l184-184c6.248-6.248 6.248-16.379 0-22.627l-22.627-22.627c-6.248-6.249-16.379-6.249-22.628 0L216 308.118l-70.059-70.059c-6.248-6.248-16.379-6.248-22.628 0l-22.627 22.627c-6.248 6.248-6.248 16.379 0 22.627l104 104c6.249 6.249 16.379 6.249 22.628.001z"></path>
            </svg>
            تم إنشاء الحساب - 
            <router-link :to="{name: 'LogIn'}"  class="font-bold">صفحة الدخول</router-link>
          </div>
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
                <input type="Submit" class="form__submit" :value="processing ? 'الرجاء الإنتظار' : 'تسجيل'">
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

export default {
    name: 'SignUp',
    components: {HeaderApp,Field,Form,ErrorMessage},
    setup() {
      const message = ref('');
      const processing = ref(false);
      const success = ref(false);
      const schema = Yup.object().shape({
        username: Yup.string().email("صيغة البريد غير صحيحة").required("يرجى كتابة الإيميل").label("البريد الإلكتروني"),
        password: Yup.string().min(8, "يرجى كتابة كلمة مرور لاتقل عن 8 أرقام وأحرف").required("يرجى كتابة كلمة مرور").label("كلمة المرور"),
      });

      function signUp(values) {
        processing.value = true;
        axios.post('/register/', values)
          .then(response => {
            success.value = true;
            processing.value = false;
            message.value = '';
          })
          .catch(error => {
            message.value = 'البريد الإلكتروني مستخدم من قبل';
            processing.value = false;
            success.value = false;
          });
      }

      return {
        schema,
        signUp,
        message,
        processing,
        success
      };
    },
}
</script>
<style>
:root {
  /*========== Colors ==========*/
  /* Color mode RGB */
  --first-color: #abfa00;
  --white-color: #fff;
  --black-color: #000;

  /*========== Font and typography ==========*/
  /*.5rem = 8px | 1rem = 16px ...*/
  --normal-font-size: .938rem;
  --tiny-font-size: .563rem;
}

.form {
  height: 80vh;
  display: grid;
  place-items: center;
  margin: 0 1.5rem;
}

.form__content {
  display: grid;
  row-gap: 1.5rem;
}

.form__input, 
.form__label, 
.form__submit {
  border: 0;
  outline: none;
  font-size: var(--normal-font-size);
}

.form__box {
  width: 312px;
  height: 59px;
  position: relative;
}

.form__shadow {
  position: absolute;
  width: 100%;
  height: 100%;
  background-color: var(--black-color);
}

.form__input {
  position: absolute;
  border: 2.5px solid var(--black-color);
  background-color: var(--white-color);
  width: 100%;
  height: 100%;
  z-index: 10;
  padding: 18px;
  transition: transform .3s;
}

.form__input::placeholder {
  transition: opacity .5s;
}

.form__label {
  z-index: 100;
  position: absolute;
  top: 16px;
  right: 20px;
  font-size: var(--tiny-font-size);
  font-weight: 600;
  transition: .2s;
  pointer-events: none;
  opacity: 0;
}

.form__button {
  justify-self: flex-start;
  background-color: var(--black-color);
}

.form__submit {
  padding: .875rem 1.5rem;
  color: var(--black-color);
  background-color: var(--first-color);
  cursor: pointer;
  transition: transform .3s;
}

.form__submit:hover {
  transform: translate(-6px, -6px);
}

/* Opaque placeholder */
.form__input:focus::placeholder {
  opacity: 0;
  transition: .3s;
}

/* Move input and sticky input up */
.form__input:focus, 
.form__input:not(:placeholder-shown).form__input:not(:focus) {
  transform: translate(-8px, -8px);
  padding: 28px 18px 18px;
  animation: input-animation .5s;
}

/* Move label and sticky label up */
.form__input:focus + .form__label,
.form__input:not(:placeholder-shown).form__input:not(:focus) + .form__label {
  opacity: 1;
  top: 2px;
  left: 12px;
  transition: .3s;
}

/* Input bounce animation */
@keyframes input-animation {
  0% {
    transform: translate(0);
  }
  40% {
    transform: translate(-9px, -9px);
  }
  60% {
    transform: translate(-7px, -7px);
  }
}

/*=============== BREAKPOINTS ===============*/
/* For small devices */
@media screen and (max-width: 340px) {
  .form__content, 
  .form__box {
    width: 100%;
  }
}

/* For large devices */
@media screen and (min-width: 968px) {
  .form__content {
    zoom: 1.1;
  }
}
</style>