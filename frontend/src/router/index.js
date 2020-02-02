import Router from 'vue-router'
import Home from '../components/common/Home.vue'
import ItemsIndex from '../components/items/ItemsIndex.vue'
import ItemForm from '../components/items/ItemForm.vue'
import ItemShow from '../components/items/ItemShow.vue'

const routes = [
  { path: '/items/new', component: ItemForm },
  { path: '/items/:id/', component: ItemShow },
  { path: '/items', component: ItemsIndex },
  { path: '/', component: Home }
]

const router = new Router({ routes })
console.log(router.options.routes)
export default router