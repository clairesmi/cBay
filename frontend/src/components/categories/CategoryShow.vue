<template>
  <div id="category-show">
  <div>
    <h1>Category Show</h1>
  </div>
  <div v-if="category" >
  <div v-for="elem in category" :key="elem.id">
    <h2>{{ elem.name }}</h2>
    <router-link :to="`/items/${elem.id}/`"><img :src="elem.image" /></router-link>
    <h3>£{{ elem.price }}</h3>
    <h4>Size: {{ elem.size }}</h4>
  </div>
  </div>
  </div>
</template>
<script>

import axios from 'axios'

export default {
  name: "category-show",
  data() {
    return {
      category: []
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
      }
      catch (err) {
        console.log(err)
      }
    }
  }

}
</script>
<style scoped>

</style>