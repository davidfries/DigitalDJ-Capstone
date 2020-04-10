<template>
    <section>
        <button class="button is-danger"
            @click="isComponentModalActive = true">
            Login
        </button>

        <b-modal :active.sync="isComponentModalActive"
                 has-modal-card
                 trap-focus
                 aria-role="dialog"
                 aria-modal>
            <!-- <Login v-bind="formProps"></Login> -->
            <form action="" @submit.prevent="login">
                <div class="modal-card" style="width: auto">
                    <header class="modal-card-head">
                        <p class="modal-card-title">Login</p>
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
                                :value="password"
                                password-reveal
                                placeholder="Your password"
                                required>
                            </b-input>
                        </b-field>

                        <b-checkbox>Remember me</b-checkbox>
                    </section>
                    <footer class="modal-card-foot">
                        <!-- <button class="button" type="button" @click="$parent.close()">Close</button> -->
                        <div class="container has-text-centered">
                        <button class="button is-primary" @click="isComponentModalActive=false">Login</button>

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
    name:"Login",
    data(){
        return {
            isComponentModalActive: false,
            showModal:true,
            email:"",
            password:""
        }
    },
    methods:{
        login:function(){
            let vm = this
            axios.post('http://digitaldj.live:5000/login', {"email":this.email, "password":this.password})
            .then(function(response){
                if (response.status === 200){
                    vm.$session.start()
                    console.log("session started")
                    vm.$router.go()
                }
            })
            .then(function(){
                vm.$router.push('/rooms')
            })
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