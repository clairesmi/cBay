<template>
<div id="item-show">
  <router-link to="/">Home</router-link>
  <h1>Item Show Page</h1>

<div>
<h2>{{ item.name }}</h2>
<div>
  <img :src=item.image alt="item-image" />
</div>
<div>
  <h3>${{ item.price }}</h3>
  <router-link v-if="item.owner" :to="`/profile/${item.owner.id}/`"><p>Posted by {{ item.owner.username }}</p></router-link>
  <p>Size: {{ item.size }}</p>
  <p>Categories:</p>
  <p v-for="category in item.categories" :key="category.name">{{ category.name }}</p>
  <p>Other items you might like:</p>
  <div v-for="item in othersInCategory" :key="item.id"> 
    <p>{{ item.name }}</p>
    <p>${{ item.price }}</p>
    <p>Size: {{ item.size }}</p>
    <router-link :to="`/items/${item.id}/`"><img :src=item.image class="small-image" alt="category-image"/>
    </router-link>
  </div>
  <div v-if="isOwner" class="item-delete">
    <button @click.prevent="handleDelete">Delete this item</button>
    <router-link :to="`/items/${item.id}/edit`"><button>Edit this item</button></router-link>
  </div>
  
</div>
</div>
<!-- add a location field into the show page with a map -->
  </div>
</template>

<script>

import axios from 'axios'
import Auth from '../../lib/auth'

export default {
  name: "item-show",
  data () {
    return {
    item: {},
    othersInCategory: []
    }
  },

  async mounted () {
    await this.getItem()
    this.isOwner()
    
  },

  methods: {
    async getItem () {
      try {
        const res = await axios.get(`/api${this.$route.path}`)
        // console.log(typeof this.$route.params.id)
        this.item = res.data
        // console.log(this.item.owner.id)
        const othersInCategory = this.item.categories.map(category => 
          category.items.filter(item => item.id !== parseInt(this.$route.params.id)))
            this.othersInCategory = othersInCategory[0]
      }
      catch (error) {
        console.log(error)
      }
    },
    isOwner() {
      if (!this.item.owner) return null
      console.log(Auth.getPayload().sub === this.item.owner.id)
      return Auth.getPayload().sub === this.item.owner.id
    },
    async handleDelete() {
      try {
      await axios.delete(`/api${this.$route.path}`, {
        headers: { Authorization: `Bearer ${Auth.getToken()}` }
          })
          this.$router.push('/items')
        }
        catch (err) {
        console.log(err)
        }
      }

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