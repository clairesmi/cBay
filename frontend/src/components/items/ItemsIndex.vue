<template>
<div id="items-index">
  <router-link to="/">Home</router-link>
  <h1>Listings</h1>
  <div v-for="elem in items" :key="elem.id">
    <h3>{{ elem.name }}</h3>
    <h4>${{ elem.price }}</h4>
    <img :src=elem.image />
    <div>{{ elem.available ? 'Available' : 'No longer available' }}</div>
    <div>Size: {{ elem.size }}</div>
    <h5>Categories:</h5>
    <div v-for="category in elem.categories" :key="category.id"> {{ category.name }}</div>
    <!-- <h5>Other Items in this category:</h5> -->
    <!-- <div v-for="item in displayOthersInCategory" :key="item.id">{{ item }}</div> -->
    
  </div>
</div>
</template>

<script>
import 'style-loader'
import axios from 'axios'

export default {
  name: "items-index",
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
      console.log('items index')
    }

    catch (error) {
      console.log(error)
    }
  }
},


computed: {
  displayOthersInCategory() {
    console.log(this.items.map(elem => elem.categories.map(item => item)))
    return this.items.map(elem => elem.categories.map(cat => cat.items.map(el => el.name)))
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