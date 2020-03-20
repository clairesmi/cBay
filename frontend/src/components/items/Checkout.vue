<template>
  <div id="checkout">
    <h1>Checkout</h1>
    <router-link to="/basket">Back to Basket</router-link>
    <h2>Total: £{{ total }}</h2>
    <button @click="makePayment">Make Payment</button>
  </div>
</template>
<script>

import axios from 'axios'
import Auth from '../../lib/auth'

export default {
  name: "checkout",
  data() {
    return {
      items: [],
      total: null
    }
  },
  mounted() {
    this.getTotal()
  },
  methods: {
    async getTotal() {
      try {
      const res = await axios.get('api/basket')
      this.items = res.data
        }
      catch (err) {
        console.log(err)
        }
      const priceArray = this.items.map(item => item.price)
      this.total = priceArray.reduce((total, current) => total + current, 0).toFixed(2)
    },
    makePayment() {
      const userID = Auth.getPayload().sub
      const purchased = { purchased: userID }
      console.log(purchased)
      try {
        this.items.map(item => axios.patch(`/api/items/${item.id}/`, {...item, owner: item.owner.id, 
        purchased: userID,
        categories: item.categories.map(category => category.id)}))
        console.log(this.items)
        this.$router.push('/profile')
      }
      catch (err) {
        console.log(err)
      }
    }
  },
}
</script>
<style scoped>

</style>