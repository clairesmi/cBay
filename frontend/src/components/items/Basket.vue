<template>
  <div id="basket" class="flex flex-col items-center h-screen bg-red-200">
    <div class="basket-headers flex flex-col items-center h-full bg-red-200">
      <h1
        class="animated zoomInDown basket-title text-6xl tracking-wide text-orange-600 mt-10"
      >
        What's in your basket?
      </h1>
    </div>
    <div
      class="basket-wrapper w-2/5 flex-col justify-center pb-5 text-gray-900 bg-red-200 h-full"
      v-if="items.length"
    >
      <div
        class="item-info flex justify-start items-center bg-white mb-2"
        v-for="item in items"
        :key="item.id"
      >
        <div>
          <router-link :to="`/items/${item.id}/`">
            <img :src="item.image" alt="item-image" class="item-image mr-10" />
          </router-link>
        </div>
        <div>
          <h3>{{ item.name }}</h3>
          <p>${{ item.price }}</p>
          <p>Size: {{ item.size }}</p>
          <router-link v-if="item.owner" :to="`/profile/${item.owner.id}/`">
            <h4 v-if="item.owner" class="flex">
              Listed by:
              <p class="detail-link detail pl-1">{{ item.owner.username }}</p>
            </h4>
          </router-link>
          <button class="button" @click="removeCheck" :id="item.id">
            Remove from basket
          </button>
        </div>
      </div>
    </div>
    <div
      v-else
      class="basket-empty flex flex-col items-center h-full text-gray-900 bg-red-200"
    >
      <h1>Your basket is empty...</h1>
      <router-link to="/items">
        <p class="basket-empty-link">Go back to listings</p>
      </router-link>
    </div>
    <div
      class="flex flex-col w-full flex justify-center items-center bg-red-200 pb-12"
    >
      <h2
        class="total flex justify-center items-center p-2 pl-5 pr-5 text-gray-900 w-2/4"
      >
        <p>Total: ${{ total }}</p>
        <router-link
          v-if="items.length"
          to="/checkout"
          class="flex flex-col justify-center items-center w-2/4"
        >
          <button class="button w-2/4 bg-red-100 text-gray-900">
            Go to checkout
          </button>
        </router-link>
      </h2>
    </div>
    <div v-if="modalShow">
      <div class="check-modal" @click="modalShow = false">
        <div
          class="modal-text flex bg-white flex flex-col justify-around items-center text-orange-600 pl-5"
        >
          <div
            class="flex w-full h-full justify-end items-start pt-5 pr-5 text-gray-800"
          >
            <button
              class="button flex justify-start items-start h-10"
              @click="modalShow = false"
            >
              <p class="h-5 text-lg mb-1">X</p>
            </button>
          </div>
          <p class="pb-20">
            Are you sure you want to remove this item from your basket?
          </p>
          <div class="mb-20 text-gray-800 pb-3">
            <button
              class="button text-gray-900 mr-2"
              @click="handleRemove"
              :id="item.id"
            >
              Yes
            </button>
            <button
              class="button text-gray-900 ml-2"
              @click="handleRemove"
              :id="item.id"
            >
              No
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import { eventBus } from "../../main";
// import Auth from "../../lib/auth";

export default {
  name: "basket",
  data() {
    return {
      items: {},
      modalShow: false,
      item: {},
      total: null
    };
  },

  async mounted() {
    await this.getBasket();
    this.calculateTotal();
    // console.log(Auth.getPayload().sub)
  },
  methods: {
    async getBasket() {
      const res = await axios.get("/api/basket");
      this.items = res.data;
      // .filter(item => item.basket === Auth.getPayload().sub)
      console.log(this.items);
      // console.log(this.items
      // .filter(item => item.basket === Auth.getPayload().sub))
    },
    async removeCheck() {
      const res = await axios.get(`api/items/${event.target.id}/`);
      this.item = res.data;
      this.modalShow = !this.modalShow;
    },
    async handleRemove() {
      if (event.target.innerText === "No") {
        this.modalShow = !this.modalShow;
      } else {
        const owner = this.item.owner;
        this.total -= this.item.price;
        const item = {
          ...this.item,
          basket: null,
          available: true,
          owner: owner.id,
          categories: this.item.categories.map(category => category.id)
        };
        this.item = item;
        try {
          await axios.patch(`/api/items/${this.item.id}/`, this.item);
          this.getBasket();
        } catch (err) {
          this.$router.push("/notfound");
        }
      }
      eventBus.removeFromBasket();
    },
    calculateTotal() {
      const priceArray = this.items.map(item => item.price);
      this.total = priceArray
        .reduce((total, current) => total + current, 0)
        .toFixed(2);
    }
  },
  created() {
    eventBus.$on("userLoggedIn", () => {
      eventBus.calculateBasket(this.items.length);
    });
  }
};
</script>
<style scoped>
.basket-title {
  font-family: "Pacifico", cursive;
  font-size: 80px;
}
.basket-wrapper {
  font-family: "Oswald", sans-serif;
  font-size: 20px;
}
.basket-empty {
  font-family: "Oswald", sans-serif;
  font-size: 40px;
}
.basket-empty-link {
  text-decoration: underline;
  font-size: 25px;
}
.basket-empty-link:hover {
  color: #dd6b33;
  transform: scale(1.02);
}
img {
  height: 200px;
  width: 200px;
}
.button {
  margin-top: 5px;
  padding: 5px 8px;
  box-shadow: 1px 1px 10px 1px gray;
  font-family: "Oswald", sans-serif;
}
.button:hover {
  transform: scale(0.98);
  color: #dd6b33;
}
.total {
  font-family: "Oswald", sans-serif;
  font-size: 20px;
}
.detail-link:hover {
  color: #dd6b33;
}
.check-modal {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  width: 100vw;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.modal-text {
  box-shadow: 1px 1px 10px 1px gray;
  font-family: "Pacifico", cursive;
  font-size: 30px;
  width: 50vw;
  height: 50vh;
  opacity: 1;
}
</style>
