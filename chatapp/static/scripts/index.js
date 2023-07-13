$(document).ready(function () {
  var currentUserId = $("#currentUser").attr("data-id")
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

  var url = `ws://${window.location.host}/ws/socket-server/`;

  function socketFunc(chatSocket) {
    chatSocket.onmessage = function (e) {
      let data = JSON.parse(e.data);
      console.log("Data:", data);
  
      if (data.type === "chat") {
        var messagesContainer = $("#chat-container");
  
        // Create a new <div> element
        var newDiv = $("<div class='chat-message'>");
        if (currentUserId == data.data.sender_id) {
          newDiv.addClass("my-chat") 
        }
  
        // Create a <p> element and set its content to 'data.message'
        var newParagraph = $("<p>").text(data.data.message);
  
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
    const receiverId = $("#chat-container").attr("data-user-id");
    window["chatSocket"].send(JSON.stringify({ 
      type:"private_room",
      message: chatMessage,
      sender_id:currentUserId,
      receiver_id:receiverId,
    }));
    socketFunc(window["chatSocket"])

  });

  $("#form-container").hide();
  $(".accordion-button").click(function (e) {
    $("#form-container").show();
    $("#form-container").addClass("d-flex d-flex-row");
    e.preventDefault();
    $(".accordion-button").addClass("collapsed");
    $(this).removeClass("collapsed");
    $("#chat-container").html("");

    const userId = $(this).attr("data-user-id");
    $("#chat-container").attr("data-user-id", userId);
    data = {
      user_id: userId,
    };
    const queryString = convertToQueryString(data);
    dataUrl = url + queryString;

    window["chatSocket"] = new WebSocket(dataUrl);
    socketFunc(window["chatSocket"])

  });
});
