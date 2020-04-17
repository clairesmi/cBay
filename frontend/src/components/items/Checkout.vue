<template>
  <div id="checkout" class="flex flex-col items-center">
    <h1
      class="animated zoomInDown checkout-title text-6xl tracking-wide text-orange-600 mt-10 mb-10"
    >
      Checkout
    </h1>
    <h2 class="total">Total: £{{ total }}</h2>
    <div class="flex justify-center mt-6 w-full">
      <button class="w-1/4 button bg-red-100" @click="makePayment">
        Make Payment
      </button>
    </div>
    <div class="flex justify-center mt-3 w-full">
      <router-link class="flex justify-center w-full" to="/basket"
        ><button class="w-1/4 button bg-red-100">
          Back to Basket
        </button></router-link
      >
    </div>
  </div>
</template>
<script>
import axios from "axios";
import Auth from "../../lib/auth";
import { eventBus } from '../../main';

export default {
  name: "checkout",
  data() {
    return {
      items: [],
      total: "",
      currentUserID: null
    };
  },
  async mounted() {
    this.currentUserID = await Auth.getPayload().sub;
    await this.getItems();
    this.getTotal();
  },
  methods: {
    async getItems() {
      try {
        const res = await axios.get("api/basket");
        this.items = res.data.filter(el => el.basket === this.currentUserID);
      } catch (err) {
        this.$router.push("/notfound");
      }
    },
    getTotal() {
      const priceArray = this.items.map(el => el.price);

      this.total = priceArray
        .reduce((total, current) => total + current, 0)
        .toFixed(2);
    },
    async makePayment() {
      // const userID = Auth.getPayload().sub;
      const items = this.items.map(item => ({
        ...item,
        owner: item.owner,
        purchased: this.currentUserID,
        basket: null,
        categories: item.categories.map(category => category)
      }));
      try {
        await items.map(item =>
          axios.patch(`/api/items/${item.id}/`, { ...item })
        );
        eventBus.emptyBasket()
        this.$router.push("/profile");
      } catch (err) {
        this.$router.push("/notfound");
      }
    }
  }
};
</script>
<style scoped>
.checkout-title {
  font-family: "Pacifico", cursive;
  font-size: 80px;
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
</style>
