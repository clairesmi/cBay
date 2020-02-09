<template>
  <div id="home" class="max-w-sm mx-auto flex p-12 bg-red rounded-lg shadow-xl">
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
<style scoped src='../../styles/output.css'>
/* Use scoped css file to only apply css styles to each specific component */

/* Or use import */
/* @import '../../styles/output.css'; */
</style>