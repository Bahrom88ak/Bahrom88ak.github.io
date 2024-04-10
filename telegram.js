var telegram_bot_id = "6690320111:AAEcuYySM2M4D7rkcuYctR0d5hygopYzutA";
var chat_id = 6005830556;
var company, city, number, tg, message;
var ready = function () {
    u_company = document.getElementById("company").value;
    u_city = document.getElementById("city").value;
    tg = document.getElementById("tg").value;
    number = document.getElementById("number").value;
    message = document.getElementById("message").value;
    message = "company: " + u_company + "\ncity: " + u_city + "\nnumber: " + number + "\nMessage: " + message + "\ntg: " + tg;
};
var sender = function () {
    ready();
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "https://api.telegram.org/bot" + telegram_bot_id + "/sendMessage",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "cache-control": "no-cache"
        },
        "data": JSON.stringify({
            "chat_id": chat_id,
            "text": message
        })
    };
    $.ajax(settings).done(function (response) {
        console.log(response);
    });
    document.getElementById("company").value = "";
    document.getElementById("city").value = "";
    document.getElementById("tg").value = "";
    document.getElementById("number").value = "";
    document.getElementById("message").value = "";
    return false;
};
