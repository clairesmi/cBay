<template>
  <div id="home" class="h-screen flex flex-col">
    <nav class="pl-8 pr-16 header-wrapper w-screen flex flex-row flex justify-between">
    <h2 class="text-red-700">{{ msg }}</h2>
    <div class="link-wrapper">
    <router-link to="/items">Go to Listings</router-link>
    <router-link to="/items/new">List a new Item</router-link>
    </div>
    </nav>
    <div class="title-wrapper h-64 flex justify-center flex items-center">
      <h1 class="text-6xl tracking-wide">cBay</h1>
    </div>
    <div class="carousel-wrapper">
      Categories
        <p class="each-category text-4xl pl-8 pr-8">all (see everything)</p>
      <div class="categories-index flex flex-row items-center justify-center">
        <button id="left-button" @click="handleClick" class="left-button text-2xl m-10">previous</button>

        <div v-if="previousCategory" class="previous-category m-4 text-blue-700">{{this.previousCategory.name}}</div>
        <div v-if="currentCategory" class="current-category m-4 text-green-700">{{this.currentCategory.name}}</div>
        <div v-if="nextCategory" class="next-category m-4 text-orange-700">{{this.nextCategory.name}}</div>

        <button id="right-button" @click="handleClick" class="right-button text-2xl m-10">next</button>
        </div>
      </div>
    </div>
</template>
<script>

import axios from 'axios'

export default {
  name: 'home',
  data () {
    // console.log('hello')
    return {
      msg: 'Home Page',
      categories: null,
      previousCategory: null,
      currentCategory: null,
      nextCategory: null
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
      const carouselCategories = this.categories.map((category, index) =>  ({ index: index, name: category.name }))
      this.carouselCategories = carouselCategories
      // console.log(this.carouselCategories[3].name)
      this.currentCategory = this.carouselCategories[i]
      console.log(this.currentCategory.name)
      this.previousCategory = this.carouselCategories[i - 1]

      this.nextCategory = this.carouselCategories[i + 1]
        console.log(this.previousCategory.index)
        console.log(this.nextCategory.index)
    },

    handleClick() {
      let iPrevious = this.previousCategory.index
      let iCurrent = this.currentCategory.index
      let iNext = this.nextCategory.index
      // console.log(iPrevious)
      console.log(iCurrent)
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
    }
  }
}
</script>
<style scoped src='../../styles/output.css'>
/* Use scoped css file to only apply css styles to each specific component */

/* Or use import */
/* @import '../../styles/output.css'; */
</style>