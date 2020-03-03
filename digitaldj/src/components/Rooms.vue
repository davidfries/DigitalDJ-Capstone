<template>
    <b-table :striped="true" :data="data" :columns="columns"></b-table>
</template>

<script>
export default {
    name:'Rooms',
    data(){
        return{
            // pass data as json object
            data:[],
            // name of columns of table, json header name
            columns:[]
        }
    }
}
</script>