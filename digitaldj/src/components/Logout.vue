<template>
    <section>
        <button class="button is-danger"
            @click="logout">
            Logout
        </button>
    </section>
</template>

<script>
export default {
    name:"Logout",
    methods:{
        logout:function(){
            this.$session.destroy()
            this.$router.go()
            this.$router.push({path: '/'})
        }
    }
}
</script>