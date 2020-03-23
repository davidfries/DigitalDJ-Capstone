<template>
    <div>
        <h1>
            Song suggestion goes here
        </h1>
        <h2>
            {{ count }} votes
        </h2>
        <button v-on:click="count++">
            Upvote
        </button>
        <button v-on:click="count--">
            Downvote
        </button>
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