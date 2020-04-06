<template>
  <div id="category-show" class=" flex flex-col justify-center items-center font-sans bg-red-200">
  <div>
    <h1 class="animated zoomInDown category-title tracking-wide text-orange-600"
     v-if="category">{{ this.header.slice(0, 1).toUpperCase() + this.header.slice(1) }}</h1>
  </div>
    <div v-if="category" class="flex flex-row flex-wrap justify-around p-5">
      <div v-for="elem in category" :key="elem.id" class="item-card flex flex-col p-5 bg-white m-5">
        <router-link :to="`/items/${elem.id}/`"><img :src="elem.image" /></router-link>
        <div class="flex flex-row justify-around pt-8">
        <h2>{{ elem.name }}</h2>
        <h3>${{ elem.price.toFixed(2) }}</h3>
        <h4>Size: {{ elem.size }}</h4>
        </div>
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
      category: [],
      header: this.$route.params.catName
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
        this.$router.push('/notfound')
      }
    }
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

img {
  height: 380px;
  width: 380px;
}



</style>