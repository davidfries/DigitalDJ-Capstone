import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Buefy from 'buefy'
// import 'buefy/dist/buefy.css'
import Rooms from './components/Rooms.vue'

Vue.use(Buefy)

Vue.config.productionTip = false
const routes = [
  { path: '/rooms', name:"rooms", component: Rooms }
]
const router = new VueRouter({
  routes // short for `routes: routes`
})

new Vue({
  
  render: h => h(App),
}).$mount('#app')
Vue.use(router)