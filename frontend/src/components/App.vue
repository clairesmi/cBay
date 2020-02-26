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
import CategoriesIndex from './categories/CategoriesIndex.vue'
import CategoryShow from './categories/CategoryShow.vue'
import Vue from 'vue'
import 'style-loader'
// import 'postcss-loader'

export default {
  name: "App",
  components: {
    Home,
    ItemsIndex,
    ItemShow,
    ItemNew,
    CategoriesIndex, 
    CategoryShow
  }, 
  // data() {
  //   return {
  //     items: [],
  //     item: {}
  //   }
  // },

}
</script>