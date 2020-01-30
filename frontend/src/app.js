import Vue from 'vue/dist/vue.js'
import Router from 'vue-router'
import App from './components/App.vue'
import router from './router'

Vue.use(Router)
Vue.config.productionTip = false

new Vue({ render: (createEl) => createEl(App),
  router,
  components: { App, Router }
}).$mount('#app')

