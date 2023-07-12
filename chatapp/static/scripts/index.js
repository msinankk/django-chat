$(document).ready(function () {
  let url = `ws://${window.location.host}/ws/socket-server/`;

  const chatSocket = new WebSocket(url);

  chatSocket.onmessage = function (e) {
    let data = JSON.parse(e.data);
    console.log("Data:", data);
    
    if (data.type === "chat") {
      let messages = document.getElementById("chat-container");

      messages.append(
        `<div>
          <p>${data.message}</p>
          </div>`
      );
    }
  };

  $("#message-form").submit(function (e) { 
    e.preventDefault();
    chatMessage = $("#message").val();
    chatSocket.send(JSON.stringify({"chat":chatMessage}))

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
