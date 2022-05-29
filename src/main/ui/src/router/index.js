import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomePage.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('../views/AboutPage.vue')
  },
  {
    path: '/articles',
    name: 'articles',
    component: () => import('../views/ArticlesPage.vue')
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
