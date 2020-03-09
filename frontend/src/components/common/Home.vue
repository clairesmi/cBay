<template>
  <div id="home" class="h-screen flex flex-col">
    <nav class="pl-8 pr-16 header-wrapper w-screen flex flex-row flex justify-between">
    <h2 class="text-red-700">{{ msg }}</h2>
    <div class="link-wrapper">
    <router-link to="/items">Go to Listings</router-link>
    <router-link to="/items/new">List a new Item</router-link>
    <router-link to="/register">Sign Up</router-link>
    <router-link to="/login">Login</router-link>
    <router-link to="/profile">Your Profile</router-link>
    <a @click="handleLogout">Logout</a>
    </div>
    </nav>
    <div class="title-wrapper h-64 flex justify-center flex items-center">
      <h1 class="text-6xl tracking-wide">cBay</h1>
    </div>
    <div class="carousel-wrapper flex flex-col justify-center">
      Categories
        <p class="each-category text-4xl pl-8 pr-8">all (see everything)</p>
      <div class="categories-index flex flex-row items-center justify-center w-screen">
        <button id="left-button" @click="handleClick" class="left-button text-2xl m-10"
        :disabled="leftButtonDisabled">previous</button>

        <router-link v-if="previousCategory" :to="{ path: `/categories/${this.previousCategory.id}` }"><div v-if="previousCategory" class="previous-category m-4 text-6xl text-blue-700 h-48 w-12/12 border border-black
        flex flex-col justify-center items-center">
          {{this.previousCategory.name}}</div></router-link>
        <router-link v-if="currentCategory" :to="{ path: `/categories/${this.currentCategory.id}` }"><div v-if="currentCategory" class="current-category m-4 text-6xl text-green-700 h-64 w-12/12 border border-black
        flex flex-col justify-center items-center">
          {{this.currentCategory.name}}</div></router-link>
        <router-link v-if="nextCategory" :to="{ path: `/categories/${this.nextCategory.id}` }"><div v-if="nextCategory" class="next-category m-4 text-6xl text-orange-700 h-48 w-12/12 border border-black
        flex flex-col justify-center items-center">
          {{this.nextCategory.name}}</div></router-link>

        <button id="right-button" @click="handleClick" class="right-button text-2xl m-10"
        :disabled="rightButtonDisabled">next</button>
        </div>
      </div>
    </div>
</template>
<script>

import axios from 'axios'
import Auth from '../../lib/auth'
import 'animate.css'

export default {
  name: 'home',
  data () {
    // console.log('hello')
    return {
      msg: 'Home Page',
      categories: null,
      previousCategory: null,
      currentCategory: null,
      nextCategory: null,
      leftButtonDisabled: false,
      rightButtonDisabled: false,
    }
  },
  async mounted () {
    await this.getCategories()
    this.mapCarouselCategories()
  },
  methods: {
    async getCategories() {
      try {
      const res = await axios.get("api/categories")
      this.categories = res.data
      // console.log(this.categories)
      }
      catch(err) {
        console.log(err)
      }
    },

    mapCarouselCategories() {
      let i = 1
      const carouselCategories = this.categories.map((category, index) =>  ({ id: index + 1, index: index, name: category.name }))
      this.carouselCategories = carouselCategories
      this.currentCategory = this.carouselCategories[i]
      this.previousCategory = this.carouselCategories[i - 1]

      this.nextCategory = this.carouselCategories[i + 1]
    },

    handleClick() {
      let timerId
      let iPrevious = this.previousCategory.index
      let iCurrent = this.currentCategory.index
      let iNext = this.nextCategory.index
      const currCategory = document.querySelector('.current-category')
      timerId = setTimeout(function() {
        currCategory.classList.add('animated', 'pulse')
          setTimeout(function() {
            currCategory.classList.remove('animated', 'pulse')

          }, 700)
        
        }, 100)
      // this.previousCategory('animated pulse')
      // console.log(iNext)

    if (event.target.id === 'right-button' && this.currentCategory.index < this.carouselCategories.length - 1 && this.nextCategory.index !== this.carouselCategories.length - 1) {
      this.currentCategory = this.carouselCategories[iCurrent += 1]
      this.previousCategory = this.carouselCategories[iPrevious += 1]
      this.nextCategory = this.carouselCategories[iNext += 1]
      }

    if (event.target.id === 'left-button' && this.currentCategory.index > 0 && this.previousCategory.index !== 0) {
      this.currentCategory = this.carouselCategories[iCurrent -= 1]
      this.previousCategory = this.carouselCategories[iPrevious -= 1]
      this.nextCategory = this.carouselCategories[iNext -= 1]
      }

    this.nextCategory.index === this.carouselCategories.length - 1 ? this.rightButtonDisabled = true : 
      this.rightButtonDisabled = false

        this.previousCategory.index === 0 ? this.leftButtonDisabled = true : 
          this.leftButtonDisabled = false  

    },
    handleLogout() {
      Auth.logout()
      this.$router.push('/items')
    }
  }
}
</script>
<style scoped src='../../styles/output.css'>
/* Use scoped css file to only apply css styles to each specific component */

/* Or use import */
/* @import '../../styles/output.css'; */
</style>