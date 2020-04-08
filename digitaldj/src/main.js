import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Buefy from 'buefy'
// import 'buefy/dist/buefy.css'
import Rooms from './components/Rooms.vue'
import MainPage from './components/MainPage.vue'
import Room from './components/Room.vue'
import About from './components/About.vue'
import Contact from './components/Contact.vue'
import Chat from './components/Chat.vue'
import NewRoom from './components/NewRoom.vue'

Vue.use(Buefy)
Vue.use(VueRouter)
Vue.config.productionTip = false
const routes = [
  { path: '/rooms', name:"rooms", component: Rooms, props:true },
  {path: '/', name:'home', component: MainPage},
  {path: '/room/:id', name:'room', component: Room, props:true},
  { path: '/about', name: "about", component: About, props: true },
  { path: '/contact', name: "contact", component: Contact, props: true },
  { path: '/chat', name: "chat", component: Chat, props: true },
  { path: '/newroom', name: "newroom", component: NewRoom, props: true }

]
const router = new VueRouter({
  routes // short for `routes: routes`
})

new Vue({
  router:router,
  render: h => h(App),
}).$mount('#app')
