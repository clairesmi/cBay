<template>
  <div id="item-form">
    <router-link to="/">Home</router-link>
    <form>
      <label>Name</label>
      <input type="text" placeholder="Product name" v-model="item.name"/>
      <label>Price</label>
      <input type="number" placeholder="0.00" step="0.01" v-model="item.price"/>
       <label>Size</label>
      <input type="text" placeholder="Product size" v-model="item.size"/>
      <!-- sep component -->
      <label>Image</label>
      <image-upload v-on:image-updated="item.image = $event"></image-upload>
      <!-- sep component -->
      <label>Categories</label>
      <Multiselect 
      :v-model="value" 
      :options="categories" 
      :multiple="true" 
      :hide-selected="true">
      </Multiselect>
      <button @click="handleSubmit">List your Item</button>
    </form>
  </div>
</template>

<script>
// import external libraries
import Vue from 'vue'
import axios from 'axios'
import Multiselect from 'vue-multiselect'
// import child components here 
import ImageUpload from './ImageUpload.vue'

export default {
  name: "item-form",
// register imported components here so they can be used in the render/template
  components: {
    ImageUpload, Multiselect
  },

  data () {
    return {
      item: {
        name: '',
        price: '',
        size: '',
        available: '',
        image: '',
      },
      categories: [],
      value: null
    }
  },

  mounted () {
    this.getCategories()
  },

  methods: {

     async getCategories () {
       try {
      const res = await axios.get('/api/categories')
      this.categories = res.data.map(category => category.name)
      // need to find a way to pass the ID into the database 
      console.log(this.categories)
       }
       catch (err) {
         console.log(err)
       }
    },

    // write handle multi-select here 

    async handleSubmit () {
      console.log('submitted')
      console.log(this.item)

      try {
        await axios.post("/api/items", this.item)
      }
      catch (error) {
        console.log(error)
      }
    }
  }
}
</script>

<style scoped></style>

