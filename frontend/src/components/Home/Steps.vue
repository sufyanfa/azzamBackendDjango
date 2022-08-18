<template>
<div class="w-full mx-auto flex items-center select-none mb-6">
  <div class="relative" :class="statusStep.step1 ?' text-secondary' :'text-gray-600'">
    <div>
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"></path></svg>
    </div>
    <div class="absolute block text-sm">طريقة الإرسال</div>
  </div>
hi {{statusStep.step1}}
  <div class="w-full h-1 rounded mx-px" :class="currentStep !== 0 ?' bg-secondary' :'bg-gray-600'"></div>

  <div class="relative" :class="currentStep !== 1 && currentStep !==0 ?' text-secondary' :'text-gray-600'">
    <div>
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
    </div>
    <div class="absolute text-sm">بيانات الحدث</div>
  </div>

  <div class="w-full h-1 rounded mx-px" :class="currentStep !== 1 ?' bg-secondary' :'bg-gray-600'"></div>

  <div class="relative">
    <div class="text-gay-500">&#9675;</div>
    <div class="absolute text-sm text-gray-500">جهات الإتصال</div>
  </div>
  <div class="w-full bg-gray-400 h-1 rounded mx-px"></div>

  <div class="relative">
    <div class="text-gray-500">&#9675;</div>
    <div class="absolute text-sm text-gray-500">إرسال</div>
  </div>
</div>
</template>
<script>
export default {
  props: {
    currentStep: {
      type: Number,
      default: 0
    },
    statusStep:{
      type: Object
    }
  }
}
</script>