<template>
<div id="profile">
  <h1>Profile Page</h1>
  <div v-if="user" class="profile-wrapper">
    <div class="profile-name">
      <h1>Hello {{ user.username }}</h1>
      <p>Registered email: {{ user.email }}</p>
      <img :src="user.profile_image">
        <h2>Recommendations from your customers</h2>
      <div v-for="recommendation in user.recommendations" :key="recommendation.id">
      </div>
    </div>
    
  </div>
</div>
  
</template>
<script>

import axios from 'axios'
import Auth from '../../lib/auth'

export default {
  name: "profile",
  data () {
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
    const res = await axios.get('/api/profile', {
      headers: { Authorization: `Bearer ${Auth.getToken()}` }
    })
    this.user = res.data
    console.log(this.user)
      }
      catch (err) {
        console.log(err)
      }
    }
  }
  
}
</script>
<style scoped>

</style>