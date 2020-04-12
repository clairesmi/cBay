<template>
<div id='app' class=" h-screen bg-red-200">
  <navbar></navbar>
  <router-view :key="$route.fullPath"></router-view>
</div>
</template>
<script>
import ItemsIndex from './items/ItemsIndex.vue'
import ItemShow from './items/ItemShow.vue'
import ItemNew from './items/ItemNew.vue'
import ItemEdit from './items/ItemEdit.vue'
import Home from './common/Home.vue'
import CategoriesIndex from './categories/CategoriesIndex.vue'
import CategoryShow from './categories/CategoryShow.vue'
import Register from './common/Register.vue'
import Login from './common/Login.vue'
import Profile from './common/Profile.vue'
import ProfileEdit from './common/ProfileEdit.vue'
import ProfileView from './user_interaction/ProfileView.vue'
import Basket from './items/Basket.vue'
import Checkout from './items/Checkout.vue'
import Navbar from './common/Navbar.vue'
import NotFound from './common/NotFound.vue'
import Vue from 'vue'
import 'style-loader'

export default {
  name: "App",
  components: {
    Home,
    Navbar,
    ItemsIndex,
    ItemShow,
    ItemNew,
    ItemEdit,
    CategoriesIndex, 
    CategoryShow,
    Register,
    Login,
    Profile, 
    ProfileEdit,
    ProfileView,
    Basket,
    Checkout,
    NotFound
  },

}
</script>