import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../components/common/Home.vue";
import ItemsIndex from "../components/items/ItemsIndex.vue";
import ItemNew from "../components/items/ItemNew.vue";
import ItemShow from "../components/items/ItemShow.vue";
import ItemEdit from "../components/items/ItemEdit.vue";
import CategoryShow from "../components/categories/CategoryShow.vue";
import Login from "../components/common/Login.vue";
import Register from "../components/common/Register.vue";
import Profile from "../components/common/Profile.vue";
import ProfileEdit from "../components/common/ProfileEdit.vue";
import ProfileView from "../components/user_interaction/ProfileView.vue";
import Basket from "../components/items/Basket.vue";
import Checkout from "../components/items/Checkout.vue";
import NotFound from "../components/common/NotFound.vue";

Vue.use(VueRouter);

const mode = "history";
const base = process.env.BASE_URL;
const routes = [
  { path: "/checkout", component: Checkout },
  { path: "/basket", component: Basket },
  { path: "/items/new", component: ItemNew },
  { path: "/items/:id/edit", component: ItemEdit },
  { path: "/items/:id/", component: ItemShow, name: "item-show" },
  { path: "/items", component: ItemsIndex },
  {
    path: "/categories/:id/:catName",
    component: CategoryShow,
    name: "category-show"
  },
  { path: "/login", component: Login },
  { path: "/register", component: Register },
  { path: "/profile/edit", component: ProfileEdit },
  { path: "/profile/:id", component: ProfileView },
  { path: "/profile", component: Profile },
  { path: "/", component: Home },
  { path: "/notfound", component: NotFound }
];

const router = new VueRouter({ routes, mode, base });
// console.log(router.options.routes);
export default router;
