document.getElementById('send-btn').addEventListener('click', sendMessage);
document.getElementById('user-input').addEventListener('keydown', function(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        sendMessage();
    }
});

function sendMessage() {
    const inputField = document.getElementById('user-input');
    const message = inputField.value.trim();
    if (message) {
        displayMessage(message, 'user');
        inputField.value = '';
        setTimeout(() => displayMessage(generateBotResponse(), 'bot'), 1000);
    }
}

function displayMessage(message, sender) {
    const chatBox = document.getElementById('chat-box');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', `${sender}-message`);
    messageElement.textContent = message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function generateBotResponse() {
    const responses = [
        "I'm here to listen. What's on your mind?",
        "It's okay to feel this way. Let's talk.",
        "I'm sorry you're feeling this way. You're not alone.",
        "I'm here for you. Let's chat."
    ];
    return responses[Math.floor(Math.random() * responses.length)];
}
