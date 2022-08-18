<template>
  
  <Steps :currentStep="currentStep" />
  <div>
    <Form
      @submit="nextStep"
      :validation-schema="currentSchema"
      v-slot="{ handleSubmit }"
    >
      <transition name="fade" mode="out-in">
        <component :is="components[currentStep]" :statusStep="statusStep" />
      </transition>
      
      <div class="flex items-center w-full my-4" :class="currentStep ==0 ?'justify-end':'justify-between'">
    
        <div v-if="currentStep == 3" class="flex justify-center mx-auto py-16">
          <div class="flex w-64 items-center rounded-lg shadow-lg mb-4 bg-secondary p-4 text-white"> 
            <div class="w-64">
              <h4 class="mb-2 font-bold">تمت إضافة الحدث</h4>
                <p>العودة إلى 
                  <router-link :to="{name:'Events'}" class="text-primary font-bold">الرئيسية</router-link>
                </p>  
            </div> 
            <div class="w-12">
              <div class="text-2xl p-2 bg-secondary rounded-full">    
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"></path></svg>
              </div>
            </div>
          </div>
        </div>

        <button v-if="currentStep !== 0&&currentStep !== 3" class="button__secondary" type="button" @click="prevStep">
          السابق
        </button>
        <button v-if="currentStep !== 3" class="button__secondary" type="submit">
          التالي
        </button>
    
      </div>
      </Form>
  </div>
          
</template>

<script>
import { Form } from "vee-validate";
import * as yup from "yup";
import { ref, reactive, computed } from "vue";
import SelectMethod from "../../components/Home/SelectMethod.vue";
import AddData from "../../components/Home/AddData.vue";
import AddContacts from "../../components/Home/AddContacts.vue";
import axios from 'axios'
import Steps from '../../components/Home/Steps.vue';

const components = [SelectMethod,AddData,AddContacts];
export default {
  name: "EventCreate",
  components: {Form,Steps},
  setup: () => {
    const currentStep = ref(0);
    const formValues = reactive({});
    const statusStep = reactive({
      step1: false,
      step2: false,
      step3: false,
      step4: false,
    });
    const schemas = [
      yup.object({
        socail: yup.string(),
      }),
      yup.object({ 
        name: yup.string().required().typeError("الرجاء ادخال اسم الحدث"),
        description : yup.string().typeError("الرجاء ادخال وصف الحدث"),
        eventID : yup.number().nullable(true),
        organizetion : yup.string(),
        is_online : yup.boolean(),
        is_certified : yup.boolean(),
        city : yup.string(),
        address : yup.string(),
        num_of_attendees : yup.number().integer(),
        start_date : yup.date(),
        end_date : yup.date(),
      }),
      yup.object({
        file :yup.mixed().required("A file is required"),
        // atten : yup.array(),
      })
    ];

    const currentSchema = computed(() => {
      return schemas[currentStep.value];
    });

    switch (currentStep.value) {
      case 0:
        statusStep.step1 = true;
        break;
      case 1:
        statusStep.step2 = true;
        break;
      case 2:
        statusStep.step3 = true;
        break;
      case 3:
        statusStep.step4 = true;
        break;
    }

    function nextStep(values) {
      Object.assign(formValues, values);
      if(currentStep.value === 1){
        axios.post('/create-event/', formValues, 
          ).then(response => {
            Object.assign(formValues, {eventID : response.data.id});
          }).catch(error => {
          }
        )
      }
      if(currentStep.value === 2){
        if(formValues.eventID !== 0){
          const data = {
            file : formValues.file, 
            event_id: formValues.eventID,
          }
          axios.post('/add-attendences/', data,{
            headers: {
              'Content-Type': 'multipart/form-data'
            }})
            .then(response => {
            })
            .catch(error => {
            })
        }
      }
      currentStep.value++;
    }

    function prevStep() {
      if (currentStep.value <= 0) {
        return;
      }

      currentStep.value--;
    }

    return {
      currentStep,
      currentSchema,
      prevStep,
      formValues,
      nextStep,
      components,
      statusStep
    }
  }
}
</script>
