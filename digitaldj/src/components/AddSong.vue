<template>
    <section>
        <button class="button is-danger"
            @click="isComponentModalActive = true">
            Suggest Song
        </button>

        <b-modal :active.sync="isComponentModalActive"
                 has-modal-card
                 trap-focus
                 aria-role="dialog"
                 aria-modal>
            <!-- <Login v-bind="formProps"></Login> -->
            <form action="" @submit="addsong">
                <div class="modal-card" style="width: auto">
                    <header class="modal-card-head">
                        <p class="modal-card-title">Suggest a Song</p>
                    </header>
                    <section class="modal-card-body">
                        <b-field label="song">
                            <b-input
                                v-model="songtitle"
                                type="text"
                                :value="songtitle"
                                placeholder="Enter song title..."
                                required>
                            </b-input>
                        </b-field>

                        
                    </section>
                    <footer class="modal-card-foot">
                        <!-- <button class="button" type="button" @click="$parent.close()">Close</button> -->
                        <div class="container has-text-centered">
                        <button class="button is-success" @click="isComponentModalActive=false">Add!</button>

                        </div>
                    </footer>
                </div>
            </form>
        </b-modal>
    </section>
</template>

<script>
import socketio from "socket.io-client";
const axios = require("axios");

export default {
    name:"AddSong",
    data(){
        return{
            isComponentModalActive: false,
            showModal:true,
            songtitle: ""
            // song_key:""
        }
    },
    created(){
        let vm=this
        axios.get('https://api.digitaldj.live/newid').then(function(response){
            // console.log("new song key "+response.data.id)
            vm.song_key=response.data.id
        })
    },
    methods:{
        addsong:function(){
            const socket = socketio("https://api.digitaldj.live");
            console.log(localStorage.getItem("room_key"))
            // console.log(this.song_key)
            axios.post('https://api.digitaldj.live/addsong',{
                "room_key":`${localStorage.getItem("room_key")}`,
                // "song_key":this.song_key,
                "song_title":this.songtitle

            }).then(function(response){
                localStorage.setItem("song_key",response.data.song_key)
            })
            this.songtitle=""
            var data={"room_key":`${localStorage.getItem("room_key")}`}
            socket.emit("update_songs",data)
        }
    }
}
</script>