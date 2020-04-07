var http = require('http').createServer();
var io = require('socket.io')(http);


io.on('connection', function(socket){
  socket.on('room_connection',function(data){
    console.log("new connection from room")
    // console.log(JSON.parse(data).room_key)
  })
    console.log('a user connected '+socket.id);
    socket.emit('new_connection',"connected!");
  });



  http.listen(port=4113, function(){
    console.log('listening on *:'+port);
  });