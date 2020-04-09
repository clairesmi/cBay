<template>
  <div id="item-form" class="flex flex-col items-center h-full">
    <h1 class="animated zoomInDown user-form-title text-6xl tracking-wide text-orange-600 mt-10 mb-20">
      Add a new listing! 
    </h1>
    <div class="form-wrapper h-64 w-2/4 flex">
    <form class="flex flex-col w-full justify-around p-40 text-gray-900">
      <label>Name</label>
      <input type="text" placeholder="Product name" v-model="item.name" required="required"/>
      <label>Price</label>
      <input type="number" placeholder="0.00" step="0.01" v-model="item.price" required="required"/>
       <label>Size</label>
      <input type="text" placeholder="Product size" v-model="item.size" required="required"/>
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
      <button class="form-button mt-2" @click="submitClicked">List your Item</button>
    </form>
    </div>
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
<style scoped>
label {
  margin-bottom: 2px;
  margin-top: 5px;
}
</style>