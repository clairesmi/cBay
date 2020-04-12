<template>
<div id="profile-edit">
  <h1>Edit your profile</h1>
  <div v-if="user" class="form-wrapper h-full w-2/4 flex">
    <form class="flex flex-col w-full justify-around p-40 text-gray-900">
      <label>Username: </label>
      <input type="text" placeholder="Username" v-model="user.username" required="required" disabled="disabled"/>
      <label>Email Address:</label>
      <input type="text" placeholder="email address" v-model="user.email" required="required"/>
      <label>Profile Picture:</label>
      <image-upload v-on:image-upload="user.profile_image = $event"></image-upload>
      <button class="form-button mt-2" @click.prevent="submitClicked">Submit</button>
    </form>
    </div>
</div>
</template>
<script>
import axios from 'axios'
import ImageUpload from '../items/ImageUpload.vue'

export default {
  name: 'profile-edit',
  components: { ImageUpload },
  data() {
    return {
      user: null
    }
  }, 
  mounted() {
    this.getUser()
  },
  methods: {
    async getUser() {
      try {
        const res = await axios.get('/api/profile')
        this.user = res.data
      } catch (err) {
        this.$router.push('/notfound')
      }
    },
    async submitClicked() {
      try {
        await axios.put('/api/profile', this.user)
        this.$router.push('/profile') 
      }
      catch {
        this.$router.push('/notfound')
      }
    }
  }
}
</script>
<style scoped>


</style>
