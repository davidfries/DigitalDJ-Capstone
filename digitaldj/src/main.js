import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import VueSession from 'vue-session'
import VueChatScroll from 'vue-chat-scroll'
import Buefy from 'buefy'
// import socketio from 'socket.io-client';
// import VueSocketIO from 'vue-socket.io-extended';
// import 'buefy/dist/buefy.css'
import Rooms from './components/Rooms.vue'
import MainPage from './components/MainPage.vue'
import Room from './components/Room.vue'
import About from './components/About.vue'
import Contact from './components/Contact.vue'
import UserSettings from './components/UserSettings.vue'
// try{
// const socket = socketio('http://localhost:4113');
// Vue.use(VueSocketIO, socket)
// }
// catch{
//   console.log("Can't connect to socket server")
// }


Vue.use(Buefy)
Vue.use(VueRouter)
Vue.use(VueSession)
Vue.use(VueChatScroll)
Vue.config.productionTip = false
const routes = [
  { path: '/rooms', name:"rooms", component: Rooms},
  {path: '/', name:'home', component: MainPage},
  {path: '/room/:room_key', name:'room', component: Room, props:true},
  {path: '/settings', name:'settings', component: UserSettings},
  { path: '/about', name: "about", component: About, props: true },
  { path: '/contact', name: "contact", component: Contact, props: true },

]
const router = new VueRouter({
  routes // short for `routes: routes`
})

new Vue({
  router:router,
  render: h => h(App),
}).$mount('#app')
