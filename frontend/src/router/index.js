import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'

const routerOptions = [
  { path: '/', component: 'Home' },
  { path: '/about', component: 'About' }
]
const route = routerOptions.map(route => {
  // let router;
  return {
    // eslint-disable-next-line no-undef
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})

Vue.use(Router)

export default new Router({
  route,
  mode: 'history'
  // routes: [
  //   {
  //     path: '/',
  //     name: 'HelloWorld',
  //     component: HelloWorld
  //   }
  // ]
})
