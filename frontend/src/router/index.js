import Router from 'vue-router'
import Home from '../components/common/Home.vue'
import ItemsIndex from '../components/items/ItemsIndex.vue'
import ItemNew from '../components/items/ItemNew.vue'
import ItemShow from '../components/items/ItemShow.vue'
import ItemEdit from '../components/items/ItemEdit.vue'
import CategoriesIndex from '../components/categories/CategoriesIndex.vue'
import CategoryShow from '../components/categories/CategoryShow.vue'
import Login from '../components/common/Login.vue'
import Register from '../components/common/Register.vue'
import Profile from '../components/common/Profile.vue'
import ProfileView from '../components/user_interaction/ProfileView.vue'
import Basket from '../components/items/Basket.vue'

const routes = [
  { path: '/basket', component: Basket },
  { path: '/items/new', component: ItemNew },
  { path: '/items/:id/edit', component: ItemEdit },
  { path: '/items/:id/', component: ItemShow },
  { path: '/items', component: ItemsIndex },
  { path: '/categories/:id/', component: CategoryShow },
  { path: '/categories', component: CategoriesIndex },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/profile/:id', component: ProfileView },
  { path: '/profile', component: Profile },
  { path: '/', component: Home }
]

const router = new Router({ routes })
console.log(router.options.routes)
export default router