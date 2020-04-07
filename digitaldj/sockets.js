var http = require('http').createServer();
var io = require('socket.io')(http);


io.on('connection', function(socket){
    console.log('a user connected '+socket.id);
  });

  http.listen(port=4113, function(){
    console.log('listening on *:'+port);
  });