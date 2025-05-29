# 📋 TalentScout AI Chatbot - Setup Instructions

## 🎯 Overview
This guide will walk you through setting up and running the TalentScout AI Chatbot on your local machine.

## 📦 What You Need
- Python 3.9 or higher
- A Groq API key (free at [console.groq.com](https://console.groq.com))
- Internet connection
- Terminal/Command Prompt access

## 🚀 Step-by-Step Setup

### Step 1: Verify Python Installation
```bash
python3 --version
# Should show Python 3.9.x or higher
```

### Step 2: Navigate to Project Directory
```bash
cd "/Users/harshit/Downloads/AI: ML assignment/talentscout-chatbot"
```

### Step 3: Install Dependencies
```bash
pip3 install -r requirements.txt
```

### Step 4: Set Up Your API Key
1. Go to [console.groq.com](https://console.groq.com)
2. Sign up/log in and create an API key
3. Edit the `.env` file:
   ```bash
   nano .env
   # OR
   open .env
   ```
4. Replace `your_actual_key_here` with your actual Groq API key:
   ```
   GROQ_API_KEY=gsk_your_actual_api_key_here
   ```
5. Save the file

### Step 5: Run the Application
```bash
streamlit run src/app.py
```

The app will automatically open in your browser at `http://localhost:8501`

## 🧪 Testing the Application

### Test Case 1: Basic Technical Questions
1. Enter name: "John Doe"
2. Experience: 3 years
3. Position: "Software Engineer"
4. Tech Stack: "Python, React, PostgreSQL"
5. Select "Technical Questions"
6. Click "Generate Questions"

### Test Case 2: Behavioral Questions
1. Fill in candidate info
2. Select "Behavioral Questions"
3. Generate and review questions

### Test Case 3: Both Question Types
1. Fill in candidate info
2. Select "Both"
3. Verify both technical and behavioral questions appear

## 🛠 Troubleshooting

### Problem: "ModuleNotFoundError"
**Solution**: Install dependencies again:
```bash
pip3 install streamlit groq python-dotenv
```

### Problem: "Invalid API key"
**Solution**: 
1. Check your API key in the `.env` file
2. Ensure no extra spaces or quotes
3. Generate a new key if needed

### Problem: "streamlit: command not found"
**Solution**: 
```bash
pip3 install --upgrade streamlit
# OR
python3 -m streamlit run src/app.py
```

### Problem: Questions not generating
**Checklist**:
- ✅ API key is correct in `.env`
- ✅ Internet connection is working
- ✅ Tech stack field is not empty
- ✅ Check browser console for errors

## 🔧 Customization Options

### Change AI Model
Edit `src/prompts.py` and change:
```python
model="mixtral-8x7b-32768"
# to another Groq model like:
model="llama2-70b-4096"
```

### Modify Question Count
In `src/prompts.py`, change:
```python
Generate 5 technical interview questions
# to:
Generate 10 technical interview questions
```

### Add New Question Types
1. Create new function in `src/prompts.py`
2. Add option to selectbox in `src/app.py`
3. Handle the new type in the generation logic

## 📁 File Structure Explained

```
talentscout-chatbot/
├── src/
│   ├── app.py              # Main Streamlit UI
│   ├── prompts.py          # AI question generation
│   └── utils/
│       ├── __init__.py     # Package initialization
│       └── helpers.py      # Utility functions
├── requirements.txt        # Python packages
├── .env                   # API key (keep secure!)
├── .env.example          # Template for .env
├── README.md             # Project documentation
└── INSTRUCTIONS.md       # This file
```

## 🚀 Production Deployment

### Streamlit Cloud (Free)
1. Push code to GitHub
2. Connect repository to [share.streamlit.io](https://share.streamlit.io)
3. Add `GROQ_API_KEY` in secrets
4. Deploy!

### Local Network Access
```bash
streamlit run src/app.py --server.address 0.0.0.0
```

## 📞 Support

If you encounter issues:
1. Check this troubleshooting guide
2. Verify all prerequisites are met
3. Ensure API key is valid and active
4. Check internet connection

---

Happy interviewing! 🎉
