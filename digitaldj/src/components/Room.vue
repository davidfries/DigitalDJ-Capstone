<template>
    <div class="container has-text-centered">
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
export default {
    name:"Room",
    data(){
      return{
        data:[],
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
      // PULL SONGS FROM DB FOR CURRENT ROOM
      var vm =this
      axios.get('http://localhost:5000/getsongs?room_key='+localStorage.getItem("room_key"))
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