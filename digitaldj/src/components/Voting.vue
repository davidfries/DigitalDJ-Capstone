<template>
    <div class="container">
        <h1>
            Song suggestion goes here
        </h1>
        <h2 class="subtitle">
            {{ count }} votes
        </h2>
        <b-button type="is-primary" inverted icon-right="arrow-up-bold" v-on:click="count++"></b-button>
        <b-button type="is-primary" inverted icon-right="arrow-down-bold" v-on:click="count--"></b-button>
    </div>
</template>

<script>
const axios = require("axios");
const lo = require("lodash");
export default {
    name:"Voting",
    data(){
        return{
            count: "0"
        }
    },
    watch:{
        count: function(){
            this.count="..."
            this.debouncedvote()
        }
    },
    created(){
        this.debouncedvote=lo.debounce(this.sendvote,500)
    },
    methods:{
        sendvote:function(){
            var vm =this;
            axios.post('http://localhost:5000/songvote',{
                "songid":localStorage.getItem("song_key"),
                "roomid":localStorage.getItem("roomid")
            }).catch(function(error){
                console.log(error);
                vm.count="0"
            })
            axios.get(`"http://localhost:5000/getsongvotecount/${localStorage.getItem("songid")}"`).then(resp => {
    //   console.log(resp.data[0].roomname);
      vm.count = resp.data.count;
    });
        }
    },
    mounted(){
        console.log("Roomid from local storage"+localStorage.getItem("roomid"))
        axios.get(`"http://localhost:5000/getsongvotecount/${localStorage.getItem("songid")}"`).then(resp => {
    //   console.log(resp.data[0].roomname);
      this.count = resp.data.count;
    });
    }
}
</script>