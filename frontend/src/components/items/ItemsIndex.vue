<template>
<div id="items-index">
  <router-link to="/">Home</router-link>
  <h1>Listings</h1>
  <div v-for="elem in items" :key="elem.id">
    <div v-if="elem.available">
    <h3>{{ elem.name }}</h3>
    <h4>${{ elem.price }}</h4>
    <router-link :to="`/items/${elem.id}/`"><img :src=elem.image alt="image-card" /></router-link>
    <div>{{ elem.available ? 'Available' : 'SOLD' }}</div>
    <!-- create boolean condition for availability and grey out if not available  - disable link if not
    available -->
    <div>Size: {{ elem.size }}</div>
    <h5>Categories:</h5>
    <div v-for="category in elem.categories" :key="category.id"> {{ category.name }}</div>
    </div>
    <div v-else class="unavailable-items-wrapper">
      <h3>{{ elem.name }}</h3>
      <h4>${{ elem.price }}</h4>
      <img :src=elem.image alt="image-card"/>
      <div>{{ elem.available ? 'Available' : 'SOLD' }}</div>
      <div>Size: {{ elem.size }}</div>
      <div v-for="category in elem.categories" :key="category.id"> {{ category.name }}</div>
    </div>
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
  async mounted () {
    await this.getItems()
  },

methods: {
  async getItems() {
    try {
      const res = await axios.get("/api/items")
      this.items = res.data.sort((a, b) => b.available - a.available)
    }
    catch (error) {
      this.$router.push('/notfound')
      }
    }
  },
}

</script>
<style scoped>
img {
  height: 400px;
  width: 400px;
}

.unavailable-items-wrapper {
  opacity: 0.5;
}

/* .unavailable-items-wrapper > img {
  opacity: 0.9;
} */
</style>