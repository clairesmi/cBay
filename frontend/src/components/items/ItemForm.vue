<template>
  <div id="item-form">
    <router-link to="/">Home</router-link>
    <form>
      <label>Name</label>
      <input type="text" placeholder="Product name"/>
      <label>Price</label>
       <label>Size</label>
      <input type="text" placeholder="Product size"/>
      <input type="number" placeholder="0.00" step="0.01" />
      <label>Available</label>
      <input type="checkbox" /> 
      <!-- sep component -->
      <label>Image</label>
      <input type="file" placeholder="Upload Image"/>
      <!-- sep component -->
      <label>Categories</label>
      <!-- <multiselect 
      v-model="value" 
      :options="categories" 
      :multiple="true" 
      :hide-selected="true">
      </multiselect> -->
      <button>List your Item</button>
    </form>
  </div>
</template>

<script>
import Vue from 'vue'
import Multiselect from 'vue-multiselect'

  // register globally
  Vue.component('multiselect', Multiselect)

export default {
  name: "item-form",
  data () {
    return {
      item: {
        name: '',
        price: '',
        size: '',
        available: '',
        image: '',
        categories: [],
      }
    }
  }
}
</script>

<style scoped></style>

