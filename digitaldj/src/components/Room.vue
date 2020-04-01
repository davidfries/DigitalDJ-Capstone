<template>
    <div>
            <AddSong></AddSong>
            <voting></voting>
        
    </div>
</template>

<script>
import Voting from './Voting.vue'
import AddSong from './AddSong.vue'
export default {
    name:"Room",
    components:{
      Voting,AddSong
    }
}
</script>