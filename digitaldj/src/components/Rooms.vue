<template>
  <div>
    <table class="container table">
      <thead>
        <tr>
          <th>Room Name</th>
          <th>Max Quantity</th>
          <th>Genre</th>
          <th>Join</th>
        </tr>
      </thead>
      <tbody>
          <!-- these need to match the fields below in column setup -->
        <tr v-for="row in data" :key="row.id">
          <td>{{row.room_name}}</td>
          <td>{{row.max_quantity}}</td>
          <td>{{row.genre}}</td>
          <td>
            <router-link id="join" class="button is-warning" :to="{name:'room',params:{room_key:row.room_key}}">Join Room</router-link>
          </td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- <b-table :striped="true" :data="data" :columns="columns">
         <b-table-column field="join" label="Join" width="40">
                    <router-link :to="{name:'room',params:data.id}">Join Room</router-link>
                    
        </b-table-column> 


  </b-table>-->
</template> 

<script>
const axios = require("axios");

// console.log(allrooms)
export default {
  name: "Rooms",
  data() {
    return {
      // pass data as json object
      data: [],
      room_key:localStorage.getItem("room_key"),
      // name of columns of table, json header name
      
    };
  },
  methods:{
    setstorage:function(id){
      console.log("setting roomid local storage...")
      localStorage.setItem("room_key",id)
      // console.log(localStorage.getItem("room_key"))
      
    }
  },
  mounted() {
    axios.get("http://localhost:5000/rooms").then(resp => {
      // console.log(resp.data[0].max_quantity);
      this.data = resp.data;
    });
  }
};
</script>