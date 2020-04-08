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
                <td><router-link class="button is-warning" :to="{name:'chat',params:{id:row.id}}">Join Room</router-link></td>
            </tr>

        </tbody>
    </table>

    <div class = "newButton">
        <b-button class="button1"><router-link :to="{name:'newroom'}">Create a New Room</router-link></b-button>
    </div>
        
    


</div>



    <!-- <b-table :striped="true" :data="data" :columns="columns">
         <b-table-column field="join" label="Join" width="40">
                    <router-link :to="{name:'room',params:data.id}">Join Room</router-link>
                    
        </b-table-column> 


     </b-table> -->
</template> 

<script>

export default {
    name:'Rooms',
    data(){
        return{
            // pass data as json object
            data:[{
                "id":1,'room_name':"Room1",'listeners':16,'genre':'Classic Rock'
            },
            {
                "id":2,'room_name':"Room2",'listeners':7,'genre':'Hard Rock'
            }
            
            ],
            // name of columns of table, json header name
            columns:[{
                field:'id',
                label:'ID',
                numeric:true
            },
            {
                field:'room_name',
                label: 'Room Name'
            },
            {
                field:'listeners',
                label: 'Number of Listeners',
                numeric:true
            },
            {
                field:'genre',
                label:"Genre"

            },
            {
                field:'join',
                label:'Join'
            }

            ]
        }
    }
}
</script>


<style>
.newButton{
    position: absolute;
    right: 30px;
    top: 50px;       
}

.button1{
    font-size: 3em;  
}
</style>