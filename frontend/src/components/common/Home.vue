<template>
  <div id="home">
    <h1>{{ msg }}</h1>
    <router-link to="/items">Go to Listings</router-link>
    <router-link to="/items/new">List a new Item</router-link>
  </div>
</template>
<script>
export default {
  name: 'home',
  data () {
    console.log('hello')
    return {
      msg: 'Home Page'
    }
  }
}
</script>
<style scoped></style>