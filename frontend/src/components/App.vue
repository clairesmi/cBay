<template>
<div id='app'>
  <router-view >
  </router-view>
</div>
</template>
<script>
import ItemsIndex from './items/ItemsIndex.vue'
import ItemShow from './items/ItemShow.vue'
import ItemNew from './items/ItemNew.vue'
import Home from './common/Home.vue'
import Vue from 'vue'
import 'style-loader'

export default {
  name: "App",
  components: {
    ItemsIndex,
    ItemShow,
    ItemNew,
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