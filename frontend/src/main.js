import Vue from "vue";
import VueRouter from "vue-router";
import App from "./App.vue";
import router from "./router";

import "../src/styles/output.css";
import "animate.css";

Vue.use(VueRouter);

export const eventBus = new Vue({
  methods: {
    loginCheck() {
      this.$emit("userLoggedIn");
    },
    updateBasket() {
      this.$emit("basketUpdated");
    },
    removeFromBasket() {
      this.$emit("removedFromBasket");
    },
    calculateBasket(data) {
      this.$emit("calculatedBasket", data);
    },
    emptyBasket() {
      this.$emit('basketIsEmpty')
    }
  }
});

new Vue({
  render: h => h(App),
  router,
  components: { App, VueRouter }
}).$mount("#app");
