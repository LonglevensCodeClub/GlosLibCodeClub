var app = require ('express')() ;
var http = require ('http'). Server (app) 
var io = require('socket.io')(http);

app.get('/simple', function(req, res){
	res.send('<h1>Hello Ruby</h1>');
});

io.on('connection', function(socket){
  console.log('a user connected');
});

app.get('/', function(req, res){
	res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(socket){
  console.log('a user connected');
  
  socket.on('disconnect', function(){
    console.log('user disconnected');
  });
  
  socket.on('chat message', function(msg){
    console.log('message: ' + msg);
  });
});


http.listen(3000, function(){
	console.log('listening on *:3000');
});
