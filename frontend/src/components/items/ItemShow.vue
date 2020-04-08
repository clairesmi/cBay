<template>
<div id="item-show">
<div v-if="item" class="show-page-wrapper flex flex-col justify-center w-full">
  <div class="flex flex-row justify-center mt-5 mb-3">
    <div class="flex h-full">
      <img :src=item.image alt="item-image" class="w-full"/>
    </div>
    <div class="bg-red-100 w-1/3">
      <h1>{{ item.name }}</h1>
      <h3>${{ item.price }}</h3>
      <router-link v-if="item.owner" :to="`/profile/${item.owner.id}/`"><p>Posted by {{ item.owner.username }}</p></router-link>
      <p>Size: {{ item.size }}</p>
      <p v-if="item.categories">{{ item.categories.length > 1 ? 'Categories:' : 'Category:'}} </p>
      <p v-for="category in item.categories" :key="category.name">{{ category.name.slice(0, 1).toUpperCase() + category.name.slice(1) }}</p>
      <div v-if="!isOwner" class="add-to-basket-wrapper">
        <button @click.prevent="addToBasket">Add to Basket</button>
      </div>
      <div v-if="isOwner" class="item-delete">
        <button @click.prevent="handleDelete">Delete this item</button>
        <router-link :to="`/items/${item.id}/edit`"><button>Edit this item</button></router-link>
      </div>
    </div>
  </div>
  <div class="flex justify-center items-center pb-3">
    <h3 v-if="othersInCategory.length">Other items you might like:</h3>
  </div>
  <div class="flex justify-center items-center w-full">
    <div v-for="item in othersInCategory" :key="item.id" class="flex flex-col pr-10"> 
      <router-link :to="`/items/${item.id}/`">
        <img :src=item.image class="small-image" :alt="item.name"/>
      </router-link>
      <p>${{ item.price }}</p>
      <p>Size: {{ item.size }}</p>
      </div>
  </div>
  
</div>
  <div v-if="loginModal">
    <div class="login-modal">
      <div class="modal-text">
        <p>You must be logged in to fill your basket!</p>
        <router-link to="/register"><button>Sign Up</button></router-link>
        <router-link to="/login"><button>Login</button></router-link>
      </div>
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
    isOwner: false,
    loginModal: false
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
      // if user is not logged in (if no payload sub) 
      // then push user to login page, else execute the below
      if (Auth.getPayload().sub) {
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
      } else {
        this.loginModal = true
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
  height: 140px;
  width: 140px;
}
.login-modal {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  width: 100vw;
  position: fixed;
  top: 50%;  
  left: 50%;
  transform: translate(-50%, -50%);
}
.modal-text {
  background-color: green;
  width: 50vw;
  height: 50vh;
  opacity: 1;
}
</style>