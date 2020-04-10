<template>
<div id="items-index" class="flex flex-col justify-center items-center font-sans bg-red-200">
  <h1 class="animated zoomInDown listings-title tracking-wide text-orange-600">All Listings</h1>
  <form class=" flex justify-center w-full text-gray-800">
  <input class="listings-search mt-5 w-1/3"
  placeholder=" search by keyword"
  v-model="searchTerm"
  />
  <!-- <button class="mt-10 ml-5 text-orange-600">Search</button> -->
  </form>
  <div class="flex flex-row flex-wrap justify-around p-5">
    <div v-for="elem in listingSearch()" :key="elem.id" class=" item-card flex p-5 bg-white mb-5">
      <div v-if="elem.available" class="flex flex-col flex-wrap">
      <router-link :to="{ name: 'item-show', params: { id: elem.id } }"><img :src=elem.image alt="image-card" /></router-link>
      <!-- <div>{{ elem.available ? 'Available' : 'SOLD' }}</div> -->
      <div class="flex flex-row justify-around pt-8">
        <h3>{{ elem.name }}</h3> 
        <div>Size: {{ elem.size }}</div> 
        <h3>${{ elem.price.toFixed(2) }}</h3>
      </div>
      </div>
      <div v-else class="unavailable-items-wrapper item-card flex flex-col flex-wrap">
        <img :src=elem.image alt="image-card"/>
        <div class="flex flex-row justify-around pt-8">
        <h3>{{ elem.name }}</h3>
        <div>Size: {{ elem.size }}</div>
        <h4>${{ elem.price.toFixed(2) }}</h4>
        <div>{{ elem.available ? 'Available' : '*SOLD*' }}</div>
        </div>
        <!-- <div v-for="category in elem.categories" :key="category.id"> {{ category.name }}</div> -->
      </div>
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
   items: [],
   searchTerm: '',
   filteredItems: []
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
    },
    listingSearch() {
      const { items, searchTerm } = this
      const re = new RegExp(searchTerm, 'i')
      return items.filter(item => {
        return re.test(item.name)}).sort((a, b) => b.available - a.available)
    }
  },
}

</script>
<style scoped>
img {
  height: 380px;
  width: 380px;
}

.listings-title {
  font-family: 'Pacifico', cursive;
  font-size: 80px;
}
form {
  font-family: 'Oswald', sans-serif;
  font-size: 22px;
  letter-spacing: 0.5px;
}
button {
  text-decoration: underline;
}
.item-card {
  height: 490px;
  font-family: 'Permanent Marker', cursive;
  font-size: 20px;
}

.unavailable-items-wrapper {
  opacity: 0.5;
}


/* .unavailable-items-wrapper > img {
  opacity: 0.9;
} */
</style>