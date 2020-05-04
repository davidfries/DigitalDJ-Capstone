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
                <div class="content" v-chat-scroll="{always: false, smooth: true}">
                    <div v-for="message in chat_data" v-bind:key="message.message_id">
                        <br>
                        <div v-if="fromCurrentUser(message.sender)">
                            <span class="right">{{message.sender}}:</span>
                            <br>
                            <span class="right pad message">{{message.message}}</span>
                        </div>
                        <div v-else>
                            <span class="left">{{message.sender}}:</span>
                            <br>
                            <span class="left pad message">{{message.message}}</span>
                        </div>
                        <br>
                    </div>
                </div>
            </div>

            <footer class="card-footer">
                <form v-if="this.$session.exists()" @submit.prevent="processmessage(message)">
                    <b-field class="left pad">
                        <b-input
                            v-model="message"
                            :value="message"
                            placeholder="Send message"
                            maxlength="200"
                            type="text">
                        </b-input>
                    </b-field>
                    <b-button class="send button right is-danger" @click="processmessage(message)">Send</b-button>
                </form>
                <form v-if="!this.$session.exists()" @submit.prevent="tempuser(nickname)">
                    Please enter a nickname:
                    <b-field class="left pad">
                        <b-input
                            v-model="nickname"
                            :value="nickname"
                            placeholder="Nickname"
                            maxlength="20"
                            type="text">
                        </b-input>
                    </b-field>
                    <b-button class="send button right is-danger" @click="tempuser(nickname)">Set Name</b-button>
                </form>
            </footer>
        </div>
    </section>
</template>




<script>
import socketio from "socket.io-client";
const axios = require("axios");
const lo = require("lodash");
const socket = socketio("http://digitaldj.live:5000");
export default {
    name:"Chat",
    props:["chat_data"],
    data(){
        return{
           
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
            axios.post('http://digitaldj.live:5000/chat', {
                "message":vm.message, 
                "sender":vm.sender, 
                "room_key":localStorage.getItem("room_key")
            })
            .then(function(){
                
                    vm.message=""
                    console.log(vm.messages)
                    var temp={"room_key":`${localStorage.getItem("room_key")}`}
                    socket.emit("update_chat",temp)
                })
            
            .catch(function(error){
                console.log(error);
            })
        },
        processmessage:function(msg){
            this.message = msg
            this.debouncedmessage()
        },
        fromCurrentUser:function(msg_sender){
            if (msg_sender == this.$session.get('email'))
                return true;
            else
                return false;
        },
        tempuser:function(nickname){
            this.$session.start()
            this.$session.set('email', nickname)
            this.$session.set('loggedIn', false)
            this.$router.go()
        }
    },
    mounted(){
        
        let vm = this
        axios.get(`http://digitaldj.live:5000/chat?room_key=${localStorage.getItem("room_key")}`)
            .then(resp => {
                vm.chat_data = resp.data
            })
    } 
}
</script>

<style>
    div.card-content{
        max-height:500px;
        overflow: scroll;
        display:flex;
        flex-direction: column-reverse;
    }
    footer.card-footer{
        border-top: solid;
        max-height:150px;
    }
    .message{
        color: white;
        background-color: #4099FF;
    }
    .send{
        margin-top:10px;
        margin-left:10px;
    }
</style>