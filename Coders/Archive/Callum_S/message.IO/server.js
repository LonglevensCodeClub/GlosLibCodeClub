var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

// Route handler
app.get('/', function (req, res) {
  // res.send('<h1>Hello Callum</h1>');
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', function (socket) {
  console.log('a user connected');
  socket.on('disconnect', function () {
    console.log('user disconnected');
  });
  socket.on('chat message', function (msg) {
    io.emit('chat message', msg);
  });
});

http.listen(3000, function () {
  console.log('listening on *:3000');
});


