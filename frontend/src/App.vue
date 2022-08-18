<template>
  <router-view/>
</template>
<script>
export default {
  name: 'App',
  mounted() {
    document.title = 'عزام إدارة الأحداث'
  }
}
</script>