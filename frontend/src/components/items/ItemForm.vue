<template>
  <div id="item-form" class="h-screen flex flex-col items-center bg-red-200">
    <h1 class="animated zoomInDown user-form-title text-6xl tracking-wide text-orange-600 mb-24">
      {{ $route.path.includes('new') ? 'Add a new listing!' : 'Update your listing!' }}
    </h1>
    <div class="form-wrapper h-full w-2/4 flex bg-red-200">
    <form class="flex flex-col w-full justify-around p-40 text-gray-900 bg-red-200">
      <label>Name</label>
      <input type="text" placeholder="Product name" v-model="item.name" required="required"/>
      <label>Price</label>
      <input type="number" placeholder="0.00" step="0.01" v-model="item.price" required="required"/>
       <label>Size</label>
      <input type="text" placeholder="Product size" v-model="item.size" required="required"/>
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
      <button class="form-button mt-2 bg-red-200" @click.prevent="submitClicked">List your Item</button>
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
      console.log(this.$route.path.includes('add'))
    }
  }

}

</script>
<style scoped>
label {
  margin-bottom: 2px;
}
</style>