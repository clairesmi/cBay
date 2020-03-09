<template>
<div id="profile">
  <h1>Profile Page</h1>
  <div v-if="user" class="profile-wrapper">
    <div class="profile-name">
      <h1>Hello {{ user.username }}</h1>
      <p>Registered email: {{ user.email }}</p>
      <img :src="user.profile_image">
        <h2>Reviews from your customers</h2>
      <div v-for="review in user.recommendations" :key="review.id">
      </div>
      <h2>Your Listings</h2>
      <div v-for="listing in listings" :key="listing.id">
        <p>{{ listing.name }}</p>
        <router-link :to="`/items/${listing.id}`"><img :src=listing.image /></router-link>
        <p>£{{ listing.price }}</p>
        <p>Size: {{ listing.size }}</p>
        <p>{{ listing.available ? 'Available' : 'Sold' }}</p>
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
    user: null,
    listings: []
    }
  },

  mounted() {
    this.getUser()
    this.getListings()
  },

  methods: {
    async getUser() {
      try {
    const res = await axios.get('/api/profile', {
      headers: { Authorization: `Bearer ${Auth.getToken()}` }
    })
    this.user = res.data
    // console.log(this.user)
      }
      catch (err) {
        console.log(err)
      }
    },
    async getListings() {
      try {
        const res = await axios.get('/api/listings', {
          headers: { Authorization: `Bearer ${Auth.getToken()}`}
        })
        this.listings = res.data
        console.log(this.listings)
      }
      catch (err) {
        console.log(err)
      }
    }
  }
  
}
</script>
<style scoped>
  img {
    height: 200px;
    width: 200px;
  }
</style>