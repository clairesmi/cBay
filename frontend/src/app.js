import Vue from 'vue/dist/vue.js'
import Router from 'vue-router'
import App from './components/App.vue'
import router from './router'
// import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(Router)
// Vue.use(BootstrapVue)
// Vue.use(IconsPlugin)

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