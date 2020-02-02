<template>
<div id="items-index">
  <router-link to="/">Home</router-link>
  <h1>Listings</h1>
  <div v-for="elem in items" :key="elem.id">
    <h3>{{ elem.name }}</h3>
    <h4>${{ elem.price }}</h4>
    <router-link :to="`/items/${elem.id}/`"><img :src=elem.image /></router-link>
    <div>{{ elem.available ? 'Available' : 'No longer available' }}</div>
    <!-- create boolean condition for availability and grey out if not available  - disable link if not
    available -->
    <div>Size: {{ elem.size }}</div>
    <h5>Categories:</h5>
    <div v-for="category in elem.categories" :key="category.id"> {{ category.name }}</div>
    
  </div>
</div>
</template>

<script>
import 'style-loader'
import axios from 'axios'

import ItemShow from './ItemShow.vue'

export default {
  name: "items-index",
   components: {
    ItemShow
  },
 data () {
  return {
   items: []
   }
 }, 
  mounted () {
    this.getItems()
  },

methods: {
  async getItems () {
    try {
      const response = await axios.get("/api/items")
      this.items = response.data
      // console.log('items index')
    }

    catch (error) {
      console.log(error)
      }
    }
  }
}

</script>
<style scoped>
img {
  height: 400px;
  width: 400px;
}
</style>