<template>
<div id="item-show">
  <h1>Item Show Page</h1>

<div>
<h2>{{ item.name }}</h2>
<div>
  <img :src=item.image />
</div>
<div>
  <h3>${{ item.price }}</h3>
  <p>Size: {{ item.size }}</p>
  <p>Categories:</p>
  <p v-for="category in item.categories" :key="category.name">{{ category.name }}</p>
  <p>Other items in this category:</p>
  <div v-for="item in othersInCategory" :key="item.id"> {{ item.name }}
    <router-link :to="`/items/${item.id}/`"><img :src=item.image class="small-image"/></router-link>
  </div>
  
</div>
</div>
<!-- create boolean condition for availability and grey out if not available -->
  </div>
</template>

<script>

import axios from 'axios'

export default {
  name: "item-show",
  data () {
    return {
    item: {},
    othersInCategory: []
    }
  },

  mounted () {
    this.getItem()
    // console.log(this.otherCategories)
    
  },

  methods: {
    async getItem () {
      try {
        const res = await axios.get(`/api${this.$route.path}`)
        // console.log(typeof this.$route.params.id)
        this.item = res.data
        const othersInCategory = this.item.categories.map(category => 
          category.items.filter(item => item.id !== parseInt(this.$route.params.id)))
            this.othersInCategory = othersInCategory[0]
      }
      catch (error) {
        console.log(error)
      }
    },

    }
  }

</script>

<style scoped>
img {
  height: 400px;
  width: 400px;
}

.small-image {
  height: 200px;
  width: 200px;
}
</style>