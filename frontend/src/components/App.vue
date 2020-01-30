<template>
<div id='app'>
  <router-view ></router-view>
  <!-- <h1>Home Page</h1> -->
</div>
</template>
<script>
import ItemsIndex from './items/ItemsIndex.vue'
import ItemForm from './items/ItemForm.vue'
import Home from './common/Home.vue'
import axios from 'axios'
import Vue from 'vue'
import 'style-loader'

export default {
  name: "App",
  components: {
    ItemsIndex,
    ItemForm,
    Home
  }, 
  data() {
    return {
      items: [],
      item: {}
    }
  }, 

//   mounted () {
//     this.getItems()
//   },

// methods: {
//   async getItems () {
//     try {
//       const response = await axios.get("/api/items")
//       this.items = response.data
//       // console.log(this.items.map(elem => elem.categories.map(item => item.items.map(el => el.name))))
//     }

//     catch (error) {
//       console.log(error)
//     }
//   }
// }

}
</script>

<style scoped></style>