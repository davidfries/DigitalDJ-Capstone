<template>
  <div class="container has-text-centered">
    <h3>Active Users: {{counter}}</h3>
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
          <td>
            <voting :song_key="row.song_key"></voting>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
const axios = require("axios");

import Voting from "./Voting.vue";
import AddSong from "./AddSong.vue";
import socketio from "socket.io-client";

export default {
  name: "Room",
  props: ["room_key"],
  data() {
    return {
      data: [],
      counter: '0',
      isConnected: false,
      client_key:"",
      columns: [
        {
          field: "song_title",
          label: "Song Title"
        },
        {
          field: "song_key",
          label: "Vote!"
        }
      ]
    };
  },
 destroyed(){
   console.log('destroyed room component')
   const socket = socketio("http://localhost:5000");
   var data ={"room_key":this.room_key,"client_key":this.client_key}
   socket.emit('leave_music_room',data)
 },
  mounted() {
        let vm=this
        // var client_key=''
        // axios.get('http://localhost:5000/newid').then(function(response){
        //     console.log("new song key "+response.data.id)
        //     client_key=response.data.id
        // })
const socket = socketio("http://localhost:5000");
  socket.on("connect",()=>{
    var data = { "room_key": this.room_key, "client_key": socket.id};
    socket.emit("room_connection", data);
    vm.client_key=socket.id
    // vm.client_key=socket.id
  })
    socket.on("new_connection", function(data) {
      this.isConnected = true;
      console.log(data);
    });
    socket.on("message", function(message) {
      console.log(message);
    });
    socket.on("active_clients_counter", function(data) {
      JSON.parse(data).forEach(element => {
        vm.counter=element.count
      });
      
    });
    // console.log(socket.id)
    
    // PULL SONGS FROM DB FOR CURRENT ROOM
    localStorage.setItem("room_key", this.room_key);
    // var vm = this;
    axios
      .get("http://localhost:5000/getsongs?room_key=" + vm.room_key)
      .then(function(response) {
        if (response.data) {
          // console.log(response.data);
          vm.data = response.data;
        }
      });
  },
  components: {
    Voting,
    AddSong
  }
};
</script>