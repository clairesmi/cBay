<template>
  <div id="app" class="h-screen bg-red-200">
    <navbar></navbar>
    <!-- <Home /> -->
    <router-view :key="$route.fullPath"></router-view>
  </div>
</template>
//
<script>
import Navbar from "./components/common/Navbar.vue";
import "style-loader";

export default {
  name: "App",
  components: {
    Navbar
  }
};
</script>
