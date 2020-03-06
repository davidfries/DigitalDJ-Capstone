<template>
    <b-navbar>
        <template slot="brand">
            <b-navbar-item tag="router-link" :to="{ path: '/' }">
                
            </b-navbar-item>
        </template>
        <template slot="start">
            <b-navbar-item>
                <router-link :to="{name:'home'}">Home</router-link>
            </b-navbar-item>
            <b-navbar-item >
                <router-link :to="{name:'rooms'}">Rooms</router-link>
                </b-navbar-item>
            <b-navbar-dropdown label="Info">
                <b-navbar-item href="#">
                    About
                </b-navbar-item>
                <b-navbar-item href="#">
                    Contact
                </b-navbar-item>
            </b-navbar-dropdown>
        </template>

        <template slot="end">
            <b-navbar-item tag="div">
                <div class="buttons">
                    <a>
                        <register></register>
                    </a>
                    <login></login>
                </div>
            </b-navbar-item>
        </template>
    </b-navbar>
</template>

<script>
import Login from './Login.vue'
import Register from './Register.vue'
export default {
  name: 'Navbar',
  props: {
    username: String
  },
  components:{
      Login,Register
  }
}
</script>
