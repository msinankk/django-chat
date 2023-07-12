$(document).ready(function () {
  let url = `ws://${window.location.host}/ws/socket-server/`;

  const chatSocket = new WebSocket(url);

  chatSocket.onmessage = function (e) {
    let data = JSON.parse(e.data);
    console.log("Data:", data);

    if (data.type === "chat") {
      var messagesContainer = $("#chat-container");

      // Create a new <div> element
      var newDiv = $("<div class='chat-message'>");

      // Create a <p> element and set its content to 'data.message'
      var newParagraph = $("<p>").text(data.message);

      // Append the <p> element to the <div> element
      newDiv.append(newParagraph);

      // Append the <div> element to the 'messages' container
      messagesContainer.append(newDiv);
    }
  };

  $("#message-form").submit(function (e) {
    e.preventDefault();
    chatMessage = $("#message").val();
    chatSocket.send(JSON.stringify({ chat: chatMessage }));
  });
  // let form = document.getElementById("message-form");
  // form.addEventListener("submit", (e) => {
  //   e.preventDefault();
  //   let message = e.target.message.value;
  //   chatSocket.send(
  //     JSON.stringify({
  //       message: message,
  //     })
  //   );
  //   form.reset();
  // });
});
