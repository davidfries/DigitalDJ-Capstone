<template>

<div class = "container">
     

        <span>Multiline message is:</span>
<p style="white-space: pre-line;">{{ message }}</p>
<br>
<textarea v-model="message" placeholder="add multiple lines"></textarea>

</div>
    
</template>




<script>
export default {
    name:"chat"
}
</script>