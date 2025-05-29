# 🚀 TalentScout AI Chatbot

An AI-powered hiring assistant that generates personalized interview questions using Groq API and Streamlit.

## ✨ Features

- ✅ **Technical Questions**: Generate coding, system design, and troubleshooting questions
- ✅ **Behavioral Questions**: Create STAR-method behavioral interview questions  
- ✅ **Personalized**: Questions adapt based on experience level and role
- ✅ **Modern UI**: Clean, responsive Streamlit interface
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

## 📱 How to Use

1. **Fill Candidate Info**: Enter name, email, experience level, etc.
2. **Add Tech Stack**: List technologies (comma-separated)
3. **Choose Question Type**: 
   - Technical Questions
   - Behavioral Questions  
   - Both
4. **Generate**: Click "Generate Questions" for personalized results

## 🔧 Project Structure

```
talentscout-chatbot/
├── src/
│   ├── app.py           # Main Streamlit application
│   ├── prompts.py       # Groq AI prompt logic
│   └── utils/           # Utility functions
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables
└── README.md           # This file
```

## 🎯 Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Groq (Mixtral-8x7B)
- **Backend**: Python 3.9+
- **Environment**: python-dotenv

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

MIT License - feel free to use this project for your hiring needs!
```bash
streamlit run src/app.py
```

## Contributing
Feel free to submit issues or pull requests to enhance the functionality of the TalentScout AI Chatbot.

## License
This project is licensed under the MIT License.