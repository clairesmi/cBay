import Vue from 'vue/dist/vue.js'
import Router from 'vue-router'
import App from './components/App.vue'
import router from './router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

Vue.use(Router)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

export const eventBus = new Vue({
  methods: {
    loginCheck() {
      this.$emit('userLoggedIn')
    }
  }
})

new Vue({ render: (createEl) => createEl(App),
  BootstrapVue,
  IconsPlugin,
  router,
  components: { App, Router }
}).$mount('#app')