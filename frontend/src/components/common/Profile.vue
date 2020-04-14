<template>
<div id="profile" class="flex flex-col items-center w-full h-full bg-red-200">
  <h1 class="animated zoomInDown user-form-title text-6xl tracking-wide text-orange-600 mb-5">Profile Page</h1>
  <div v-if="user" class="profile-wrapper flex w-full h-full justify-center items-center bg-red-200">
    <div class="profile-name flex w-10/12 justify-center h-full p-5 bg-red-100 text-gray-800">
      <div class="flex flex-col w-1/3 items-center">
      <h1 class="username text-gray-800">Hello {{ user.username }}</h1>
      <p class="pb-2">Registered email: {{ user.email }}</p>
      <img v-if="user.profile_image" :src="user.profile_image">
      <router-link to="/profile/edit"><button class="form-button mt-5">Edit your profile</button></router-link>
      </div>
        <!-- <h2>Reviews from your customers</h2>
      <div v-for="review in user.recommendations" :key="review.id">
      </div> -->
      <div class="listings-wrapper flex flex-col w-1/3 items-center">
      <h2 class="pb-2">Your Listings</h2>
        <div v-for="listing in listings" :key="listing.id" class="flex flex-col items-center listing bg-white p-3 mb-3">
          <p>{{ listing.name }}</p>
          <router-link :to="`/items/${listing.id}`"><img :src=listing.image /></router-link>
          <p>£{{ listing.price }}</p>
          <p>Size: {{ listing.size }}</p>
          <p>{{ listing.available ? 'Available' : 'Sold' }}</p>
        </div>
      </div>
      <div class="purchased-items-wrapper flex flex-col w-1/3 h-full items-center">
        <h2 class="pb-2">Your Purchases</h2>
          <div v-for="purchase in purchasedItems" :key="purchase.id" class="flex flex-col items-center listing bg-white p-3 mb-3">
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
        this.$router.push('/notfound')
      }
    },
    async getListings() {
      try {
        const res = await axios.get('/api/listings', {
          headers: { Authorization: `Bearer ${Auth.getToken()}`}
        })
        this.listings = res.data
      }
      catch (err) {
        this.$router.push('/notfound')
      }
    },
    async getPurchasedItems() {
      try {
        const res = await axios.get('api/purchased')
        this.purchasedItems = res.data.filter(item => item.purchased === this.user.id)
      }
      catch (err) {
        this.$router.push('/notfound')
      }
    }
  }
  
}
</script>
<style scoped>
.username {
  font-family: 'Pacifico', cursive;
  font-size: 40px;
}
  img {
    height: 200px;
    width: 200px;
  }
  .profile-name {
    font-family: 'Oswald', sans-serif;
    font-size: 20px;
  }
  .listings-wrapper {
    overflow: scroll;
  }
  .listing {
    box-shadow: 1px 1px 10px 1px gray;
    font-family: 'Permanent Marker', cursive;
  }
  .purchased-items-wrapper {
    overflow: scroll;
  }
</style>