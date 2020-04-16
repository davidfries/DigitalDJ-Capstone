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
                <div class="content">
                    messages go here
                </div>
            </div>

            <footer class="card-footer">
                <b-field>
                    <b-input maxlength="200" type="textarea"></b-input>
                </b-field>
                <b-button class="button is-primary">Send</b-button>
            </footer>
        </div>
    </section>
</template>




<script>
// https://www.npmjs.com/package/vue-chatbox
export default {
    name:"Chat",
    data(){

    },
    methods:{
        send:function(){

        }
    }
}
</script>