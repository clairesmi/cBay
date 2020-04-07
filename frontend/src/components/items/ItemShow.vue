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
    <router-link :to="{path: `/items/${item.id}/`}"><img :src=item.image class="small-image" alt="category-image"/>
    </router-link>
  </div>
  <div v-if="!isOwner" class="add-to-basket-wrapper">
    <button @click.prevent="addToBasket">Add to basket</button>
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
    othersInCategory: [],
    isOwner: false
    }
  },

  async mounted () {
    await this.getItem()
    this.isOwnerCheck()
    
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
        this.$router.push('/notfound')
      }
    },
    // check if the logged in user is also the owner of the posted item 
    // so they can be permitted to edit or delete
    isOwnerCheck() {
      if (!this.item.owner) return null
      // console.log(Auth.getPayload().sub === this.item.owner.id)
      this.isOwner = Auth.getPayload().sub === this.item.owner.id
      console.log(this.isOwner)
    },

    async addToBasket() {

      // if user is not logged in (if no payload) 
      // then push user to login page, else execute the below

      // sort out router links

      const userID = Auth.getPayload().sub
      const owner = this.item.owner
      const item = {...this.item, basket: userID, available: false, owner: this.item.owner.id, 
      categories: this.item.categories.map(category => category.id) }
      this.item = item
      try {
      await axios.patch(`/api${this.$route.path}/`, this.item)
      this.$router.push('/items')
      }
      catch (err) {
        this.$router.push('/notfound')
      }
    },

    async handleDelete() {
      try {
      await axios.delete(`/api${this.$route.path}`, {
        headers: { Authorization: `Bearer ${Auth.getToken()}` }
          })
          this.$router.push('/items')
        }
        catch (err) {
        this.$router.push('/notfound')
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