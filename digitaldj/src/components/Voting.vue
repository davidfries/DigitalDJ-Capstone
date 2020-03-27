<template>
    <div>
        <h1>
            Song suggestion goes here
        </h1>
        <h2 class="subtitle">
            {{ count }} votes
        </h2>
        <b-button type="is-primary" inverted icon-right="arrow-up-bold" v-on:click="count++"></b-button>
        <b-button type="is-primary" inverted icon-right="arrow-down-bold" v-on:click="count--"></b-button>
    </div>
</template>

<script>
export default {
    name:"Voting",
    data(){
        return{
            count: 0
        }
    }
}
</script>