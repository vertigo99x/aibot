import { createRouter, createWebHistory } from 'vue-router'

import store from '../store'


import Main from '../views/Main.vue';
import LoginView from '../views/LoginView.vue';

import notFoundvue from '../views/notFoundvue.vue';




const routes = [
    {
        path: '/',
        name: 'main',
        component: Main,
        meta: { requireLogin: false }
    },
   
    {
        path: '/login',
        name: 'login',
        component: LoginView,
        meta: { requireLogin: false }
    },
    {
        path: '/:notFound',
        name: 'notFound',
        component: notFoundvue,
        
           
      },
]


const router = createRouter({
    history: createWebHistory(),
    routes
})


router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requireLogin) && !store.state.refresh) {
        next({ name: 'login', query: { redirect: to.fullPath } });
    } else {
        next();
    }
})

export default router
