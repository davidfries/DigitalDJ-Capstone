<template>
    <div class="container has-text-centered">
            <h3 v-if="isConnected">Connected to socket server!</h3>
            <AddSong></AddSong>

            <table class="table">
              <thead>
              <tr>
                <th>Song Title</th>
                <th>Vote!</th>

              </tr>
              </thead>
              <tbody>
                <tr v-for="row in data" :key="row.id">
                  <td>{{row.song_title}}</td>
                  <td><voting :song_key=row.song_key></voting></td>


                </tr>


              </tbody>






            </table>
            
        
    </div>
</template>

<script>
const axios = require("axios");

import Voting from './Voting.vue'
import AddSong from './AddSong.vue'
import socketio from 'socket.io-client';
const socket = socketio('http://localhost:4113');

export default {
    name:"Room",
    props:["room_key"],
    data(){
      return{
        data:[],
        isConnected:false,
        columns:[{
          "field":"song_title",
          "label":"Song Title"
        },
        {
            "field":"song_key",
            "label":"Vote!"
        }]
      }
    },
    
    mounted(){
      socket.on("new_connection",function(data){
  this.isConnected=true;
  console.log(data)
})
      socket.emit('room_connection',{"room_key":this.room_key})
      // PULL SONGS FROM DB FOR CURRENT ROOM
      localStorage.setItem("room_key",this.room_key)
      var vm =this
      axios.get('http://localhost:5000/getsongs?room_key='+vm.room_key)
      .then(function(response){
        if(response.data){
          console.log(response.data)
          vm.data=response.data
        }
        
      })
    },
    components:{
      Voting,AddSong
    }
}
</script>