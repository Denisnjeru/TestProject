import Vue from 'vue'
import Router from 'vue-router'
import store from './store/index'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('./views/Home.vue'),
      beforeEnter: (to, from, next) => {
        console.log(store.state)
        if(store.state.User.userType !== 'supplier') {
          next()
        } else {
          next({ name: 'supplier-home' }) 
        }
      }
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('./views/auth/Login.vue')
    },
    {
      path: '/reset-password',
      name: 'reset-password',
      component: () => import('./views/auth/ResetPassword.vue')
    },
    {
      path: '/set-password/:token',
      name: 'set-password',
      component: () => import('./views/auth/SetPassword.vue')
    },
    {
      path: '/update-password/:token',
      name: 'update-password',
      component: () => import('./views/users/UpdatePassword.vue')
    },
    {
      path: '/login-new',
      name: 'login-new',
      component: () => import('./views/auth/LoginNew.vue')
    },
    {
      path: '/user/create',
      name: 'user-create',
      component: () => import('./views/users/CreateUser.vue')
    },
    {
      path: '/profile/:id',
      name: 'profile',
      component: () => import('./views/users/Profile.vue')
    },
    {
      path: '/profile/update/:id',
      name: 'update-profile',
      component: () => import('./views/users/UpdateProfile.vue')
    },
    
  ]
})
