$(document).ready(function () {
  $.ajaxSetup({
    beforeSend: function (xhr, settings) {
      if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
        xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
      }
    },
  });
  var currentUserId = $("#currentUser").attr("data-id");
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

  function addMessage() {
    
  }

  var url = `ws://${window.location.host}/ws/socket-server/`;

  function socketFunc(chatSocket) {
    chatSocket.onmessage = function (e) {
      let data = JSON.parse(e.data);
      // console.log("Data:", data);

      if (data.type === "chat") {
        roomName = $("#chat-container").attr("data-room");
        if (data.room_name == roomName) {
          var messagesContainer = $("#chat-container");

          // Create a new <div> element
          var newDiv = $("<div class='chat-message'>");
          if (currentUserId == data.data.sender_id) {
            newDiv.addClass("my-chat");
          }

          // Create a <p> element and set its content to 'data.message'
          var newParagraph = $("<p>").text(data.data.message);

          // Append the <p> element to the <div> element
          newDiv.append(newParagraph);

          // Append the <div> element to the 'messages' container
          messagesContainer.append(newDiv);
        }
      } else if ((data.type = "success_connection")) {
        $("#chat-container").attr("data-room", data.room_name);
      } else {
      }
    };
  }

  $("#message-form").submit(function (e) {
    e.preventDefault();
    chatMessage = $("#message").val();
    const receiverId = $("#chat-container").attr("data-user-id");
    if (chatMessage != "") {
      window["chatSocket"].send(
        JSON.stringify({
          type: "private_room",
          message: chatMessage,
          sender_id: currentUserId,
          receiver_id: receiverId,
        })
      );
      socketFunc(window["chatSocket"]);
    }
    $("#message").val("");
  });

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
    if (window["chatSocket"] != null) {
      window["chatSocket"].close();
    }
    window["chatSocket"] = new WebSocket(dataUrl);
    socketFunc(window["chatSocket"]);

    var requestData = {
      receiver_id: userId,
    };
    console.log(requestData);
    $.ajax({
      type: "POST",
      url: "/previous-chat",
      data: requestData,
      // contentType: "application/json",
      success: function (response) {
        // Handle the success response
        data = JSON.parse(response.data)
        console.log(data);
        data.forEach(item => {
          console.log(item);
          const message = item.fields.text
          var messagesContainer = $("#chat-container");

          // Create a new <div> element
          var newDiv = $("<div class='chat-message'>");
          if (currentUserId == item.fields.sender) {
            newDiv.addClass("my-chat");
          }

          // Create a <p> element and set its content to 'data.message'
          var newParagraph = $("<p>").text(message);

          // Append the <p> element to the <div> element
          newDiv.append(newParagraph);

          // Append the <div> element to the 'messages' container
          messagesContainer.append(newDiv);
        });
      },
    });
  });
});

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
