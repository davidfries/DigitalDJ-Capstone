<template>
    <section>
        <div>
            <div class="pad card flex-container">
                <h1>My Account Information<br></h1>
                    <h2>Email: </h2>
                        <p>{{this.$session.get('email')}}<br><br></p>
                    <h2>Username: </h2>
                        <p>{{this.$session.get('username')}}<br></p>
                        <b-nav>
                            <b-nav-item class="button pad is-primary"
                                @click="changeUsername">
                                Change Username
                            </b-nav-item>
                            <b-nav-item class="button pad is-primary"
                                @click="changePassword">
                                Change Password
                            </b-nav-item>
                        </b-nav>
            </div>
            <div class="pad card flex-container">
                <h1>My Rooms<br></h1>
                <table class="container table">
                    <thead>
                        <th>Room Name</th>
                        <th>Max Quantity</th>
                        <th>Genre</th>
                    </thead>
                    <tbody>

                    </tbody>
                    </table>
            </div>
        </div>
    </section>
</template>

<script>
//const axios = require("axios");
export default {
    name:"UserSettings",
    data(){
        return{
            email: "",
            password: "",
            username: "",
            rooms: []
        }
    },
    methods:{
        changePassword:function(){

        },
        changeUsername:function(){
            
        }
    }
}
</script>

<style>
h1{
    font-size: 25px;
    line-height: 75px;
}
h2{
    font-size: 17px;
}
</style>