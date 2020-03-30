<template>
  <div id='navbar' class="text-gray-800 bg-red-200">
      <b-navbar toggleable="sm" type="light" variant="light" class="flex flex-row justify-between pl-5 pr-5 pt-2">
        <router-link to="/">Home</router-link>
        <div class="link-wrapper flex flex-row">
          <div class="pr-3"><router-link to="/items">Go to Listings</router-link></div>
          <div v-if="isAuth()" class="pr-3"><router-link to="/items/new">New Listing</router-link></div>
          <div v-if="!isAuth()" class="pr-3"><router-link to="/register">Sign Up</router-link></div>
          <div v-if="!isAuth()" class="pr-3"><router-link to="/login">Login</router-link></div>
          <div v-if="isAuth()" class="pr-3"><router-link to="/profile">Your Profile</router-link></div>
          <div v-if="isAuth()" class="text-orange-600 pr-3"><a @click="handleLogout">Logout</a></div>
        </div>
      </b-navbar>
  </div>
  
</template>
<script>

import Auth from '../../lib/auth'

export default {
  name: 'navbar',
  mounted() {
    // this.isAuth()
  },
  methods: {
    handleLogout() {
      Auth.logout()
      this.$router.push('/items')
    },
    isAuth() {
      console.log(Auth.isAuthenticated())
      return Auth.isAuthenticated()
    },
  },
}  
</script>
<style scoped>
  #navbar {
    font-family: 'Oswald', sans-serif;
    font-size: 20px;
    text-decoration: underline;
  }
  a:hover {
    cursor: pointer;
  }
</style>