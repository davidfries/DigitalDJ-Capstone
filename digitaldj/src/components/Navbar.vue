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
            
                <b-navbar-item>
                    <router-link :to="{name:'about'}">About</router-link>
                </b-navbar-item>

                <b-navbar-item >                  
                    <router-link :to="{name:'contact'}">Contact</router-link>
                </b-navbar-item>

            </b-navbar-dropdown>
        </template>

        <template slot="end">
            <b-navbar-item tag="div">
                <div class="buttons">
                    <a v-if="!this.$session.exists()">
                        <register></register>
                    </a>
                    <a v-if="!this.$session.exists()">
                        <login></login>
                    </a>
                    <a v-if="this.$session.exists()">
                        <add-room></add-room>
                    </a>
                    <a v-if="this.$session.exists()">
                        <logout></logout>
                    </a>
                </div>
            </b-navbar-item>
        </template>
    </b-navbar>
</template>

<script>
import Login from './Login.vue'
import Register from './Register.vue'
import Logout from './Logout.vue'
import AddRoom from './AddRoom.vue'

export default {
  name: 'Navbar',
  props: {
    username: String
  },
  components:{
      Login,Register,Logout,AddRoom
  }
}
</script>
