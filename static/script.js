// Chat functionality
const chatMessages = document.getElementById('chatMessages');
const messageInput = document.getElementById('messageInput');
const chatForm = document.getElementById('chatForm');
const sendBtn = document.getElementById('sendBtn');
const loadingIndicator = document.getElementById('loadingIndicator');
const toast = document.getElementById('toast');

// Auto-resize textarea
messageInput.addEventListener('input', function() {
    this.style.height = 'auto';
    this.style.height = Math.min(this.scrollHeight, 120) + 'px';
});

// Handle Enter key
function handleKeyPress(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        sendMessage(event);
    }
}

// Send message
async function sendMessage(event) {
    event.preventDefault();

    const message = messageInput.value.trim();

    if (!message) {
        showToast('Please enter a message', 'error');
        return;
    }

    // Add user message to chat
    addMessage(message, 'user');

    // Clear input
    messageInput.value = '';
    messageInput.style.height = 'auto';

    // Show loading indicator
    loadingIndicator.style.display = 'flex';
    sendBtn.disabled = true;

    try {
        // Send message to backend
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        if (data.status === 'success') {
            // Add bot response to chat
            addMessage(data.response, 'bot');
        } else {
            addMessage('Sorry, I encountered an error. Please try again.', 'bot');
            showToast(data.error || 'Error occurred', 'error');
        }
    } catch (error) {
        console.error('Error:', error);
        addMessage('Sorry, I\'m having trouble connecting. Please try again.', 'bot');
        showToast('Connection error: ' + error.message, 'error');
    } finally {
        // Hide loading indicator
        loadingIndicator.style.display = 'none';
        sendBtn.disabled = false;
        messageInput.focus();
    }
}

// Add message to chat
function addMessage(content, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;

    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';

    // Handle text formatting
    contentDiv.innerHTML = sanitizeAndFormat(content);

    messageDiv.appendChild(contentDiv);
    chatMessages.appendChild(messageDiv);

    // Scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Sanitize and format message content
function sanitizeAndFormat(text) {
    // Escape HTML
    let escaped = document.createElement('div');
    escaped.textContent = text;
    let sanitized = escaped.innerHTML;

    // Convert URLs to links
    sanitized = sanitized.replace(
        /(https?:\/\/[^\s]+)/g,
        '<a href="$1" target="_blank" rel="noopener noreferrer" style="color: #60a5fa; text-decoration: underline;">$1</a>'
    );

    // Convert line breaks
    sanitized = sanitized.replace(/\n/g, '<br>');

    // Simple markdown-like formatting (optional)
    sanitized = sanitized.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    sanitized = sanitized.replace(/\*(.*?)\*/g, '<em>$1</em>');

    return sanitized;
}

// Clear chat
function clearChat() {
    if (confirm('Are you sure you want to clear the chat history?')) {
        chatMessages.innerHTML = '';
        addMessage('Hello! 👋 I\'m your AI assistant. How can I help you today?', 'bot');
        showToast('Chat cleared', 'success');
    }
}

// Show toast notification
function showToast(message, type = 'success') {
    toast.textContent = message;
    toast.className = `toast ${type}`;
    toast.style.display = 'block';

    setTimeout(() => {
        toast.style.display = 'none';
    }, 3000);
}

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    messageInput.focus();
});