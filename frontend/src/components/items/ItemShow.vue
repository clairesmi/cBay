<template>
<div id="item-show" class="bg-red-200 h-full">
<div v-if="item" class="show-page-wrapper flex flex-row justify-center h-full w-full bg-red-200 pt-5">
  <div class="product-wrapper flex flex-row justify-center w-4/5 mb-20">
    <div class="flex flex-col bg-white items-start justify-center items-center mr-10 pr-5 pl-5">
      <h1 class="item-show-header pr-5 pb-5">{{ item.name }}</h1>
      <img :src=item.image alt="item-image"/>
      <h3 v-if="item.price" class="item-show-header pt-5">${{ item.price.toFixed(2) }}</h3>
    </div>
    <div class="bg-red-100 h-full w-1/3 flex flex-col pl-5 pr-5 pt-10 pb-10 justify-between text-gray-800">
      <div class="details-wrapper h-full flex flex-col justify-start">
      <h4 class="title flex pb-1">Size: <p class="detail pl-1">{{ item.size }}</p></h4>
      <div class="item-category-header flex flex-col"><p class="pr-1 title" v-if="item.categories">{{ `${item.categories.length > 1 ? 'Categories' : 'Category'}` }}:  </p>
      <p class="detail detail-link pb-1" v-for="category in item.categories" :key="category.name">
        <router-link :to="`/categories/${category.id}/${category.name}`">{{ category.name.slice(0, 1).toUpperCase() + category.name.slice(1) }}
        </router-link></p></div>
      <router-link v-if="item.owner" :to="`/profile/${item.owner.id}/`">
      <h4 class="title flex">Posted by:  <p class="detail-link detail pl-1">{{ item.owner.username }}</p></h4></router-link>
      </div>
      <div class="buttons-wrapper flex flex-col items-center pb-16">
      <div v-if="!isOwner" class="add-to-basket-wrapper flex justify-center mt-20">
        <button class="button text-gray-900" @click.prevent="addToBasket">Add to Basket 🛒</button>
      </div>
      <div v-if="isOwner" class="item-delete">
        <button class="button text-gray-900" @click.prevent="handleDelete">Delete this item</button>
        <router-link :to="`/items/${item.id}/edit`"><button class="button text-gray-900">Edit this item</button></router-link>
      </div>
      </div>
    </div>
  </div>
  <div class="flex flex-col justify-center w-1/5 pt-2">
  <div class="flex">
    <h3 class="title-others text-orange-600" v-if="othersInCategory.length">Other items you might like:</h3>
  </div>
  <div class="flex flex-col justify-start items-start h-full w-full pt-3">
    <div v-for="item in othersInCategory.slice(0, 3)" :key="item.id" 
    class="flex flex-col h-48 m-4 pt-3 pr-2 pb-2 pl-2 bg-white items-center"> 
      <router-link :to="`/items/${item.id}/`">
        <img :src=item.image class="small-image" :alt="item.name"/>
      </router-link>
      <div class="small-image-text flex pb-2 pt-1 justify-around items-center">
      <p class="pr-1">Size: {{ item.size }}</p>
      <p>${{ item.price.toFixed(2) }}</p>
      </div>
      </div>
  </div>
  </div>
</div>
  <div v-if="loginModal">
    <div class="login-modal flex">
      <div class="modal-text bg-white flex flex-col justify-around items-center text-orange-600 pl-5">
        <div class="flex w-full h-full justify-end items-start pt-5 pr-5 text-gray-800">
        <button class="button flex justify-start items-start h-10" @click="loginModal = false">
          <p class="h-5 text-lg mb-1">X</p>
          </button>
        </div>
        <p class="pb-20">You must be logged in to fill your basket!</p>
        <div class="mb-20 text-gray-800 pb-3"> 
          <router-link to="/register"><button class="button text-gray-900 mr-2">Sign Up</button></router-link>
        <router-link to="/login"><button class="button text-gray-900 ml-2">Login</button></router-link>
        </div>
      </div>
    </div>
  </div>
</div>
<!-- add a location field into the show page with a map -->
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
.show-page-wrapper {
  font-family: 'Oswald', sans-serif;
  font-size: 22px;
  letter-spacing: 0.5px;
}
img {
  height: 400px;
  width: 400px;
}
.item-show-header {
  font-family: 'Permanent Marker', cursive;
  font-size: 60px;
}
.title {
  font-family: 'Oswald', sans-serif;
  font-size: 35px;
}
.title-others {
  font-family: 'Pacifico', cursive;
  font-size: 25px;
}
.detail {
  font-family: 'Oswald', sans-serif;
  font-size: 35px;
  letter-spacing: 0.5px;
}
.detail-link:hover {
  color: #dd6b33;
}
.button {
  padding: 5px 10px;
  box-shadow: 1px 1px 10px 1px gray;
  font-family: 'Oswald', sans-serif;
}
.button:hover {
  transform: scale(0.98);
  color: #dd6b33;
}

.small-image {
  height: 140px;
  width: 140px;
}
.small-image-text {
  font-family: 'Permanent Marker', cursive;
  font-size: 20px;
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
  box-shadow: 1px 1px 10px 1px gray;
  font-family: 'Pacifico', cursive;
  font-size: 30px;
  width: 50vw;
  height: 50vh;
  opacity: 1;
}
</style>