$(document).ready(function () {
  let url = `ws://${window.location.host}/ws/socket-server/`;

  const chatSocket = new WebSocket(url);

  chatSocket.onmessage = function (e) {
    let data = JSON.parse(e.data);
    console.log("Data:", data);
    // chatSocket.send(JSON.stringify({"message":"success"}))

    if (data.type === "chat") {
      let messages = document.getElementById("container");

      messages.append(
        "beforeend",
        `<div>
          <p>${data.message}</p>
      </div>`
      );
    }
  };

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
