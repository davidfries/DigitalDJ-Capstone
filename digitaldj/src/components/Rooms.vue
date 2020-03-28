<template>
  <div>
    <table class="container is-fluid table">
      <thead>
        <tr>
          <th>Room Name</th>
          <th>Listeners</th>
          <th>Genre</th>
          <th>Join</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="row in data" :key="row.id">
          <td>{{row.room_name}}</td>
          <td>{{row.listeners}}</td>
          <td>{{row.genre}}</td>
          <td>
            <router-link class="button is-warning" :to="{name:'room',params:{id:row.id}}">Join Room</router-link>
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
      // name of columns of table, json header name
      columns: [
        {
          field: "id",
          label: "ID",
          numeric: true
        },
        {
          field: "room_name",
          label: "Room Name"
        },
        {
          field: "listeners",
          label: "Number of Listeners",
          numeric: true
        },
        {
          field: "genre",
          label: "Genre"
        },
        {
          field: "room_security",
          label: "Security"
        },
        {
          field: "join",
          label: "Join"
        }
      ]
    };
  },
  mounted() {
    axios.get("http://localhost:5000/rooms").then(resp => {
      console.log(resp.data[0].roomname);
      this.data = resp.data;
    });
  }
};
</script>