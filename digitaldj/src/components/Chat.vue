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
                        <span class="text-secondary time">{{message.timestamp}}</span>
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
                    <b-button class="button is-primary">Send</b-button>
                </form>
            </footer>
        </div>
    </section>
</template>




<script>
const axios = require("axios");
export default {
    name:"Chat",
    props: ["room_key"],
    data(){
        return{
            messages:[],
            message: "",
            sender: localStorage.sender,
            room: this.room_key
        }
    },
    methods:{
        send:function(){
            let vm = this
            console.log(this.sender)
            console.log(this.room)
            console.log(this.message)
            axios.post('http://localhost:5000/chat', {"message":this.message, "sender":this.sender, "room":this.room})
            .then(function(response){
                if (response.status === 200){
                    vm.messages.push(vm.message)
                }
            })
        }
    }
}
</script>