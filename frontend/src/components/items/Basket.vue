<template>
<div id="basket">
  <!-- remember to add in delete from basket (remove user id from item) -->
  <!-- TOTAL (USE REDUCE FOR THIS)-->
  <!-- PAY -->
  <h1>What's in your basket?</h1>
  <div class="basket-wrapper">

  </div>
  </div>
</template>
<script>

import axios from 'axios'

export default {
  name: "basket",
  data() {
    return {
      items: {}
    }
  },
  mounted() {
    this.getBasket()
  },
  methods: {
    async getBasket() {
      const res = await axios.get('/api/basket')
      console.log(res.data)         
      this.items = res.data
    }
  }
}
</script>
<style scoped>

</style>