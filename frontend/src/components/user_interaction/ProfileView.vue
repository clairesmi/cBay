<template>
  <div id="profile-view">
    <h1>Profile View Page</h1>
    <div v-if="user" class="profile-view-wrapper">
      <div class="listings-header">
        <h1>{{ user.username }}'s listings</h1>
      </div>
      <div class="listings-body">
        <img :src=user.profile_image alt="profile-image"/>
        <div v-for="listing in user.listings" :key="listing.id">
        <p>{{ listing.listed_item.name }}</p>
        <router-link :to="`/items/${listing.listed_item.id}`"><img :src=listing.listed_item.image /></router-link>
        <p>£{{ listing.listed_item.price }}</p>
        <p>Size {{ listing.size }}</p>
        </div>
        <div v-for="review in user.recommendations" :key="review.id">

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
      user: null
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
        this.user = res.data
        console.log(this.user)
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