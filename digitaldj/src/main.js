import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Buefy from 'buefy'
import socketio from 'socket.io-client';
import VueSocketIO from 'vue-socket.io';
// import 'buefy/dist/buefy.css'
import Rooms from './components/Rooms.vue'
import MainPage from './components/MainPage.vue'
import Room from './components/Room.vue'
import About from './components/About.vue'
import Contact from './components/Contact.vue'
try{
const SocketInstance = socketio('http://localhost:4113');
Vue.use(VueSocketIO, SocketInstance)
}
catch{
  console.log("Can't connect to socket server")
}


Vue.use(Buefy)
Vue.use(VueRouter)
Vue.config.productionTip = false
const routes = [
  { path: '/rooms', name:"rooms", component: Rooms},
  {path: '/', name:'home', component: MainPage},
  {path: '/room/:room_key', name:'room', component: Room, props:true},
  
  { path: '/about', name: "about", component: About, props: true },
  { path: '/contact', name: "contact", component: Contact, props: true }

]
const router = new VueRouter({
  routes // short for `routes: routes`
})

new Vue({
  router:router,
  render: h => h(App),
}).$mount('#app')
