<template>
  <div id="category-show" class=" flex flex-col justify-center items-center font-sans bg-red-200">
    <h1 class="animated zoomInDown category-title tracking-wide text-orange-600"
     v-if="category">{{ this.header.slice(0, 1).toUpperCase() + this.header.slice(1) }}</h1>
     <div class="flex w-3/6 justify-center items-center bg-white">
       <form class="flex w-3/6">
        <input class="w-full"
        placeholder=" search by keyword"
        v-model="searchTerm"
        @input.prevent="listingSearch"
      />
      </form>
      <multiselect class="pr-20 w-2/4"
      v-model="selectedSizes"
      @input="listingSearch"
      :options="sizes"
      :multiple="true"
      placeholder="Filter by size"
      >
      <template slot="singleLabel" slot-scope="{ option }">{{ option }}</template>
      </multiselect>
    </div>
    <div v-if="category.length" class="flex flex-row flex-wrap justify-around p-5">
      <div v-for="elem in listingSearch()" :key="elem.id" class="item-card flex flex-col p-5 bg-white m-5">
        <router-link :to="`/items/${elem.id}/`"><img :src="elem.image" /></router-link>
        <div class="flex flex-row justify-around pt-8">
          <h2>{{ elem.name }}</h2>
          <h3>${{ elem.price.toFixed(2) }}</h3>
          <h4>Size: {{ elem.size }}</h4>
        </div>
      </div>
    </div>
    <div v-if="category.length">
      <div class="flex flex-col items-center" v-if="!listingSearch().length">
        <h1 class="not-found-header p-5 text-orange-600">Sorry...</h1>
        <p class="not-found-text text-gray-800">We don't currently have anything that matches your search criteria</p>
        <p class="not-found-text text-gray-800">Please try another search!</p>
      </div>
    </div>
  </div>
</template>
<script>

import axios from 'axios'
import Multiselect from 'vue-multiselect'

export default {
  name: "category-show",
  components: {
    Multiselect
  },
  data() {
    return {
      category: [],
      header: this.$route.params.catName,
      searchTerm: '',
      sizes: [],
      selectedSizes: [],
      filteredItems: []
    }
  },
  async mounted() {
    this.getCategory()
  },
  methods: {
    async getCategory() {
      try {
      const res = await axios.get(`/api/categories/${this.$route.params.id}`)
      this.category = res.data.items
      console.log(this.category)
      this.sizes = this.category.reduce((a, b) => {
        if (!a.includes(b.size)) {
          a.push(b.size)
        } return a 
      }, [])
    }
      catch (err) {
        this.$router.push('/notfound')
      }
    },
    listingSearch() {
      const { category, searchTerm, selectedSizes } = this
      const re = new RegExp(searchTerm, 'i')
      return category.filter(item => {
        return re.test(item.name) && selectedSizes.length ? selectedSizes.includes(item.size) 
        : (re.test(item.name) && category)
        })
    },
  }

}
</script>
<style scoped>
.category-title {
  font-family: 'Pacifico', cursive;
  font-size: 80px;
}

.item-card {
  height: 490px;
  font-family: 'Permanent Marker', cursive;
  font-size: 20px;
}

.multiselect {
  font-family: 'Oswald', sans-serif;
  letter-spacing: 0.5px;
}

img {
  height: 380px;
  width: 380px;
}
form {
  font-family: 'Oswald', sans-serif;
  font-size: 16px;
  letter-spacing: 0.5px;
  color: #35495e;
}
button {
  text-decoration: underline;
}
.not-found-header {  
  font-family: 'Pacifico', cursive;
  font-size: 80px;
}
.not-found-text {
  font-family: 'Oswald', sans-serif;
  font-size: 22px;
  padding: 5px;
}
</style>