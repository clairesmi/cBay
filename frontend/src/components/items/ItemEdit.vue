<template>
  <div id="item-edit">
    <h1>Edit Item</h1>
    <item-form v-if="item" 
    :item="item" 
    :categories="categories" 
    :value="value"
    @submit-clicked="handleSubmit"
    @multi-select-input="handleMultiSelect"
    >
    </item-form>
  </div>
</template>
<script>
import axios from 'axios'
import ItemForm from '../items/ItemForm.vue'

export default {
  name: "item-edit",
  components: {
    ItemForm
  },
  data() {
    return {
      item: {
        name: '',
        price: '',
        size: '',
        available: true,
        image: '',
      },
      categories: [],
      value: []
    }
  },

    mounted() {
      this.getItem()
      this.getCategories()
    },
    methods: {
      async getItem() {
        const itemId = this.$route.params.id
        const res = await axios.get(`/api/items/${itemId}`)
        // console.log(res.data)
        this.item = res.data
        // console.log(this.item)
      },
      async getCategories() {
        try {
        const res = await axios.get('/api/categories')
        // console.log(res)
        this.categories = res.data
          }
        catch (err) {
          console.log(err)
        }
      },
      async handleSubmit() {
        // event.preventDefault()
        const itemId = this.$route.params.id
        const item = {... this.item, owner: this.item.owner.id}
        this.item = item
          console.log(this.item)
        try {
          await axios.patch(`/api/items/${itemId}/`, this.item)
          this.$router.push('/profile')
        }
          catch (error) {
          console.log(error)
        }
      },
      //  updatedValue can be used from the child component
      handleMultiSelect(updatedValue) {
        console.log(updatedValue)
        if (!updatedValue) {
        return this.item = {...this.item}
          }
        this.item = {...this.item, categories: updatedValue.map(val => val.id)}
        console.log(this.item)
      }
    }
}
</script>
<style scoped>

</style>