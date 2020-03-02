window.onload=function(){
    // new Vue instance
    Vue.component('todoinput',{
        data:function(){return {
            todo:null,
            category:"default",
            completed:0}
        },
        template: `<div class="field is-grouped">
        <p class="control is-expanded">
            <form method="POST" v-on:submit.prevent="sendform()">
          <input class="input" type="text" placeholder="Todo" v-model="todo">
          <input class="input" type="text" placeholder="Category" v-model=category>
          <label class="checkbox">
          <input type="checkbox" v-model="completed">
          Completed?
          </label
        </p>
        <p class="control">
          <button type="submit" class="button is-primary" >Submit</button>
        </p>
        </form>
      </div>`
      ,
      methods:{
          sendform(){
              var formData = new FormData();
              formData.append('todo',this.todo);
              formData.append('category',this.category);
              formData.append('completed',this.completed);
              console.log("sending form!")
              
              axios.post("http://localhost:5000/createtodo",formData,{
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
                }
              }).catch(error => {
                  console.log(error.response)
              })
          }
      }

    })
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
                // .get('https://jsonplaceholder.typicode.com/todos/')
                .get("http://localhost:5000/todos")
                // send that data to our message object above, bind it to the response data
                .then(response => (this.message =response.data))
        }
      })
    
    
}
