<template>
  <div id="home" class="h-screen flex flex-col font-sans bg-red-200">
    <div class="title-wrapper h-56 flex justify-center flex items-center">
      <router-link to="/items">
        <h1
          class="cbay-title animated zoomInDown cbay-title tracking-wide text-orange-600"
        >
          cBay
        </h1>
      </router-link>
    </div>
    <div
      class="cbay-description flex justify-center flex items-center text-gray-800 pt-2 pb-2"
    >
      <p>Buy and sell unwanted clothes with cBay! Sign up to get started...</p>
    </div>
    <div class="carousel-wrapper flex flex-col justify-center">
      <div
        class="categories-index flex flex-row items-center justify-center w-screen"
      >
        <button
          id="left-button"
          @click="handleClick"
          class="left-button text-2xl m-10 text-orange-600"
          :disabled="leftButtonDisabled"
        >
          ←
        </button>

        <router-link
          v-if="previousCategory"
          :to="{
            name: 'category-show',
            params: {
              id: this.previousCategory.id,
              catName: this.previousCategory.name
            }
          }"
        >
          <div
            v-if="previousCategory"
            class="previous-category m-4 text-6xl text-gray-800 w-12/12 bg-white p-3 flex flex-col justify-center items-center"
          >
            <img
              :src="this.previousCategory.image"
              :alt="previousCategory.name"
              class="h-48 w-12/12"
            />
            <p class="image-text text-4xl">{{ previousCategory.name }}</p>
          </div>
        </router-link>
        <router-link
          v-if="currentCategory"
          :to="{
            name: 'category-show',
            params: {
              id: this.currentCategory.id,
              catName: this.currentCategory.name
            }
          }"
        >
          <div
            v-if="currentCategory"
            class="current-category m-4 text-6xl text-gray-800 w-12/12 bg-white p-4 flex flex-col justify-center items-center"
          >
            <img
              :src="this.currentCategory.image"
              :alt="currentCategory.name"
              class="h-64 w-12/12"
            />
            <p class="image-text text-4xl">{{ currentCategory.name }}</p>
          </div>
        </router-link>
        <router-link
          v-if="nextCategory"
          :to="{
            name: 'category-show',
            params: {
              id: this.nextCategory.id,
              catName: this.nextCategory.name
            }
          }"
        >
          <div
            v-if="nextCategory"
            class="next-category m-4 text-6xl text-gray-800 w-12/12 bg-white p-3 flex flex-col justify-center items-center"
          >
            <img
              :src="this.nextCategory.image"
              :alt="nextCategory.name"
              class="h-48 w-12/12"
            />
            <p class="image-text text-4xl">{{ nextCategory.name }}</p>
          </div>
        </router-link>

        <button
          id="right-button"
          @click="handleClick"
          class="right-button text-2xl m-10 text-orange-600"
          :disabled="rightButtonDisabled"
        >
          →
        </button>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
// import Auth from "../../lib/auth";
import "animate.css";

export default {
  name: "home",
  data() {
    return {
      categories: null,
      previousCategory: null,
      currentCategory: null,
      nextCategory: null,
      leftButtonDisabled: false,
      rightButtonDisabled: false
    };
  },
  async mounted() {
    await this.getCategories();
    this.mapCarouselCategories();
  },
  methods: {
    async getCategories() {
      try {
        const res = await axios.get("/api/categories");
        this.categories = res.data;
      } catch (err) {
        this.$router.push("/notfound");
      }
    },

    mapCarouselCategories() {
      let i = 1;
      const carouselCategories = this.categories.map((category, index) => ({
        id: index + 1,
        index: index,
        name: category.name,
        image: category.category_image
      }));

      this.carouselCategories = carouselCategories;
      this.currentCategory = this.carouselCategories[i];
      this.previousCategory = this.carouselCategories[i - 1];
      this.nextCategory = this.carouselCategories[i + 1];
    },

    handleClick() {
      // eslint-disable-next-line no-unused-vars
      let timerId;
      let iPrevious = this.previousCategory.index;
      let iCurrent = this.currentCategory.index;
      let iNext = this.nextCategory.index;
      const currCategory = document.querySelector(".current-category");
      timerId = setTimeout(function() {
        currCategory.classList.add("animated", "pulse");
        setTimeout(function() {
          currCategory.classList.remove("animated", "pulse");
        }, 700);
      }, 100);

      if (
        event.target.id === "right-button" &&
        this.currentCategory.index < this.carouselCategories.length - 1 &&
        this.nextCategory.index !== this.carouselCategories.length - 1
      ) {
        this.currentCategory = this.carouselCategories[(iCurrent += 1)];
        this.previousCategory = this.carouselCategories[(iPrevious += 1)];
        this.nextCategory = this.carouselCategories[(iNext += 1)];
      }

      if (
        event.target.id === "left-button" &&
        this.currentCategory.index > 0 &&
        this.previousCategory.index !== 0
      ) {
        this.currentCategory = this.carouselCategories[(iCurrent -= 1)];
        this.previousCategory = this.carouselCategories[(iPrevious -= 1)];
        this.nextCategory = this.carouselCategories[(iNext -= 1)];
      }

      this.nextCategory.index === this.carouselCategories.length - 1
        ? (this.rightButtonDisabled = true)
        : (this.rightButtonDisabled = false);

      this.previousCategory.index === 0
        ? (this.leftButtonDisabled = true)
        : (this.leftButtonDisabled = false);
    }
  }
};
</script>
<style>
@import "../../styles/output.css";

.cbay-title {
  font-family: "Pacifico", cursive;
  font-size: 120px;
}
.cbay-description {
  font-family: "Oswald", sans-serif;
  font-size: 22px;
  letter-spacing: 0.5px;
}
.image-text {
  font-family: "Permanent Marker", cursive;
  /* font-size: 20px; */
}
.right-button {
  font-size: 40px;
}
.left-button {
  font-size: 40px;
}
img {
  height: 200px;
  width: 200px;
}
/* Use scoped css file to only apply css styles to each specific component */

/* Or use import */
/* @import '../../styles/output.css'; */
</style>
