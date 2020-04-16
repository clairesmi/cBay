<template>
  <div id="app" class="h-screen bg-red-200">
    <navbar></navbar>
    <!-- <Home /> -->
    <router-view :key="$route.fullPath"></router-view>
  </div>
</template>
//
<script>
// import ItemsIndex from "./components/items/ItemsIndex.vue";
// import ItemShow from "./components/items/ItemShow.vue";
// import ItemNew from "./components/items/ItemNew.vue";
// import ItemEdit from "./components/items/ItemEdit.vue";
// import Home from "./components/common/Home.vue";
// import CategoriesIndex from "./components/categories/CategoriesIndex.vue";
// import CategoryShow from "./components/categories/CategoryShow.vue";
// import Register from "./components/common/Register.vue";
// import Login from "./components/common/Login.vue";
// import Profile from "./components/common/Profile.vue";
// import ProfileEdit from "./components/common/ProfileEdit.vue";
// import ProfileView from "./components/user_interaction/ProfileView.vue";
// import Basket from "./components/items/Basket.vue";
// import Checkout from "./components/items/Checkout.vue";
import Navbar from "./components/common/Navbar.vue";
// import NotFound from "./components/common/NotFound.vue";
// import Vue from "vue";
import "style-loader";

export default {
  name: "App",
  components: {
    // Home,
    Navbar
    // ItemsIndex,
    // ItemShow
    // ItemNew,
    // ItemEdit,
    // CategoriesIndex,
    // CategoryShow,
    // Register,
    // Login,
    // Profile,
    // ProfileEdit,
    // ProfileView,
    // Basket,
    // Checkout,
    // NotFound
  }
};
</script>
