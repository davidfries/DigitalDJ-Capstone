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
                        <button class="button is-success">Add!</button>

                        </div>
                    </footer>
                </div>
            </form>
        </b-modal>
    </section>
</template>

<script>
const axios = require("axios");
export default {
    name:"AddSong",
    data(){
        return{
            isComponentModalActive: false,
            showModal:true,
            songtitle: "",
            song_key:""
        }
    },
    mounted(){
        let vm=this
        axios.get('http://localhost:5000/newid').then(function(response){
            console.log("new song key "+response.data.id)
            vm.song_key=response.data.id
        })
    },
    methods:{
        addsong:function(){
            
            console.log(this.song_key)
            axios.post('http://localhost:5000/addsong',{
                "room_key":`${localStorage.getItem("room_key")}`,
                "song_key":this.song_key,
                "song_title":this.songtitle

            })
        }
    }
}
</script>