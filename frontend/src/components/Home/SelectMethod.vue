<template>
  <div class="w-full px-4 py-16">
    <div class="mx-auto w-full max-w-md">
      <p class="font-bold py-4">إختر وسيلة التواصل</p>
      <RadioGroup v-model="selected">
        <RadioGroupLabel for="socail" class="sr-only">وسيلة الإرسال</RadioGroupLabel>
        <div class="space-y-2">
          <RadioGroupOption
            as="template"
            v-for="method in methods"
            :key="method.name"
            :value="method"
            v-slot="{ active, checked }"
            :disabled="method.avalible != 'متاح'"
          >
            <div
              :class="[
                active
                  ? 'ring-2 ring-white ring-opacity-60 ring-offset-2 ring-offset-primary'
                  : '',
                checked ? 'bg-primary bg-opacity-75 text-white ' : 'bg-white ',
              ]"
              class="relative flex cursor-pointer rounded-lg px-5 py-4 shadow-md focus:outline-none"
            >
              <div class="flex w-full items-center justify-between">
                <div class="flex items-center">
                  <div class="text-sm">
                    <RadioGroupLabel
                      as="p" name="socail"
                      :class="checked ? 'text-black' : 'text-gray-900'"
                      class="font-medium"
                    >
                      {{ method.name }} <span v-show="method.avalible != 'متاح' " :class="checked ? 'text-secondary' : ' text-black'"> {{ method.avalible }}</span>
                    </RadioGroupLabel>
                  </div>
                </div>
                <div v-show="checked" class="shrink-0 text-black">
                  <svg class="h-6 w-6" viewBox="0 0 24 24" fill="none">
                    <circle
                      cx="12"
                      cy="12"
                      r="12"
                      fill="#000"
                      fill-opacity="1"
                    />
                    <path
                      d="M7 13l3 3 7-7"
                      stroke="#fff"
                      stroke-width="1.5"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                    />
                  </svg>
                </div>
              </div>
            </div>
          </RadioGroupOption>
        </div>
      </RadioGroup>
      <ErrorMessage name="socail" />
    </div>
  </div>
</template>

<script>
import { Field, ErrorMessage } from "vee-validate";
import { reactive, toRefs } from "vue";
import { ref } from 'vue'
import {
  RadioGroup,
  RadioGroupLabel,
  RadioGroupDescription,
  RadioGroupOption,
} from '@headlessui/vue'
export default { 
  data() {
    return {
      selected: '',
      methods: [
        {
          name: 'البريد الإلكتروني',
          value: 'email',
          avalible: 'متاح',
        },
        {
          name: 'الرسائل النصية',
          value: 'sms',
          avalible:'(قريباً)',
        },
        {
          name: 'الواتساب',
          value: 'whatsapp',
          avalible:'(قريباً)',
        },
      ],
    };
  }, 
  components: {
    RadioGroup,
    RadioGroupLabel,
    RadioGroupDescription,
    RadioGroupOption,
    Field,
    ErrorMessage,
  },
  setup() {
    const state = reactive({
      socail : '',
    })
    return {
      ...toRefs(state),
    }
  }
}
</script>
