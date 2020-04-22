<template>
 <video class='video-js' 
 id="my-player"
   controls
    preload="auto"
    data-setup='{}'
 >
  <source :src="url" type="application/x-mpegURL">
  <!-- <source src="//vjs.zencdn.net/v/oceans.webm" type="video/webm"> -->
</video>   
</template>

<script>
import videojs from 'video.js'
// videojs('my-player');
// videojs('#test').Player()

export default {
    name:"Stream",
    props:["room_key"],
    data(){
        return{
            player:null,
            url:`http://stream.digitaldj.live/hls/${this.room_key}.m3u8`
        }
    },
    mounted(){
        this.player=videojs('my-player',this.options,function onPlayerReady(){
            console.log('player is ready')
        })
    }
}
</script>