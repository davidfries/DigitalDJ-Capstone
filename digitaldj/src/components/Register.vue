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
            <form action="">
                <div class="modal-card" style="width: auto">
                    <header class="modal-card-head">
                        <p class="modal-card-title">Register</p>
                    </header>
                    <section class="modal-card-body">
                        <b-field label="Email">
                            <b-input
                                type="email"
                                :value="email"
                                placeholder="Your email"
                                required>
                            </b-input>
                        </b-field>

                        <b-field label="Password">
                            <b-input
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
                                type='password'
                                id="confirmPassword"
                                :value="confirm"
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
                        <button class="button is-primary" v-on:click="check">Sign Up!</button>

                        </div>
                    </footer>
                </div>
            </form>
        </b-modal>
    </section>
</template>

<script>
// const Login = {
//         props: ['email', 'password'],
//         template: `
            
//         `
//     }
export default {
    name:"Register",
    // components:{
    //     Login
    // },
    props:['email', 'password', 'confirm'],
    data(){
        return {
            isComponentModalActive: false,
            showModal:true,
            formProps: {
                email:'email@email.com',
                password:'hunter2',
                confirm:'hunter2'
            }
        }
    },
    check: function (){
        var pass = document.getElementById("password").value;
        var conf = document.getElementById("confirmPassword").value;
        if (pass != conf) {
            alert("Passwords do not match.");
            return false;
        }
        return true;
    }
}
</script>
<style>
    #reg{
        margin-right:5px;
    }
</style>