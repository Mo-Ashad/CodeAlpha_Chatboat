# CodeAlpha_Chatboat

CodeAlpha Internship Project - AI Chatbot using Flask and Gemini API with modern web interface.

---

# AI-Powered Chatbot 🤖

A modern, intelligent chatbot application built with Flask and Google's Gemini API, featuring a sleek web interface and commercial-ready training patterns.

## Features ✨

- **AI-Powered Responses**: Uses Google Gemini API for intelligent, context-aware responses
- **Retrieval-Based & Generative Models**: Combines predefined patterns with generative AI
- **Modern Web Interface**: Beautiful, responsive UI with real-time messaging
- **Conversation Context**: Maintains conversation history for coherent interactions
- **Training Patterns**: Pre-configured commercial use patterns for instant responses
- **Instant Responses**: Optimized for low-latency communication
- **User Engagement Tracking**: Built-in metrics for monitoring interactions
- **Mobile Responsive**: Fully responsive design for all devices
- **Health Monitoring**: API health checks and status indicators

## Project Structure 📁

```
CodeAlpha_Chatboat/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── .env.example               # Environment configuration template
├── static/
│   ├── index.html             # Main HTML interface
│   ├── styles.css             # Modern CSS styling
│   └── script.js              # Frontend JavaScript
├── training/
│   └── patterns.json          # Commercial training patterns
├── tests/
│   └── test_chatbot.py        # Unit tests
└── README.md                  # Project documentation
```

## Installation 🚀

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Google Gemini API key

### Step 1: Clone the Repository
```bash
git clone https://github.com/Mo-Ashad/CodeAlpha_Chatboat.git
cd CodeAlpha_Chatboat
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your Gemini API key
# GEMINI_API_KEY=your_api_key_here
```

Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### Step 5: Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Usage 💬

### Web Interface
1. Open your browser and navigate to `http://localhost:5000`
2. Type your message in the input field
3. Press Enter or click the Send button
4. Get instant AI-powered responses

### API Endpoints

#### Send Message
```bash
POST /api/chat
Content-Type: application/json

{
  "message": "Your message here"
}
```

Response:
```json
{
  "status": "success",
  "message": "Your message here",
  "response": "AI response",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

#### Get Conversation History
```bash
GET /api/history
```

#### Clear Conversation
```bash
POST /api/clear
```

#### Health Check
```bash
GET /api/health
```

## Training Patterns 📚

The chatbot comes with predefined commercial training patterns:

### Categories:
- **Greeting**: Hello, Hi, Hey, Greetings
- **Help Request**: Help, Support, Assist, Guidance
- **Product Inquiry**: Product, Service, Pricing, Features
- **Business Hours**: Hours, Open, Closed, Available
- **Contact Request**: Contact, Email, Phone, Call
- **Technical Support**: Error, Bug, Not Working, Troubleshoot
- **Pricing**: Cost, Price, Affordable, Discount
- **Account**: Login, Password, Sign up, Register
- **Feedback**: Feedback, Suggestion, Complaint, Rate
- **Closing**: Goodbye, Bye, Thanks, Thank you

Each pattern has predefined responses and confidence thresholds for accuracy optimization.

## Testing 🧪

Run the test suite to verify functionality and accuracy:

```bash
python -m pytest tests/test_chatbot.py -v
```

### Test Coverage
- ✅ Pattern matching accuracy
- ✅ API endpoint functionality
- ✅ Response accuracy and content safety
- ✅ Performance benchmarks
- ✅ User engagement tracking
- ✅ Conversation context maintenance

## Optimization & Performance 🚀

### Accuracy Optimization
- Pattern matching with confidence thresholds
- Context-aware response generation
- Conversation history tracking
- Predefined patterns for common queries

### User Engagement
- Real-time response delivery
- Conversation history maintenance
- Quick action buttons for common queries
- Visual feedback and status indicators
- Toast notifications for user guidance

### Performance Metrics
- Response time tracking
- Message length analysis
- Session duration monitoring
- User satisfaction metrics

## Deployment 🌐

### Docker Deployment
```bash
docker build -t chatbot .
docker run -p 5000:5000 --env-file .env chatbot
```

### Production Setup
1. Set `FLASK_ENV=production`
2. Set `DEBUG=False`
3. Use a production WSGI server (gunicorn)
4. Enable HTTPS/SSL
5. Configure rate limiting
6. Set up monitoring and logging

## Configuration 📋

### Environment Variables
- `GEMINI_API_KEY`: Your Google Gemini API key
- `FLASK_ENV`: Development or Production
- `DEBUG`: Enable/Disable debug mode
- `SECRET_KEY`: Flask secret key for sessions

### Customization
Edit `app.py` to customize:
- Response generation logic
- Training patterns
- Conversation history length
- API timeouts
- Error handling

## API Architecture 🏗️

The chatbot uses a hybrid approach:

1. **Pattern Matching Layer**: Quick responses for predefined patterns
2. **Context Layer**: Maintains conversation history
3. **AI Generation Layer**: Uses Gemini API for complex queries
4. **Response Filtering**: Ensures safety and relevance

## Frontend Features 🎨

- Modern, intuitive UI with gradient backgrounds
- Real-time message updates
- Typing indicators and loading animations
- Responsive design (Mobile, Tablet, Desktop)
- Smooth animations and transitions
- Toast notifications for feedback
- Quick action buttons
- Conversation history display

## Troubleshooting 🔧

### Issue: API Key Error
**Solution**: Ensure your `.env` file contains a valid GEMINI_API_KEY

### Issue: CORS Errors
**Solution**: Flask-CORS is already configured. Check browser console for detailed errors.

### Issue: Slow Responses
**Solution**: 
- Check internet connection
- Verify API key limits
- Optimize conversation history length

### Issue: Connection Refused
**Solution**: 
- Ensure app.py is running
- Check if port 5000 is available
- Try a different port in app.py

## Contributing 🤝

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## Security Considerations 🔒

- Input validation and sanitization
- Rate limiting for API calls
- CORS configuration
- Environment variable protection
- Error message sanitization
- Session management

## Future Enhancements 🚀

- [ ] Multi-language support
- [ ] Voice input/output integration
- [ ] Analytics dashboard
- [ ] User authentication
- [ ] Custom training data
- [ ] Sentiment analysis
- [ ] Integration with CRM systems
- [ ] Webhook support

## License 📄

This project is part of the CodeAlpha Internship Program.

## Support 💬

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: CodeAlpha Team

## Acknowledgments 🙏

- Google Gemini API for AI capabilities
- Flask framework for backend
- CodeAlpha for internship opportunity

---

**Built with ❤️ for better customer engagement**
