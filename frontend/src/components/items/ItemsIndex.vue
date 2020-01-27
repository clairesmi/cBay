<template>
<div id="items-index">

  <h1>Listings</h1>
  <div v-for="elem in items" :key="elem.id">
    <h3>{{ elem.name }}</h3>
    <h4>${{ elem.price }}</h4>
    <img :src=elem.image />
    <div>{{ elem.available ? 'Available' : 'No longer available' }}</div>
    <div>Size: {{ elem.size }}</div>
    <h5>Categories:</h5>
    <div v-for="category in elem.categories" :key="category.id"> {{ category.name }}</div>
    <h5>Other Items in this category:</h5>
    <div v-for="item in displayOthersInCategory" :key="item.id">{{ item }}</div>
    
  </div>
</div>
</template>

<script>
import 'style-loader'
export default {
  name: "items-index",
  props: {
    items: Array,
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