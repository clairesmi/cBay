<template>
<div id="item-show">
<div v-if="item" class="show-page-wrapper flex flex-col justify-center w-full">
  <div class="flex flex-row justify-center mt-5 mb-2 pb-2">
    <div class="flex h-full">
      <img :src=item.image alt="item-image" class="w-full"/>
    </div>
    <div class="bg-red-100 w-1/3 flex flex-col pl-5 pr-5 pt-2 justify-start">
      <div class="item-show-header flex pb-5 text-orange-600"><h1 class="pr-5">{{ item.name }}</h1>
      <h3>${{ item.price }}</h3>
      </div>
      <h4 class="title flex">Size: <p class="detail pl-1">{{ item.size }}</p></h4>
      <div class="item-category-header flex"><p class="pr-1 title" v-if="item.categories">{{ `${item.categories.length > 1 ? 'Categories' : 'Category'}` }}:  </p>
      <p class="detail detail-link" v-for="category in item.categories" :key="category.name">
        <router-link :to="`/categories/${category.id}/${category.name}`">{{ category.name.slice(0, 1).toUpperCase() + category.name.slice(1) }}
        </router-link></p></div>
      <router-link v-if="item.owner" :to="`/profile/${item.owner.id}/`">
      <h4 class="title flex">Posted by: <p class="detail-link detail pl-1">{{ item.owner.username }}</p></h4></router-link>
      <div v-if="!isOwner" class="add-to-basket-wrapper flex justify-center mt-20">
        <button @click.prevent="addToBasket">Add to Basket 🛒</button>
      </div>
      <div v-if="isOwner" class="item-delete">
        <button @click.prevent="handleDelete">Delete this item</button>
        <router-link :to="`/items/${item.id}/edit`"><button>Edit this item</button></router-link>
      </div>
    </div>
  </div>
  <div class="flex justify-center items-center">
    <h3 class="title text-orange-600" v-if="othersInCategory.length">Other items you might like:</h3>
  </div>
  <div class="flex justify-center items-center w-full">
    <div v-for="item in othersInCategory" :key="item.id" 
    class="flex flex-col m-5 p-3 bg-white justify-center items-center"> 
      <router-link :to="`/items/${item.id}/`">
        <img :src=item.image class="small-image" :alt="item.name"/>
      </router-link>
      <div class="small-image-text flex pb-3 pt-1 justify-around items-center">
      <p class="pr-1">Size: {{ item.size }}</p>
      <p>${{ item.price.toFixed(2) }}</p>
      </div>
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
.show-page-wrapper {
  font-family: 'Oswald', sans-serif;
  font-size: 22px;
  letter-spacing: 0.5px;
}
.item-show-header {
  font-family: 'Pacifico', cursive;
  font-size: 40px;
}
.title {
  font-family: 'Pacifico', cursive;
  font-size: 30px;
}
.detail {
  font-family: 'Oswald', sans-serif;
  font-size: 22px;
  letter-spacing: 0.5px;
  padding-top: 10px;
}
.detail-link:hover {
  transform: scale(1.1);
  color: #dd6b33;
}
img {
  height: 400px;
  width: 400px;
}
button {
  padding: 5px 10px;
  box-shadow: 1px 1px 10px 1px gray;
}
button:hover {
  transform: scale(0.98);
}

.small-image {
  height: 160px;
  width: 160px;
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
  background-color: green;
  width: 50vw;
  height: 50vh;
  opacity: 1;
}
</style>