<template>
  <div id="profile-view" class="flex flex-col items-center h-full w-full bg-red-200">
      <h1 v-if="userListings" class="animated zoomInDown user-form-title text-6xl tracking-wide text-orange-600 mb-5 pb-10 bg-red-200">
        {{ userListings[0].owner.username }}'s listings</h1>
      <div v-if="userListings" class="profile-view-wrapper flex flex-wrap w-full h-auto justify-center items-center bg-red-200">
      <img v-if="userListings[0].owner.profile_image" :src=userListings[0].owner.profile_image alt="profile-image"/>
        <div v-for="listing in userListings" :key="listing.id" class="flex">
          <div v-if="listing.available" class="listings-body w-7/8 flex flex-col justify-center h-full m-3 p-4 bg-red-100 text-gray-800">
            <router-link :to="`/items/${listing.id}`"><img :src=listing.image /></router-link>
            <div class="listing-text flex flex-col justify-center itmes-center w-full pt-1">
            <p>{{ listing.name }}</p>
            <p>£{{ listing.price }}</p>
            <p>Size {{ listing.size }}</p>
            </div>
          </div>
          <!-- <h2>Customer Reviews</h2>
          <div v-for="review in userListings[0].owner.recommendations" :key="review.id">
          <div>{{ review }}</div>
          </div> -->
        </div>
      </div>
    </div>
</template>
<script>

import axios from "axios"

export default {
  name: "profile-view",
  data () {
    return {
      userListings: null
    }

  },
  mounted() {
    this.getUserProfile()
    // console.log(this.userListings)
  },

  methods: {
    async getUserProfile() {
      // console.log(this.$route.path)
      try {
        const res = await axios.get(`/api/${this.$route.path}/`)
        this.userListings = res.data
        // console.log(res.data[0].owner.profile_image.length)
        // console.log(this.userListings[0].owner.recommendations.map(rev => rev))
      }
      catch (err) {
        this.$router.push('/notfound')
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
.listing-text {
  font-family: 'Permanent Marker', cursive;
  font-size: 18px;
}
</style>