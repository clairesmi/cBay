<template>
<div>
  <h1>Home Page</h1>
  <items-index :items="items" />
  <item-form :item="item" />
</div>
</template>
<script>
import ItemsIndex from './items/ItemsIndex.vue'
import ItemForm from './items/ItemForm.vue'
import axios from 'axios'
import 'style-loader'

export default {
  name: "Main",
  components: {
    ItemsIndex,
    ItemForm,
  }, 
  data() {
    return {
      items: [],
      item: {}
    }
  }, 

  mounted () {
    this.getItems()
  },

methods: {
  async getItems () {
    try {
      const response = await axios.get("/api/items")
      this.items = response.data
      // console.log(this.items.map(elem => elem.categories.map(item => item.items.map(el => el.name))))
    }

    catch (error) {
      console.log(error)
    }
  }
}

}
</script>

<style scoped></style>