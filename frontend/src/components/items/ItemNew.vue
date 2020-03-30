<template>
  <div id="item-new">
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
// import external libraries
import axios from 'axios'
import ItemForm from '../items/ItemForm.vue'
// import child components here 

export default {
  name: "item-new",
// register imported components here so they can be used in the render/template
  components: {
    ItemForm
  },

  data () {
    return {
      item: {
        name: '',
        price: '',
        size: '',
        available: true,
        image: '',
      },
      categories: [],
      value: null
    }
  },

  mounted () {
    this.getCategories()
  },

  methods: {

     async getCategories() {
       try {
      const res = await axios.get('/api/categories')
      this.categories = res.data
       }
       catch (err) {
         console.log(err)
       }
    },

    handleMultiSelect(updatedValue) {
      // console.log(value)
      if (!updatedValue) {
        return this.item = {...this.item, categories: []}
      }
      this.item = {...this.item, categories: updatedValue.map(val => val.id)}
      // console.log(this.item)
    },

    async handleSubmit () {
      // console.log('submitted')
      console.log(this.item)

      try {
        await axios.post("/api/items", this.item)
        this.$router.push('/profile')
      }
      catch (error) {
        console.log(error)
      }
    }
  }
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style scoped></style>

