$(document).ready(function () {
  function convertToQueryString(data) {
    const params = new URLSearchParams();

    // Iterate over the properties of the data object
    for (const key in data) {
      if (data.hasOwnProperty(key)) {
        params.append(key, data[key]);
      }
    }

    // Return the generated query string
    return "?" + params.toString();
  }

  let url = `ws://${window.location.host}/ws/socket-server/`;

  function socketFunc(chatSocket) {
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
  }

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

  $("#form-container").hide();
  $(".accordion-button").click(function (e) {
    $("#form-container").show();
    $("#form-container").addClass("d-flex d-flex-row");
    e.preventDefault();
    $(".accordion-button").addClass("collapsed");
    $(this).removeClass("collapsed");
    $("#chat-container").html("");
    const userId = $(this).attr("data-user-id");
    data = {
      user_id: userId,
    };
    const queryString = convertToQueryString(data);
    dataUrl = url + queryString;

    const chatSocket = new WebSocket(dataUrl);
    socketFunc(chatSocket)

  });
});
