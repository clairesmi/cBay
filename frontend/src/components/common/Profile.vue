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
      <div class="listings-wrapper">
      <h2>Your Listings</h2>
        <div v-for="listing in listings" :key="listing.id">
          <p>{{ listing.name }}</p>
          <router-link :to="`/items/${listing.id}`"><img :src=listing.image /></router-link>
          <p>£{{ listing.price }}</p>
          <p>Size: {{ listing.size }}</p>
          <p>{{ listing.available ? 'Available' : 'Sold' }}</p>
        </div>
      </div>
      <div class="purchased-items-wrapper">
        <h2>Your Purchases</h2>
          <div v-for="purchase in purchasedItems" :key="purchase.id">
            <p>{{ purchase.name }}</p>
            <img :src=purchase.image />
            <p>£{{ purchase.price }}</p>
            <p>Size: {{ purchase.size }}</p>
            <router-link :to="`/profile/${purchase.owner.id}/`"><p>Sold by: {{ purchase.owner.username }}</p></router-link>
          </div>
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
    listings: [],
    purchasedItems: []
    }
  },

  async mounted() {
    await this.getUser()
    this.getListings()
    this.getPurchasedItems()
  },

  methods: {
    async getUser() {
      try {
    const res = await axios.get('/api/profile', {
      headers: { Authorization: `Bearer ${Auth.getToken()}` }
    })
    this.user = res.data
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
    },
    async getPurchasedItems() {
      try {
        const res = await axios.get('api/purchased')
        this.purchasedItems = res.data
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