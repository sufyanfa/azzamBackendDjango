<template>
    <div>
    EventID {{ eventID}} with UserID {{ userID }}

  </div>
</template>
<script>
    export default {
        name: 'Verification',
        data() {
            return {
                eventID: '',
                userID : ''
            }
        },
        created(){
            this.eventID = this.$route.params.eventid;
            this.userID = this.$route.params.userid;
        }
    }
</script>