# 🤖 TalentScout AI Chatbot

An AI-powered conversational hiring assistant that generates personalized interview questions through natural conversation using Groq API and Streamlit.

## ✨ Features

### 🗣️ Conversational Interface
- ✅ **Natural Conversation**: Chat naturally with the AI assistant
- ✅ **Intelligent Flow**: Guided conversation through greeting, info collection, and question generation
- ✅ **Context Awareness**: Maintains conversation context and candidate profile
- ✅ **Smart Parsing**: Automatically extracts information from natural language

### 📝 Question Generation
- ✅ **Technical Questions**: Generate coding, system design, and troubleshooting questions
- ✅ **Behavioral Questions**: Create STAR-method behavioral interview questions  
- ✅ **Personalized Content**: Questions adapt based on experience level and tech stack
- ✅ **Multiple Question Types**: Support for technical, behavioral, or combined question sets

### 🎨 User Experience
- ✅ **Real-time Profile**: Live candidate profile display with progress tracking
- ✅ **Conversation History**: Complete message history with proper formatting
- ✅ **Conversation Controls**: Reset options and session management
- ✅ **Modern UI**: Clean, responsive conversational interface
- ✅ **Fast AI**: Powered by Groq's lightning-fast LLM inference

## 🛠 Prerequisites

- Python 3.9+
- Groq API Key (get it from [Groq Console](https://console.groq.com))
- Git (optional)

## 🚀 Quick Start

### 1️⃣ Setup Environment

```bash
# Clone or download the project
cd talentscout-chatbot

# Install dependencies
pip3 install -r requirements.txt
```

### 2️⃣ Configure API Key

1. Get your Groq API key from [console.groq.com](https://console.groq.com)
2. Edit the `.env` file:
   ```
   GROQ_API_KEY=your_actual_groq_api_key_here
   ```

### 3️⃣ Run the Application

```bash
streamlit run src/app.py
```

The app will open in your browser at `http://localhost:8501`

## 💬 How to Use the Conversational Interface

### Natural Conversation Flow

1. **Start with a Greeting**: 
   ```
   "Hi, I'm John Smith applying for a Senior Python Developer role with 5 years of experience"
   ```

2. **Provide Missing Information**: 
   ```
   "My email is john.smith@email.com"
   ```

3. **Describe Your Tech Stack**: 
   ```
   "I work with Python, Django, React, PostgreSQL, Docker, and AWS"
   ```

4. **Choose Question Type**: 
   ```
   "I'd like both technical and behavioral questions"
   ```

5. **Get Personalized Questions**: The AI generates tailored interview questions displayed in the sidebar

### Conversation Features

- 🗣️ **Natural Language**: Type as you would speak - no forms to fill
- 🔄 **Smart Context**: AI remembers your information throughout the conversation
- 📊 **Live Profile**: See your candidate profile update in real-time
- 🆘 **Help System**: Type "help" anytime for guidance
- 👋 **Easy Exit**: Say "bye", "done", or "quit" to end the conversation

### Quick Commands
- `help` - Get contextual assistance
- `bye` / `done` / `quit` - End conversation
- Use sidebar controls to reset or start new conversation

## 🔧 Project Structure

```
talentscout-chatbot/
├── src/
│   ├── app.py              # Main conversational Streamlit application
│   ├── conversation.py     # Conversation flow and state management
│   ├── prompts.py          # Groq AI prompt logic
│   └── utils/              # Utility functions
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables
└── README.md              # This file
```

## 🌐 Live Deployments

### 🚀 Production App
**Heroku**: [https://talentscout-ai-harshit-6ec95dfb8d2e.herokuapp.com/](https://talentscout-ai-harshit-6ec95dfb8d2e.herokuapp.com/)

### 📂 Source Code
**GitHub**: [https://github.com/Alphabeast1707/talentscout-ai-chatbot](https://github.com/Alphabeast1707/talentscout-ai-chatbot)

## 🎯 Tech Stack

- **Frontend**: Streamlit (Conversational UI)
- **AI Model**: Groq (Llama 3.3 70B Versatile)
- **Conversation**: State Management & Natural Language Processing
- **Backend**: Python 3.11+
- **Environment**: python-dotenv
- **Deployment**: Heroku Platform

## 📊 New Features in Conversational Version

### 🤖 Conversational AI
- **Natural Language Understanding**: Parse candidate information from conversational input
- **Context Management**: Maintain conversation state and candidate profile
- **Smart Tech Stack Detection**: Automatically identify technologies from descriptions
- **Intelligent Fallbacks**: Helpful responses when input is unclear

### 🎨 Enhanced UI/UX
- **Real-time Profile Display**: Live candidate information updates
- **Conversation History**: Complete chat history with message formatting
- **Progress Tracking**: Visual indicators for profile completion
- **Conversation Controls**: Reset and session management options

### 🔧 Advanced Features
- **Multi-state Flow**: Guided conversation through distinct stages
- **Error Recovery**: Graceful handling of incomplete or invalid information
- **Help System**: Contextual assistance throughout the conversation
- **Session Persistence**: Maintains state across user interactions

## 🤝 Contributing

1. Fork the repository from [GitHub](https://github.com/Alphabeast1707/talentscout-ai-chatbot)
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes and test thoroughly
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Submit a pull request

## 📄 Documentation

- **Complete Technical Docs**: [DOCUMENTATION.md](./DOCUMENTATION.md)
- **Heroku Deployment Guide**: [HEROKU_DEPLOYMENT.md](./HEROKU_DEPLOYMENT.md)
- **Project Summary**: [PROJECT_SUMMARY.md](./PROJECT_SUMMARY.md)

## 📝 License

MIT License - feel free to use this project for your hiring needs!

---

**🤖 TalentScout AI Chatbot** • *Making interview preparation conversational and intelligent* • Built with ❤️ using Streamlit and Groq AI