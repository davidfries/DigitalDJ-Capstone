<template>
    <div class="container">
        <form @submit.prevent="Message">
            <div class="form-group">
                <input
                    type="text"
                    name="message"
                    class="form-control"
                    placeholder="Send message"
                    v-model="message">
            </div>

            <b-button class="button is-primary">Send</b-button>
        </form>
    </div>
</template>

<script>
const axios = require("axios");
export default {
    name:"Message",
    data(){
        return{
            message: "",
            sender: "",
            room: ""
        }
    },
    methods:{
        send:function(){
            //let vm = this
            axios.post('http://localhost:5000/chat', {"message":this.message, "sender":this.sender, "room":this.room})
        }
    }
}
</script>