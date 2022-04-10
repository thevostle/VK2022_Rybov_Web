import Vue from 'vue'
import Router from 'vue-router'

import Shop from '@/components/Shop'
import productItem from '@/components/productItem'


Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/catalog',
      name: 'Магазин',
      component: Shop
    },
    {
      path: '/item',
      name: 'item',
      component: productItem
    }
  ]
})
