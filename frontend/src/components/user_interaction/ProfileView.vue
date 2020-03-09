<template>
  <div id="profile-view">
    <h1>Profile View Page</h1>
    <div v-if="userListings" class="profile-view-wrapper">
      <div class="listings-header">
        <h1>{{ userListings[0].owner.username }}'s listings</h1>
      </div>
      <div class="listings-body">
        <img :src=userListings[0].owner.profile_image alt="profile-image"/>
        <div v-for="listing in userListings" :key="listing.id">
        <p>{{ listing.name }}</p>
        <router-link :to="`/items/${listing.id}`"><img :src=listing.image /></router-link>
        <p>£{{ listing.price }}</p>
        <p>Size {{ listing.size }}</p>
        </div>
          <h2>Customer Reviews</h2>
        <div v-for="review in userListings[0].owner.recommendations" :key="review.id">
          <div>{{ review }}</div>
          </div>
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
  },

  methods: {
    async getUserProfile() {
      // console.log(this.$route.path)
      try {
        const res = await axios.get(`/api/${this.$route.path}/`)
        this.userListings = res.data
        console.log(this.userListings[0].owner.recommendations.map(rev => rev))
      }
      catch (err) {
        console.log(err)
      }
      // console.log(this.user)
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