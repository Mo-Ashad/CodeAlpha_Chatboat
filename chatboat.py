import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import google.generativeai as genai
from datetime import datetime

load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Please add it to your .env file."
    )

genai.configure(api_key=GEMINI_API_KEY)

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")
# Chat history and conversation context
conversation_history = []
max_history_length = 10

# Predefined training patterns for commercial use
TRAINING_PATTERNS = {
    "greeting": {
        "patterns": ["hello", "hi", "hey", "greetings", "what's up"],
        "responses": ["Hello! How can I assist you today?", "Hi there! What can I help you with?"]
    },
    "help": {
        "patterns": ["help", "support", "assist", "guidance", "how do i"],
        "responses": ["I'm here to help! Please describe your issue or question."]
    },
    "product_inquiry": {
        "patterns": ["product", "service", "pricing", "cost", "price", "features"],
        "responses": ["I'd be happy to help with product information. What specifically would you like to know?"]
    },
    "hours": {
        "patterns": ["hours", "open", "closed", "available", "operation time"],
        "responses": ["Our business hours are Monday-Friday, 9 AM - 6 PM EST. How can I help?"]
    }
}

def check_predefined_patterns(user_input):
    """Check if user input matches predefined patterns"""
    user_input_lower = user_input.lower()
    
    for category, data in TRAINING_PATTERNS.items():
        for pattern in data["patterns"]:
            if pattern in user_input_lower:
                return data["responses"][0]
    
    return None

def generate_response(user_message):
    """Generate response using Gemini API with conversation context"""
    try:
        # Check predefined patterns first
        predefined_response = check_predefined_patterns(user_message)
        if predefined_response:
            return predefined_response
        
        # Build conversation context
        conversation_text = "\n".join([
            f"User: {msg['user']}\nAssistant: {msg['assistant']}"
            for msg in conversation_history[-max_history_length:]
        ])
        
        # Create prompt with context
        prompt = f"""You are a helpful customer service AI chatbot. Be professional, friendly, and concise.
Previous conversation:
{conversation_text}

Current user message: {user_message}

Provide a helpful response:"""
        
        # Generate response from Gemini
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        return f"I apologize, but I encountered an error: {str(e)}"

@app.route('/api/chat', methods=['POST'])
def chat():
    """Main chat endpoint"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Generate AI response
        bot_response = generate_response(user_message)
        
        # Store in conversation history
        conversation_history.append({
            'user': user_message,
            'assistant': bot_response,
            'timestamp': datetime.now().isoformat()
        })
        
        # Keep history manageable
        if len(conversation_history) > max_history_length * 2:
            conversation_history.pop(0)
        
        return jsonify({
            'status': 'success',
            'message': user_message,
            'response': bot_response,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/history', methods=['GET'])
def get_history():
    """Get conversation history"""
    try:
        return jsonify({
            'status': 'success',
            'history': conversation_history
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/clear', methods=['POST'])
def clear_history():
    """Clear conversation history"""
    try:
        # Clear the existing list in-place to avoid reassigning the global name
        conversation_history.clear()
        return jsonify({'status': 'success', 'message': 'Conversation history cleared'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

@app.route('/', methods=['GET'])
def index():
    """Root endpoint"""
    return jsonify({
        'name': 'AI Chatbot API',
        'version': '1.0.0',
        'endpoints': {
            'POST /api/chat': 'Send a message and get AI response',
            'GET /api/history': 'Get conversation history',
            'POST /api/clear': 'Clear conversation history',
            'GET /api/health': 'Health check'
        }
    })

if __name__ == '__main__':
    # Parse DEBUG from environment into a boolean (handles 'True'/'False' strings)
    debug_env = os.getenv('DEBUG', 'True')
    debug = str(debug_env).lower() in ('1', 'true', 'yes')
    app.run(debug=debug, host='0.0.0.0', port=5000)
