<template>
  <h1>Item Show Page</h1>
</template>

<script>

import axios from 'axios'

export default {
  name: "item-show",
  props: {
    items: Array
  },
  data () {
    return {
    item: {}
    }
  },

  mounted () {
    this.getItem()
    // console.log(this.$route)
  },

  methods: {
    async getItem () {
      try {
        const itemId = this.$route.params.id
        const res = await axios.get(`/api/items/${itemId}`)
        console.log(res.data)
        this.item = res.data
      }
      catch (error) {
        console.log(error)
      }
    }
  }

}
</script>

<style scoped>

</style>