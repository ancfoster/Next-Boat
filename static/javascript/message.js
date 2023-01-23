// Init variables
const messageContents = document.getElementById("id_message_contents");
const messageSubmit = document.getElementById("message-submit");

// Disables send button if length criteria not met
messageContents.addEventListener('input', checkMessageLength);
function checkMessageLength(e) {
    if(messageContents.value.length > 0) {
        messageSubmit.disabled = false;
    }
    if(messageContents.value.length < 1) {
        messageSubmit.setAttribute('disabled', 'disabled');
    }
    if(messageContents.value.length > 500) {
        messageSubmit.setAttribute('disabled', 'disabled');
    }
}