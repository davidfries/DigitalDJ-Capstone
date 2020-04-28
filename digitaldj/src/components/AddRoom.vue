<template>

    <section>
        
        <button id="reg" class="button is-primary"
            @click="isComponentModalActive = true">
            Add Room
        </button>

        <b-modal :active.sync="isComponentModalActive"
                 has-modal-card
                 trap-focus
                 aria-role="dialog"
                 aria-modal>
            <!-- <Login v-bind="formProps"></Login> -->
            <form action="" @submit="addroom">
                <div class="modal-card" style="width: auto">
                    <header class="modal-card-head">
                        <p class="modal-card-title">Add Room</p>
                    </header>
                    <section class="modal-card-body">
                        <b-field label="Room Name">
                            <b-input
                                v-model="room_name"
                                type="text"
                                :value="room_name"
                                placeholder="David's Room"
                                required>
                            </b-input>
                        </b-field>

                        <b-field label="Genre">
                            <b-input
                                v-model="genre"
                                type="text"
                                :value="genre"
                                placeholder="Pop/Rock"
                                required>
                            </b-input>
                        </b-field>

                        

                        <b-field label="Max Listeners">
                            <b-input
                                v-model="max_listeners"
                                type="number"
                                id="confirmPassword"
                                :value="max_listeners"
                                min="2"
                                max="32" 
                                placeholder="8"
                                required>
                            </b-input>
                        </b-field>

                        <b-checkbox
                        v-model="security"
                        :value="security"
                        required
                        >Private?</b-checkbox>
                    </section>
                    <footer class="modal-card-foot">
                        <!-- <button class="button" type="button" @click="$parent.close()">Close</button> -->
                        <div class="container has-text-centered">
                        <button class="button is-primary" @click="isComponentModalActive=false">Create Room!</button>

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
    name:"AddRoom",
    data(){
        return {
            isComponentModalActive: false,
            showModal:true,
            room_name: "",
            genre: "",
            max_listeners: "",
            security:"0"
        }
    },
    methods:{
        addroom:function(){
            var data={
                "room_name":this.room_name,
                "genre":this.genre,
                "security":this.security,
                "max_listeners":this.max_listeners
            }
        axios.post('http://localhost:5000/addroom',data).then(function(response){
            console.log(response)
        })
        

        
    
}}}
</script>
