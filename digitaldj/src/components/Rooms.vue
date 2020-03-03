<template>
    <b-table :striped="true" :data="data" :columns="columns"></b-table>
</template>

<script>
export default {
    name:'Rooms',
    data(){
        return{
            // pass data as json object
            data:[{
                "id":1,'room_name':"Room1",'listeners':16,'genre':'Classic Rock'
            }],
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

            }
            ]
        }
    }
}
</script>