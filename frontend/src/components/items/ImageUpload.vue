<template>
<div id="image-upload">
  <input id="files" type="file" placeholder="Upload Image" @change="handleUpload"/>
  <div class="h-24">
  <img v-if="thumbnail" :src=this.thumbnail class="h-24 w-24" />
  <img v-if="loading" src="https://media.giphy.com/media/L05HgB2h6qICDs5Sms/giphy.gif" class="h-24 w-24 flex justify-center items-center" />
  </div>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  name: "image-upload", 
  props: {
    image: String
  },
  data() {
    return {
      thumbnail: '',
      loading: false
    }
  },

  mounted () {
    // this.getData()
  },

  methods: {
    // when there is a change event, we are setting the event target to the file list that is selected (files)
    // on event.target.files (an array of files)
    // so that we can pinpoint the file to be uploaded
    async handleUpload({ target: { files } }) {
      this.loading = true
      const body = new FormData
      body.append("file", files[0])
      body.append("upload_preset", 'qpedrr5c')
      console.log(files[0])
      const res = await axios.post('https://api.cloudinary.com/v1_1/dpmupgnig/image/upload', body)
      this.thumbnail = res.data.secure_url
      this.$emit("image-upload", res.data.secure_url)
      this.loading = false
    }
  }
}
</script>

<style scoped>

</style>