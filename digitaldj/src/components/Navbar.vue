<template>
    <b-navbar>
        <template slot="brand">
            <b-navbar-item tag="router-link" :to="{ path: '/' }">
                <img src="favicon-96x96.png">
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
                    <a v-if="!isLoggedIn">
                        <register></register>
                    </a>
                    <a v-if="!isLoggedIn">
                        <login></login>
                    </a>
                    <a v-if="isLoggedIn">
                        <add-room></add-room>
                    </a>
                    <a v-if="isLoggedIn">
                        <b-button tag="router-link" :to="{name: 'settings'}" class="button is-primary">
                            Settings
                        </b-button>
                    </a>
                    <a v-if="isLoggedIn">
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
  },
  computed:{
      isLoggedIn:function(){
          return (this.$session.exists() && this.$session.get('loggedIn'))
      }
  }
}
</script>
