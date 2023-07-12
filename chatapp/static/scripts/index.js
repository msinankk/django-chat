$(function () {
    var messageForm = $('#message-form');
    var messageInput = $('#message');
    var messageList = $('#chat-container');

    messageForm.on('submit', function (event) {
        event.preventDefault();
        var message = messageInput.val().trim();
        if (message !== '') {
            // Send the message via WebSocket
            websocket.send(JSON.stringify({
                'message': message,
                'sender': 'You'
            }));
            messageInput.val(''); // Clear the input field
        }
    });

    // WebSocket connection
    var websocket = new WebSocket('ws://' + window.location.host + '/ws/chat/{{ room.id }}/');

    // Handle incoming WebSocket messages
    websocket.onmessage = function (event) {
        var data = JSON.parse(event.data);
        var message = data.message;
        var sender = data.sender;
        var messageElement = $('<p><strong>' + sender + ':</strong> ' + message + '</p>');
        messageList.append(messageElement);
    };

    // Close the WebSocket connection when the page is unloaded
    $(window).on('beforeunload', function () {
        websocket.close();
    });
});