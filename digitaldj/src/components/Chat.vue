<template>
    <section>
        <!--
        <div class = "container">
        <span>Multiline message is:</span>
        <p style="white-space: pre-line;">{{ message }}</p>
        <br>
        <textarea v-model="message" placeholder="add multiple lines"></textarea>
        </div>
        -->
        <div class = "card">
            <div class="card-content">
                <div class="messages" v-chat-scroll="{always: false, smooth: true}">
                    <div v-for="message in messages" :key="message.id">
                        <span class="text-info">[{{ message.user }}]: </span>
                        <span>{{message.message}}</span>
                        <!--<span class="text-secondary time">{{message.timestamp}}</span>-->
                    </div>
                </div>
            </div>

            <footer class="card-footer">
                <form @submit.prevent="send">
                    <b-field>
                        <b-input
                            v-model="message"
                            :value="message"
                            placeholder="Send message"
                            maxlength="200"
                            type="textarea">
                        </b-input>
                    </b-field>
                    <b-button class="button is-primary" @click="processmessage(message)">Send</b-button>
                </form>
            </footer>
        </div>
    </section>
</template>




<script>
const axios = require("axios");
const lo = require("lodash");
export default {
    name:"Chat",
    data(){
        return{
            messages:[],
            message: "",
            sender: ""
        }
    },
    created(){
        this.debouncedmessage=lo.debounce(this.sendmessage,500)
    },
    methods:{
        sendmessage:function(){
            let vm = this
            if(this.$session.exists()){
                vm.sender = this.$session.get('email')
            }
            //console.log(vm.sender)
            //console.log(vm.room)
            //console.log(vm.message)
            axios.post('http://localhost:5000/chat', {
                "message":vm.message, 
                "sender":vm.sender, 
                "room":localStorage.getItem("room_key")
            })
            .then(function(){
                axios.get(`http://localhost:5000/chat`)
                .then(function(response){
                    vm.messages = response.data
                })
            })
            .catch(function(error){
                console.log(error);
            })
        },
        processvote:function(msg){
            let vm = this
            this.message = msg
            this.debouncedmessage
            axios.get(`http://localhost:5000/chat`)
                .then(function(response){
                    vm.messages = response.data
                })
        }
    },
    mounted(){
        axios.get(`http://localhost:5000/chat`)
                .then(resp => {
                    this.messages = resp.data
                })
    }
}
</script>