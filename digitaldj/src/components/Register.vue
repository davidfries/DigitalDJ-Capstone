<template>

    <section>
        
        <button id="reg" class="button is-primary"
            @click="isComponentModalActive = true">
            Register
        </button>

        <b-modal :active.sync="isComponentModalActive"
                 has-modal-card
                 trap-focus
                 aria-role="dialog"
                 aria-modal>
            <!-- <Login v-bind="formProps"></Login> -->
            <form action="" @submit="register">
                <div class="modal-card" style="width: auto">
                    <header class="modal-card-head">
                        <p class="modal-card-title">Register</p>
                    </header>
                    <section class="modal-card-body">
                        <b-field label="Email">
                            <b-input
                                v-model="email"
                                type="email"
                                :value="email"
                                placeholder="Your email"
                                required>
                            </b-input>
                        </b-field>

                        <b-field label="Password">
                            <b-input
                                v-model="password"
                                type="password"
                                id="password"
                                :value="password"
                                password-reveal
                                placeholder="Your password"
                                required>
                            </b-input>
                        </b-field>

                        <b-field label="Confirm Password">
                            <b-input
                                v-model="confirmPassword"
                                type="password"
                                id="confirmPassword"
                                :value="confirmPassword"
                                password-reveal
                                placeholder="Retype your password"
                                required>
                            </b-input>
                        </b-field>

                        <b-checkbox>Remember me</b-checkbox>
                    </section>
                    <footer class="modal-card-foot">
                        <!-- <button class="button" type="button" @click="$parent.close()">Close</button> -->
                        <div class="container has-text-centered">
                        <button class="button is-primary" @click="isComponentModalActive=false;persist()">Sign Up!</button>

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
    name:"Register",
    data(){
        return {
            isComponentModalActive: false,
            showModal:true,
            email: "",
            password: "",
            confirmPassword: ""
        }
    },
    methods:{
        register:function(){
            var pass = document.getElementById("password").value;
            var conf = document.getElementById("confirmPassword").value;
            if (pass != conf) {
                console.log("Passwords do not match.");
            }
            else{
                axios.post('http://localhost:5000/register', {"email":this.email, "password":this.password})
            }
        },
        persist:function(){
            localStorage.email = this.email
        }
    },
    mounted(){
        if (localStorage.email) {
            this.email = localStorage.email
        }
    }
}
</script>
<style>
    #reg{
        margin-right:5px;
    }
</style>