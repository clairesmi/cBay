<template>
  <div id='navbar' class="text-gray-800 bg-red-200">
      <b-navbar toggleable="sm" type="light" variant="light" class="flex flex-row justify-between pl-5 pr-5 pt-2">
        <router-link to="/">Home</router-link>
          <div v-if="isLoggedIn" class="link-wrapper flex flex-row">
          <div class="pr-3"><router-link to="/items">Go to Listings</router-link></div>
            <div class="pr-3"><router-link to="/items/new">New Listing</router-link></div>
            <div class="pr-3"><router-link to="/profile">Your Profile</router-link></div>
            <div class="text-orange-600 pr-3"><a @click="handleLogout">Logout</a></div>
        </div>
        <div v-if="!isLoggedIn" class="link-wrapper flex flex-row">
          <div class="pr-3"><router-link to="/register">Sign Up</router-link></div>
          <div class="pr-3"><router-link to="/login">Login</router-link></div>
        </div>
      </b-navbar>
  </div>
  
</template>
<script>

import Auth from '../../lib/auth'
import { eventBus } from '../../app'

export default {
  name: 'navbar',
  data() {
    return {
      isLoggedIn: null
    }
  },
  methods: {
    handleLogout() {
      Auth.logout()
      this.isLoggedIn = this.isAuth()
      this.$router.push('/items')
    },
    isAuth() {
      return Auth.isAuthenticated()
    },
  },
  created() {
    eventBus.$on('userLoggedIn', () => {
      this.isLoggedIn = this.isAuth()
    })
  }

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