import Vue from 'vue/dist/vue.js'
import Router from 'vue-router'
import App from './components/App.vue'
import router from './router'

Vue.use(Router)

export const eventBus = new Vue({
  methods: {
    loginCheck() {
      this.$emit('userLoggedIn')
    },
    updateBasket() {
      this.$emit('basketUpdated')
    },
    removeFromBasket() {
      this.$emit('removedFromBasket')
    },
    calculateBasket(data) {
      this.$emit('calculatedBasket', data)
    }
  }
})

new Vue({ render: (createEl) => createEl(App),
  // BootstrapVue,
  // IconsPlugin,
  router,
  components: { App, Router }
}).$mount('#app')