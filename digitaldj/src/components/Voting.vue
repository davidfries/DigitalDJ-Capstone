<template>
    <div class="container">
        <!-- <h1>
            Song suggestion goes here
        </h1> -->
        <h2>
            {{ count }} votes
        </h2>
        <b-button type="is-primary" inverted icon-right="arrow-up-bold" @click="processvote(1)"></b-button>
        <b-button type="is-primary" inverted icon-right="arrow-down-bold" @click="processvote(-1)"></b-button>
    </div>
</template>

<script>
const axios = require("axios");
const lo = require("lodash");
export default {
    name:"Voting",
     props:[
        'song_key'
    ],
    data(){
        return{
            count: "0",
            vote_status:"0"
            // song_key:""
        }
    },
    // watch:{
    //     count: function(){
    //         this.count="..."
            
    //     }
    // },
    created(){
        this.debouncedvote=lo.debounce(this.sendvote,500)
    },
    methods:{
        sendvote:function(){
            var vm =this;
            axios.post('http://localhost:5000/songvote',{
                "song_key":vm.song_key,
                "room_key":localStorage.getItem("room_key"),
                "vote_status":vm.vote_status
            })
            .then(function(){
                axios.get(`http://localhost:5000/getsongvotecount?song_key=${vm.song_key}`)
            .then(function(resp) {
                vm.count=resp.data[0].count
            })

            })
            
            .catch(function(error){
                console.log(error);
                vm.count="0"
            })
            
    //   console.log(resp.data[0].roomname);
     
  
        },
        processvote:function(vote_status){
            var vm =this;
            if(vote_status===1){
                // this.count++;
                this.vote_status="1";
                this.debouncedvote()
                // console.log("after deb")
                
                axios.get(`http://localhost:5000/getsongvotecount?song_key=${vm.song_key}`)
            .then(function(resp) {
                vm.count=resp.data[0].count
            })
            }
            else if(vote_status===-1){
                // this.count--;
                this.vote_status="-1";
                 this.debouncedvote()
                axios.get(`http://localhost:5000/getsongvotecount?song_key=${vm.song_key}`)
            .then(function(resp) {
                vm.count=resp.data[0].count
            })
            }

        }
    },
    mounted(){
        // console.log(`http://localhost:5000/getsongvotecount?song_key=${this.song_key}`)
        console.log("Roomid from local storage"+localStorage.getItem("room_key"))
        axios.get(`http://localhost:5000/getsongvotecount?song_key=${this.song_key}`).then(resp => {
    //   console.log(resp.data[0].roomname);
        
      this.count = resp.data[0].count;
    });
    }
   
}
</script>