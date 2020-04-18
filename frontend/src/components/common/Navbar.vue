<template>
  <div id="navbar" class="text-gray-800 bg-red-200">
    <nav
      toggleable="sm"
      type="light"
      variant="light"
      class="flex flex-row justify-between pl-5 pr-5 pt-2"
    >
      <router-link to="/">Home</router-link>
      <div v-if="isLoggedIn" class="link-wrapper flex flex-row">
        <div class="pr-3">
          <router-link to="/items">Go to Listings</router-link>
        </div>
        <div class="pr-3">
          <router-link to="/items/new">New Listing</router-link>
        </div>
        <div class="pr-3">
          <router-link to="/profile">Your Profile</router-link>
        </div>
        <div class="pr-5 pl-2">
          <router-link to="/basket">
            <div
              class="flex justify-center items-center basket-count text-xs bg-orange-600"
            >
              <p class="text-white">{{ itemsInBasket }}</p>
            </div>
            <p class="text-xl">🛒</p>
          </router-link>
        </div>
        <div class="text-orange-600 pr-3">
          <a @click="handleLogout">Logout</a>
        </div>
      </div>
      <div v-if="!isLoggedIn" class="link-wrapper flex flex-row">
        <div class="pr-3">
          <router-link to="/register">Sign Up</router-link>
        </div>
        <div class="pr-3">
          <router-link to="/login">Login</router-link>
        </div>
      </div>
    </nav>
  </div>
</template>
<script>
import Auth from "../../lib/auth";
import { eventBus } from "../../main";

export default {
  name: "navbar",
  data() {
    return {
      isLoggedIn: null,
      itemsInBasket: 0
    };
  },
  methods: {
    handleLogout() {
      Auth.logout();
      this.isLoggedIn = this.isAuth();
      this.$router.push("/items");
    },
    isAuth() {
      return Auth.isAuthenticated();
    }
  },
  created() {
    // when the userLoggedIn event is emitted from the event bus, execute this.isAuth
    eventBus.$on("userLoggedIn", () => {
      this.isLoggedIn = this.isAuth();
    }),
      eventBus.$on("basketUpdated", () => {
        this.itemsInBasket += 1;
      }),
      eventBus.$on("removedFromBasket", () => {
        this.itemsInBasket -= 1;
      }),
      eventBus.$on("calculatedBasket", data => {
        this.itemsInBasket = data;
      });
    eventBus.$on("basketIsEmpty", () => {
      this.itemsInBasket = 0;
    });
  }
};
</script>
<style scoped>
#navbar {
  font-family: "Oswald", sans-serif;
  font-size: 20px;
  text-decoration: underline;
}
a:hover {
  cursor: pointer;
}
.basket-count {
  margin-bottom: -15px;
  /* background: orange; */
  border-radius: 50%;
  color: white;
  height: 15px;
  width: 15px;
}
</style>
