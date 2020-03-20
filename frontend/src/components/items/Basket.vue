<template>
<div id="basket"  v-if="items">
  <!-- TOTAL (USE REDUCE FOR THIS)-->
  <!-- PAY - empty basket and remove items from item index, create a field to store 'purchased' items
  which can be displayed on users profile-->
  <div class="basket-headers">
  <h1>What's in your basket?</h1>
  <h2>Total: ${{ total }}</h2>
  <router-link to="/checkout"><button>Go to checkout</button></router-link>
  </div>
  <div class="basket-wrapper" v-for="item in items" :key="item.id">
      <div class="item-info">
        <h3>{{ item.name }}</h3>
        <router-link :to="`/items/${item.id}/`"><img :src=item.image alt="item-image" class="item-image"/>
        </router-link>
        <p>${{ item.price }}</p>
        <p>Size: {{ item.size }}</p>
        <p v-if="item.owner">Listed by: {{ item.owner.username }}</p>
        <button @click="removeCheck" :id="item.id">Remove from basket</button>
    </div>
  <div v-if="modalShow">
    <div class="check-modal">
      <div class="modal-text">
      <p>Are you sure you want to remove this item from your basket?</p>
      <button @click="handleRemove" :id=item.id>Yes</button>
      <button @click="handleRemove" :id=item.id>No</button>
      </div>
    </div>
  </div>
  </div>
  </div>
</template>
<script>

import axios from 'axios'

export default {
  name: "basket",
  data() {
    return {
      items: {},
      modalShow: false,
      item: {},
      total: null
    }
  },

  async mounted() {
    await this.getBasket()
    this.calculateTotal()
  },
  methods: {
    async getBasket() {
      const res = await axios.get('/api/basket')
      // console.log(res.data)         
      this.items = res.data
    },
    async removeCheck() {
      const res = await axios.get(`api/items/${event.target.id}/`) 
      // console.log(res.data)
      this.item = res.data
      this.modalShow = !this.modalShow
      // console.log(this.modalShow)
    },
    async handleRemove() {
      //  if yes, use item ID to patch to update it with basket null 
      // console.log(event.target)
      if (event.target.innerText === 'No') {
        this.modalShow = !this.modalShow 
        // console.log(event.target.id)
        }
      else {  
      const owner = this.item.owner
      const item = {...this.item, basket: null, available: true, owner: owner.id, 
      categories: this.item.categories.map(category => category.id)}
       this.item = item
      try {
      await axios.patch(`/api/items/${this.item.id}/`, this.item)
      this.$router.push('/items')
      }
      catch (err) {
        console.log(err)
        }
      }
    },
    calculateTotal() {
      const priceArray = this.items.map(item => item.price)
      this.total = priceArray.reduce((total, current) => total + current)
    }
  }
}


</script>
<style scoped>
img {
  height: 200px;
  width: 200px;
}
.check-modal {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  width: 100vw;
  /* background: beige; */
  /* opacity: 0.2; */
  position: fixed;
  top: 50%;  
  left: 50%;
  transform: translate(-50%, -50%);
  /* z-index: 1;  */
}
.modal-text {
  background-color: green;
  width: 50vw;
  height: 50vh;
  /* z-index: 2; */
  opacity: 1;
}
</style>