<template>
<div id="image-upload">
  <input id="files" type="file" placeholder="Upload Image" @change="handleUpload"/>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  name: "image-upload", 
  props: {
    image: String
  },

  mounted () {
    // this.getData()
  },

  methods: {
    // when there is a change event, we are setting the event target to the file list that is selected (files)
    // on event.target.files (an array of files)
    // so that we can pinpoint the file to be uploaded
    async handleUpload({ target: { files } }) {
      console.log(files)
      const body = new FormData
      body.append("file", files[0])
      body.append("upload_preset", 'qpedrr5c')
      console.log(files[0])
      const res = await axios.post('https://api.cloudinary.com/v1_1/dpmupgnig/image/upload', body)
      this.$emit("image-upload", res.data.secure_url)
    }
  }
}
</script>

<style scoped>

</style>