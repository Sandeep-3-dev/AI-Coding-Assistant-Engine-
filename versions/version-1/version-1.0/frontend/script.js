async function sendMessage(){

    const message =
        document.getElementById("user-input").value;

    const response = await fetch(
        "http://127.0.0.1:8000/chat",
        {
            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({
                message:message
            })
        }
    );

    const data = await response.json();

    document.getElementById("chat-box").innerHTML +=
        "<p><b>You:</b> "+message+"</p>";

    document.getElementById("chat-box").innerHTML +=
        "<p><b>Bot:</b> "+data.reply+"</p>";

}