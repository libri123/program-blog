import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomePage.vue'
import AboutView from '../views/AboutPage.vue'
import ArticalesView from '../views/ArticlesPage.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },
  {
    path: '/articles',
    name: 'articles',
    component: ArticalesView
  },
  {
    path: '/article/:id',
    name: 'singleArticle',
    component: () => import('../views/SingleArticle.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
