<template>
  <div id="item-form">
    <router-link to="/">Home</router-link>
    <form>
      <label>Name</label>
      <input type="text" placeholder="Product name" v-model="item.name"/>
      <label>Price</label>
      <input type="number" placeholder="0.00" step="0.01" v-model="item.price"/>
       <label>Size</label>
      <input type="text" placeholder="Product size" v-model="item.size"/>
      <!-- sep component -->
      <label>Image</label>
      <image-upload v-on:image-upload="item.image = $event"></image-upload>
      <label>Categories</label>
        <div>
          <multiselect @input="multiSelectInput"
            v-model="updatedValue"
            :options="categories"
            :multiple="true"
            track-by="name"
            label="name"
            placeholder="Select item categories">
              <template slot="singleLabel" slot-scope="{ option }">{{ option.name }}</template>
          </multiselect>
            <pre class="categories-chosen"><code>{{ value ? value.name: null }}</code></pre>
        </div>
      <button @click="submitClicked">List your Item</button>
    </form>
  </div>
</template>

<script>
// import external libraries
import Multiselect from 'vue-multiselect'
// import child components here 
import ImageUpload from './ImageUpload.vue'

export default {
  name: "item-form",
// register imported components here so they can be used in the render/template
  components: {
    ImageUpload, Multiselect
  },
  props: {
    item: Object,
    categories: Array,
    value: Array
  },

  data() {
    return {
      // make a copy of value which can be emitted to the parent
      updatedValue: this.$props.value
    }
  },

  methods: {
    submitClicked() {
      this.$emit("submit-clicked")
    },
    multiSelectInput() {
      //  emit the new values from the multi-select to the parent 
      this.$emit("multi-select-input", this.updatedValue)
    }
  }

}

</script>