<template>
  <div class="container" id="app">
    <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.8.0/css/bulma.min.css"> -->
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <Navbar username="testusr"></Navbar>
    <section class="hero is-success is-fullheight">
  <div class="hero-body">
    <div class="container has-text-centered">
      <router-view></router-view>
    
    </div>
  </div>
  </section>
    
    
  </div>
</template>

<script>

// import HelloWorld from './components/HelloWorld.vue'
// import MainPage from './components/MainPage.vue'
import Navbar from './components/Navbar.vue'
export default {
  name: 'App',
  components: {
    // MainPage,
    Navbar

  },
  
}
</script>

// THIS IS WHERE YOU EDIT COLORS FOR CSS PLEASE REFERENCE BULMA DOCS
<style lang="scss">
div.card{
  border-style: solid;
  border-radius: 5px;
}
div.flex-container{
  display: flex;
  flex-flow: column wrap;
  justify-content: space-around;
  align-items: flex-start;
}
.right{
  float:right;
}
.left{
  float:left;
}
.pad{
  padding:10px;
}
h1, h2, h3 {
  text-transform: uppercase;
  letter-spacing: 3px;
}

// Colors
@import "~bulma/sass/utilities/_all";
$primary: #4D658D;
$danger: #432F75;
$info: #7EB1D8;
$success: #72AB97;
$warning: #635192;
$primary-invert: findColorInvert($primary);
$twitter: #4099FF;
$twitter-invert: findColorInvert($twitter);
$colors: (
    "white": ($white, $black),
    "black": ($black, $white),
    "light": ($light, $light-invert),
    "dark": ($dark, $dark-invert),
    "primary": ($primary, $primary-invert),
    "info": ($info, $info-invert),
    "success": ($success, $success-invert),
    "warning": ($warning, $warning-invert),
    "danger": ($danger, $danger-invert),
    "twitter": ($twitter, $twitter-invert)
);

// Links
$link: $primary;
$link-invert: $primary-invert;
$link-focus-border: $primary;

// Import Bulma and Buefy styles
@import "~bulma";
@import "~buefy/src/scss/buefy";
</style>


