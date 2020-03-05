<template>
    <section>
        <button class="button is-danger"
            @click="loginmodal()">
            Login
        </button>

        <b-modal :active.sync="isComponentModalActive"
                 has-modal-card
                 trap-focus
                 aria-role="dialog"
                 aria-modal>
            <modal-form v-bind="formProps"></modal-form>
        </b-modal>
    </section>
</template>

<script>
const ModalForm = {
        props: ['email', 'password'],
        template: `
            <form action="">
                <div class="modal-card" style="width: auto">
                    <header class="modal-card-head">
                        <p class="modal-card-title">Login</p>
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
                                :value="password"
                                password-reveal
                                placeholder="Your password"
                                required>
                            </b-input>
                        </b-field>

                        <b-checkbox>Remember me</b-checkbox>
                    </section>
                    <footer class="modal-card-foot">
                        <button class="button" type="button" @click="$parent.close()">Close</button>
                        <button class="button is-primary">Login</button>
                    </footer>
                </div>
            </form>
        `
    }
export default {
    name:"Login",
    methods:{
        loginmodal(){
            this.$buefy.modal.open({
                component:ModalForm,
              hasModalCard:true,
              trapFocus:true
            })
        }
    },
    data(){
        return {
            isComponentModalActive: false,
            formProps: {
                email:'email@email.com',
                password:'hunter2'
            }
        }
    }
}
</script>