import Vue from 'vue'
import Router from 'vue-router'
import index from '../pages/index'
import btn from '../pages/pagebtn'
import list from '../pages/pagelist'
import navS from '../pages/pagenav'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/nav',
      name: 'nav',
      component: navS
    },
    {
      path: '/btn',
      name: 'btn',
      component: btn
    },
    {
      path: '/list',
      name: 'list',
      component: list
    }
  ]
})
