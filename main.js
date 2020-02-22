window.onload=function(){
    // new Vue instance
    app = new Vue({
        // binds the vue instance to the specified HTML ID attribute
        el: '#app', 
        data(){
            return{
                message:null
            }
        },
        // mounted is a part of the Vue lifecycle
        mounted(){
            axios
                // using axios to get the JSON at the following URL
                .get('https://jsonplaceholder.typicode.com/todos/')
                // send that data to our message object above, bind it to the response data
                .then(response => (this.message =response.data))
        }
      })

}
