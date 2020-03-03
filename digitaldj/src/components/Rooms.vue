<template>
    <b-table :striped="true" :data="data" :columns="columns">
        <!-- <b-table-column field="join" label="Join" width="40">
                    <router-link :to="{name:'room',params:data.id}">Join Room</router-link>
                    
        </b-table-column> -->


    </b-table>
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