<template>
 <video class='video-js' 
 id="my-player"
   controls
    preload="auto"
    data-setup='{}'
 >
  <source src="http://stream.digitaldj.live/hls/teststream.m3u8" type="application/x-mpegURL">
  <!-- <source src="//vjs.zencdn.net/v/oceans.webm" type="video/webm"> -->
</video>   
</template>

<script>
import videojs from 'video.js'
// videojs('my-player');
// videojs('#test').Player()

export default {
    name:"Stream",
    props:{
        type:Object,
        default(){
            return{};
        }
    },
    data(){
        return{
            player:null
        }
    },
    mounted(){
        this.player=videojs('my-player',this.options,function onPlayerReady(){
            console.log('player is ready')
        })
    }
}
</script>