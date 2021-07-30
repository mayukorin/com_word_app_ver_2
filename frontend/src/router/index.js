import Vue from "vue";
import VueRouter from "vue-router";
import SentenceView from "@/components/templates/SentenceView";
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "SentenceView",
    component: SentenceView,
  },
];

const router = new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL,
  routes,
});

export default router;
