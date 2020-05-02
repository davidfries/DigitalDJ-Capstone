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
                                @click="isUsernameModalActive = true">
                                Change Username
                            </b-nav-item>
                            <b-nav-item class="button pad is-primary"
                                @click="isPasswordModalActive = true">
                                Change Password
                            </b-nav-item>
                        </b-nav>
            </div>
            <br>
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
                    <br>
            </div>

            <b-modal :active.sync="isUsernameModalActive"
                 has-modal-card
                 trap-focus
                 aria-role="dialog"
                 aria-modal>
                <form action="" @submit.prevent="changeUsername">
                    <div class="modal-card" style="width: auto">
                        <header class="modal-card-head">
                            <p class="modal-card-title">Change Username</p>
                        </header>
                        <section class="modal-card-body">
                        <b-field label="New Username">
                            <b-input
                                v-model="username"
                                type="username"
                                :value="username"
                                placeholder="New username"
                                required>
                            </b-input>
                        </b-field>
                    </section>
                    <footer class="modal-card-foot">
                        <!-- <button class="button" type="button" @click="$parent.close()">Close</button> -->
                        <div class="container has-text-centered">
                        <button class="button is-primary" @click="isUsernameModalActive=false">Change</button>

                        </div>
                    </footer>
                    </div>
                </form>
            </b-modal>

            <b-modal :active.sync="isPasswordModalActive"
                 has-modal-card
                 trap-focus
                 aria-role="dialog"
                 aria-modal>
                <form action="" @submit.prevent="changePassword">
                    <div class="modal-card" style="width: auto">
                        <header class="modal-card-head">
                            <p class="modal-card-title">Change Password</p>
                        </header>
                        <section class="modal-card-body">
                        <b-field label="Old Password">
                            <b-input
                                v-model="password"
                                type="password"
                                :value="password"
                                password-reveal
                                placeholder="Your old password"
                                required>
                            </b-input>
                        </b-field>

                        <b-field label="New Password">
                            <b-input
                                v-model="newPassword"
                                type="newPassword"
                                :value="newPassword"
                                password-reveal
                                placeholder="Your new password"
                                required>
                            </b-input>
                        </b-field>

                        <b-field label="New Password Validation">
                            <b-input
                                v-model="newPasswordValid"
                                type="newPasswordValid"
                                :value="newPasswordValid"
                                password-reveal
                                placeholder="Retype your new password"
                                required>
                            </b-input>
                        </b-field>
                    </section>
                    <footer class="modal-card-foot">
                        <!-- <button class="button" type="button" @click="$parent.close()">Close</button> -->
                        <div class="container has-text-centered">
                        <button class="button is-primary" @click="isPasswordModalActive=false">Change</button>

                        </div>
                    </footer>
                    </div>
                </form>
            </b-modal>
        </div>
    </section>
</template>

<script>
//const axios = require("axios");
export default {
    name:"UserSettings",
    data(){
        return{
            isUsernameModalActive: false,
            isPasswordModalActive: false,
            email: "",
            password: "",
            newPassword: "",
            newPasswordValid: "",
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