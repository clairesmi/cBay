<template>
  <div id="item-new">
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
      <image-upload v-on:image-upload="item.image = $event"></image-upload>
      <label>Categories</label>
        <div>
          <multiselect @input="handleMultiSelect"
            v-model="value"
            :options="categories"
            :multiple="true"
            track-by="name"
            label="name"
            placeholder="Select item categories">
              <template slot="singleLabel" slot-scope="{ option }">{{ option.name }}</template>
          </multiselect>
            <pre class="categories-chosen"><code>{{ value ? value.name: null }}</code></pre>
        </div>
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
  name: "item-new",
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
        available: true,
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

     async getCategories() {
       try {
      const res = await axios.get('/api/categories')
      this.categories = res.data
      // .map(category => category.name)
      // need to find a way to pass the ID into the database 
      // console.log(this.categories)
       }
       catch (err) {
         console.log(err)
       }
    },

    // write handle multi-select here 

    handleMultiSelect(value) {
      // console.log(value)
      if (!value) {
        return this.item = {...this.item, categories: []}
      }
      this.item = {...this.item, categories: value.map(val => val.id)}
      // console.log(this.item)
    },

    async handleSubmit () {
      // console.log('submitted')
      console.log(this.item)

      try {
        await axios.post("/api/items", this.item)
        this.$router.push('/profile')
      }
      catch (error) {
        console.log(error)
      }
    }
  }
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style scoped></style>

