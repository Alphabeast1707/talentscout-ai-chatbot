# 📚 TalentScout AI Chatbot - Complete Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [Architecture & Design](#architecture--design)
3. [Installation & Setup](#installation--setup)
4. [Configuration](#configuration)
5. [API Reference](#api-reference)
6. [User Interface Guide](#user-interface-guide)
7. [Technical Implementation](#technical-implementation)
8. [AI Models & Prompting](#ai-models--prompting)
9. [Error Handling & Validation](#error-handling--validation)
10. [Deployment](#deployment)
11. [Troubleshooting](#troubleshooting)
12. [Performance Optimization](#performance-optimization)
13. [Contributing Guidelines](#contributing-guidelines)
14. [Changelog](#changelog)

---

## Project Overview

### 🎯 Purpose
TalentScout AI Chatbot is an intelligent hiring assistant designed to revolutionize the interview process by generating personalized, role-specific interview questions using advanced AI technology. The application leverages Groq's lightning-fast LLM inference to create both technical and behavioral questions tailored to specific job roles, experience levels, and technology stacks.

### 🔑 Key Benefits
- **Personalization**: Questions adapt to candidate experience level (0-20+ years)
- **Role Specificity**: Tailored prompts for different job positions
- **Technology Awareness**: Questions based on specific tech stacks
- **Speed**: Sub-second question generation using Groq API
- **Flexibility**: Multiple AI models to choose from
- **User-Friendly**: Intuitive Streamlit interface

### 🎯 Target Users
- **HR Professionals**: Streamline interview preparation
- **Technical Recruiters**: Generate relevant technical questions
- **Engineering Managers**: Create consistent interview experiences
- **Startups**: Quick and efficient hiring processes
- **Educators**: Create assessment questions for courses

---

## Architecture & Design

### 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    TalentScout AI System                    │
├─────────────────────────────────────────────────────────────┤
│  Frontend Layer (Streamlit)                                │
│  ├── User Interface (app.py)                              │
│  ├── Input Validation & Sanitization                      │
│  └── Error Handling & User Feedback                       │
├─────────────────────────────────────────────────────────────┤
│  Business Logic Layer                                      │
│  ├── Question Generation (prompts.py)                     │
│  ├── Configuration Management (config.py)                 │
│  └── Utility Functions (utils/helpers.py)                 │
├─────────────────────────────────────────────────────────────┤
│  External Services Layer                                   │
│  ├── Groq API Integration                                 │
│  ├── Environment Configuration                            │
│  └── Model Selection & Management                         │
└─────────────────────────────────────────────────────────────┘
```

### 📁 Project Structure

```
talentscout-chatbot/
├── 📄 Documentation Files
│   ├── README.md              # Quick start guide
│   ├── INSTRUCTIONS.md        # Detailed setup instructions
│   ├── PROJECT_SUMMARY.md     # Project completion summary
│   └── DOCUMENTATION.md       # This comprehensive guide
│
├── ⚙️ Configuration Files
│   ├── requirements.txt       # Python dependencies
│   ├── .env                  # Environment variables (gitignored)
│   ├── .env.example          # Environment template
│   ├── .gitignore            # Git ignore rules
│   └── upload_to_github.sh   # GitHub upload helper script
│
└── 💻 Source Code
    └── src/
        ├── app.py              # Main Streamlit application
        ├── config.py           # Configuration constants
        ├── prompts.py          # AI question generation logic
        └── utils/
            ├── __init__.py     # Package initialization
            └── helpers.py      # Utility functions
```

### 🎨 Design Principles

1. **Modularity**: Each component has a single responsibility
2. **Configurability**: Easy to modify settings without code changes
3. **Extensibility**: Simple to add new features or models
4. **Error Resilience**: Graceful handling of API failures
5. **User Experience**: Intuitive interface with helpful feedback
6. **Security**: Input validation and API key protection

---

## Installation & Setup

### 📋 Prerequisites

#### System Requirements
- **Operating System**: macOS, Linux, or Windows
- **Python Version**: 3.9 or higher
- **Memory**: Minimum 2GB RAM
- **Storage**: 100MB free space
- **Internet**: Required for Groq API calls

#### Account Requirements
- **Groq Account**: Register at [console.groq.com](https://console.groq.com)
- **API Key**: Generate from Groq Console
- **GitHub Account**: Optional, for code sharing

### 🚀 Installation Steps

#### 1. Environment Setup

```bash
# Check Python version
python3 --version  # Should be 3.9+

# Navigate to project directory
cd "path/to/talentscout-chatbot"

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows
```

#### 2. Dependency Installation

```bash
# Install required packages
pip3 install -r requirements.txt

# Verify installation
pip3 list | grep -E "(streamlit|groq|python-dotenv)"
```

#### 3. Environment Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit with your API key
nano .env  # or use your preferred editor
```

Add your Groq API key:
```env
GROQ_API_KEY=gsk_your_actual_api_key_here
```

#### 4. Verification

```bash
# Test the application
streamlit run src/app.py

# The app should open at http://localhost:8501
```

### 🔧 Development Setup

For contributors or advanced users:

```bash
# Install development dependencies
pip3 install pytest black flake8 mypy

# Run code formatting
black src/

# Run linting
flake8 src/

# Run type checking
mypy src/
```

---

## Configuration

### 📝 Environment Variables

| Variable | Description | Required | Example |
|----------|-------------|----------|---------|
| `GROQ_API_KEY` | Your Groq API key | ✅ Yes | `gsk_abc123...` |

### ⚙️ Application Settings

#### Model Configuration (config.py)
```python
# Available AI Models
ALTERNATIVE_MODELS = [
    "llama-3.3-70b-versatile",    # Latest, best reasoning
    "llama-3.1-8b-instant",       # Fast and efficient  
    "llama3-70b-8192",            # Stable production
    "llama3-8b-8192",             # Fastest
    "gemma2-9b-it",               # Google's model
]

# Default Model
DEFAULT_MODEL = "llama-3.3-70b-versatile"

# Temperature Settings (creativity level)
TECH_TEMPERATURE = 0.7        # Technical questions
BEHAVIORAL_TEMPERATURE = 0.6   # Behavioral questions

# Token Limits
MAX_TOKENS_TECH = 1000        # Technical responses
MAX_TOKENS_BEHAVIORAL = 800    # Behavioral responses

# Question Counts
DEFAULT_TECH_QUESTIONS = 5
DEFAULT_BEHAVIORAL_QUESTIONS = 5
```

#### Role-Specific Prompts
```python
ROLE_PROMPTS = {
    "software engineer": "Focus on coding, algorithms, and system design",
    "data scientist": "Emphasize statistics, ML, and data analysis", 
    "devops engineer": "Concentrate on infrastructure, CI/CD, and monitoring",
    "product manager": "Focus on strategy, user experience, and stakeholder management",
    "designer": "Emphasize user experience, design principles, and tools"
}
```

### 🎛️ Customization Options

#### Adding New Models
```python
# In config.py, add to ALTERNATIVE_MODELS list
ALTERNATIVE_MODELS.append("new-model-name")
```

#### Custom Role Prompts
```python
# Add new role-specific guidance
ROLE_PROMPTS["new_role"] = "Custom guidance for new role"
```

#### Adjusting Question Difficulty
```python
# Modify experience level thresholds
def get_difficulty_level(experience):
    if experience < 2:
        return "beginner"
    elif experience < 5:
        return "intermediate"
    elif experience < 10:
        return "advanced"
    else:
        return "expert"
```

---

## API Reference

### 🔌 Core Functions

#### `generate_tech_questions()`
Generates technical interview questions based on provided parameters.

**Parameters:**
- `tech_stack` (str): Comma-separated list of technologies
- `position` (str, optional): Job role/position
- `experience` (int, optional): Years of experience (0-20+)
- `model` (str, optional): AI model to use

**Returns:**
- `str`: Generated technical questions or error message

**Example:**
```python
questions = generate_tech_questions(
    tech_stack="Python, FastAPI, PostgreSQL",
    position="Backend Developer", 
    experience=3,
    model="llama-3.3-70b-versatile"
)
```

#### `generate_behavioral_questions()`
Creates behavioral interview questions using STAR methodology.

**Parameters:**
- `position` (str): Job role/position
- `experience` (int, optional): Years of experience
- `model` (str, optional): AI model to use

**Returns:**
- `str`: Generated behavioral questions or error message

**Example:**
```python
questions = generate_behavioral_questions(
    position="Product Manager",
    experience=5,
    model="llama-3.3-70b-versatile"
)
```

### 🛠️ Utility Functions

#### `validate_tech_stack(tech_list)`
Validates technology stack input.

**Parameters:**
- `tech_list` (list): List of technologies

**Returns:**
- `tuple`: (is_valid: bool, error_message: str)

#### `sanitize_input(text, max_length=100)`
Cleans and validates text input.

**Parameters:**
- `text` (str): Input text to sanitize
- `max_length` (int): Maximum allowed length

**Returns:**
- `str`: Sanitized text

#### `get_difficulty_description(experience)`
Returns difficulty level description based on experience.

**Parameters:**
- `experience` (int): Years of experience

**Returns:**
- `str`: Difficulty level description

---

## User Interface Guide

### 🖥️ Main Interface

#### Header Section
- **Title**: "🚀 TalentScout AI Chatbot"
- **Subtitle**: Role-specific interview question generator

#### Sidebar Controls
- **Model Selection**: Dropdown to choose AI model
- **About Section**: Project information
- **Model Info**: Details about selected model
- **Quick Tips**: Usage guidelines

#### Main Form
1. **Candidate Information**
   - Name (required)
   - Email (required)
   - Position/Role (required)
   - Years of Experience (0-20+ slider)

2. **Technical Details**
   - Tech Stack (comma-separated)
   - Technology count display

3. **Question Type Selection**
   - Technical Questions only
   - Behavioral Questions only  
   - Both types

4. **Generation Button**
   - "Generate Questions" with loading state

#### Results Display
- **Generated Questions**: Formatted output
- **Error Messages**: User-friendly error handling
- **Success Indicators**: Confirmation of successful generation

### 📱 Responsive Design

The interface adapts to different screen sizes:
- **Desktop**: Full sidebar and main content
- **Tablet**: Collapsible sidebar
- **Mobile**: Stacked layout with hamburger menu

### 🎨 UI Components

#### Sidebar Elements
```python
# Model selector
selected_model = st.selectbox(
    "🤖 AI Model",
    ALTERNATIVE_MODELS,
    help="Choose the AI model for question generation"
)

# Information panels
st.info("AI-powered interview question generator")
```

#### Form Elements
```python
# Input fields with validation
name = st.text_input("👤 Candidate Name *", placeholder="Enter full name")
email = st.text_input("📧 Email *", placeholder="candidate@email.com")

# Slider with custom styling
experience = st.slider("💼 Years of Experience", 0, 20, 2)
```

#### Interactive Elements
```python
# Question type selection
question_type = st.radio(
    "🎯 Question Type *",
    ["Technical Questions", "Behavioral Questions", "Both"],
    horizontal=True
)
```

---

## Technical Implementation

### 🧠 AI Integration

#### Groq API Setup
```python
from groq import Groq
import os

# Initialize client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# API call structure
response = client.chat.completions.create(
    model=selected_model,
    messages=[{"role": "user", "content": prompt}],
    temperature=temperature,
    max_tokens=max_tokens
)
```

#### Prompt Engineering

**Technical Questions Prompt Structure:**
```python
prompt = f"""
Generate {question_count} technical interview questions for a {position} role 
with {experience} years of experience.

Tech stack: {tech_stack}
Difficulty level: {difficulty}
Role guidance: {role_guidance}

Make questions practical and role-specific. Include:
- 2 coding/problem-solving questions
- 2 system design/architecture questions  
- 1 troubleshooting/debugging question

Format each question on a new line without numbering.
"""
```

**Behavioral Questions Prompt Structure:**
```python
prompt = f"""
Generate {question_count} behavioral interview questions for a {position} role 
with {experience} years of experience.

Focus on STAR method (Situation, Task, Action, Result) scenarios.
Include questions about:
- Leadership and teamwork
- Problem-solving and decision-making
- Communication and conflict resolution
- Growth and learning experiences
- Role-specific behavioral competencies

Format each question on a new line without numbering.
"""
```

### 🔄 Data Flow

1. **User Input** → Streamlit form collection
2. **Validation** → Input sanitization and validation
3. **API Call** → Groq API request with structured prompt
4. **Response Processing** → Parse and format AI response
5. **Display** → Show results to user with error handling

### 💾 State Management

Streamlit session state usage:
```python
# Initialize session state
if 'generated_questions' not in st.session_state:
    st.session_state.generated_questions = None

# Store results
st.session_state.generated_questions = questions

# Persist form data
if 'form_data' not in st.session_state:
    st.session_state.form_data = {}
```

### 🔒 Security Measures

1. **API Key Protection**: Environment variables only
2. **Input Sanitization**: Strip and validate all inputs
3. **Length Limits**: Prevent excessive API usage
4. **Error Handling**: No sensitive data in error messages

---

## AI Models & Prompting

### 🤖 Available Models

#### Primary Models

**1. llama-3.3-70b-versatile** (Recommended)
- **Context**: 128K tokens
- **Strengths**: Best reasoning, latest features
- **Use Case**: Complex technical questions
- **Performance**: High quality, moderate speed

**2. llama-3.1-8b-instant** (Speed Optimized)
- **Context**: 128K tokens  
- **Strengths**: Fast inference, efficient
- **Use Case**: Quick question generation
- **Performance**: Good quality, high speed

**3. llama3-70b-8192** (Production Stable)
- **Context**: 8K tokens
- **Strengths**: Stable, reliable
- **Use Case**: Consistent results
- **Performance**: High quality, moderate speed

#### Model Selection Guidelines

```python
# Choose based on requirements
def select_optimal_model(use_case):
    if use_case == "speed":
        return "llama-3.1-8b-instant"
    elif use_case == "quality":
        return "llama-3.3-70b-versatile" 
    elif use_case == "stability":
        return "llama3-70b-8192"
    else:
        return DEFAULT_MODEL
```

### 🎯 Prompt Engineering Best Practices

#### 1. Clear Structure
```python
# Template with clear sections
prompt_template = """
CONTEXT: {context}
TASK: {task}  
REQUIREMENTS: {requirements}
OUTPUT FORMAT: {format}
"""
```

#### 2. Role-Specific Guidance
```python
# Adaptive prompts based on role
role_adaptations = {
    "frontend": "Focus on UI/UX, JavaScript frameworks, responsive design",
    "backend": "Emphasize APIs, databases, server architecture", 
    "fullstack": "Balance frontend and backend technologies"
}
```

#### 3. Experience-Level Adaptation
```python
def adapt_for_experience(base_prompt, experience):
    if experience < 2:
        return base_prompt + "\nFocus on fundamental concepts and basic implementation."
    elif experience >= 10:
        return base_prompt + "\nInclude advanced architecture and leadership scenarios."
    return base_prompt
```

### 📊 Prompt Performance Optimization

#### Temperature Settings
- **Technical Questions**: 0.7 (balanced creativity)
- **Behavioral Questions**: 0.6 (more consistent)
- **Creative Tasks**: 0.8-0.9 (higher creativity)

#### Token Management
```python
# Optimal token allocation
TOKEN_LIMITS = {
    "technical": 1000,     # Detailed explanations
    "behavioral": 800,     # Structured scenarios  
    "quick": 500,          # Brief responses
}
```

---

## Error Handling & Validation

### 🛡️ Input Validation

#### Required Field Validation
```python
def validate_required_fields(name, email, position):
    errors = []
    
    if not name or len(name.strip()) < 2:
        errors.append("Name must be at least 2 characters")
    
    if not email or "@" not in email:
        errors.append("Valid email address required")
        
    if not position or len(position.strip()) < 2:
        errors.append("Position must be specified")
        
    return errors
```

#### Technology Stack Validation
```python
def validate_tech_stack(tech_list):
    if not tech_list:
        return False, "At least one technology required"
    
    if len(tech_list) > 10:
        return False, "Maximum 10 technologies allowed"
    
    for tech in tech_list:
        if len(tech.strip()) < 2:
            return False, f"Invalid technology: {tech}"
    
    return True, ""
```

#### Input Sanitization
```python
def sanitize_input(text, max_length=100):
    if not text:
        return ""
    
    # Remove dangerous characters
    sanitized = re.sub(r'[<>"\']', '', text)
    
    # Limit length
    if len(sanitized) > max_length:
        sanitized = sanitized[:max_length]
    
    return sanitized.strip()
```

### ⚠️ Error Categories

#### 1. API Errors
```python
try:
    response = client.chat.completions.create(...)
except Exception as e:
    if "authentication" in str(e).lower():
        return "❌ Invalid API key. Please check your Groq API key."
    elif "rate_limit" in str(e).lower():
        return "⏳ Rate limit exceeded. Please try again in a moment."
    else:
        return f"🔧 API Error: {str(e)}"
```

#### 2. Validation Errors
```python
# User-friendly validation messages
VALIDATION_MESSAGES = {
    "name_required": "👤 Please enter a candidate name",
    "email_invalid": "📧 Please enter a valid email address",
    "tech_stack_empty": "💻 Please specify at least one technology",
    "position_required": "🎯 Please specify the job position"
}
```

#### 3. System Errors
```python
def handle_system_error(error):
    error_type = type(error).__name__
    
    if error_type == "ConnectionError":
        return "🌐 Network connection issue. Please check your internet."
    elif error_type == "TimeoutError":
        return "⏱️ Request timed out. Please try again."
    else:
        return "🔧 System error occurred. Please contact support."
```

### 🚨 Error Display

#### User-Friendly Messages
```python
# Error display with icons and helpful text
if errors:
    for error in errors:
        st.error(f"❌ {error}")
    
    # Helpful suggestions
    st.info("💡 **Tips:**\n- Check all required fields\n- Verify your API key\n- Try again in a moment")
```

#### Debug Information
```python
# Debug mode for development
if DEBUG_MODE:
    st.expander("🔍 Debug Info").write({
        "model": selected_model,
        "tokens_used": token_count,
        "response_time": response_time,
        "error_details": error_details
    })
```

---

## Deployment

### 🚀 Local Deployment

#### Standard Deployment
```bash
# Install dependencies
pip3 install -r requirements.txt

# Set environment variables
export GROQ_API_KEY="your_api_key"

# Run application
streamlit run src/app.py --port 8501
```

#### Docker Deployment
```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ src/
COPY .env .env

EXPOSE 8501

CMD ["streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### ☁️ Cloud Deployment

#### Streamlit Cloud
1. **Push to GitHub**: Ensure code is in GitHub repository
2. **Connect Account**: Link GitHub to Streamlit Cloud
3. **Deploy App**: Select repository and branch
4. **Set Secrets**: Add GROQ_API_KEY in app settings

#### Heroku Deployment
```bash
# Create Procfile
echo "web: streamlit run src/app.py --server.port=$PORT --server.address=0.0.0.0" > Procfile

# Deploy to Heroku
heroku create talentscout-ai
heroku config:set GROQ_API_KEY="your_api_key"
git push heroku main
```

#### AWS/GCP Deployment
```yaml
# docker-compose.yml for cloud deployment
version: '3.8'
services:
  talentscout:
    build: .
    ports:
      - "8501:8501"
    environment:
      - GROQ_API_KEY=${GROQ_API_KEY}
    restart: unless-stopped
```

### 🔧 Production Considerations

#### Environment Configuration
```python
# Production settings
PRODUCTION_CONFIG = {
    "debug": False,
    "cache_ttl": 3600,
    "rate_limit": 100,
    "timeout": 30,
    "max_concurrent_requests": 10
}
```

#### Monitoring & Logging
```python
import logging

# Configure logging for production
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
```

#### Health Checks
```python
# Health check endpoint
def health_check():
    try:
        # Test API connectivity
        test_response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": "test"}],
            max_tokens=10
        )
        return {"status": "healthy", "api": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}
```

---

## Troubleshooting

### 🔍 Common Issues

#### 1. API Key Problems

**Issue**: "Invalid API key" error
```
❌ Authentication failed. Please check your Groq API key.
```

**Solutions**:
```bash
# Verify API key format
echo $GROQ_API_KEY | grep "gsk_"

# Check .env file
cat .env | grep GROQ_API_KEY

# Test API key manually
curl -H "Authorization: Bearer $GROQ_API_KEY" \
     https://api.groq.com/openai/v1/models
```

#### 2. Module Import Errors

**Issue**: "ModuleNotFoundError" 
```
ModuleNotFoundError: No module named 'groq'
```

**Solutions**:
```bash
# Reinstall dependencies
pip3 install -r requirements.txt --force-reinstall

# Check Python path
python3 -c "import sys; print(sys.path)"

# Verify installation
pip3 show groq streamlit python-dotenv
```

#### 3. Streamlit Port Issues

**Issue**: "Port already in use"
```
OSError: [Errno 48] Address already in use
```

**Solutions**:
```bash
# Find process using port 8501
lsof -i :8501

# Kill process (replace PID)
kill -9 <PID>

# Use different port
streamlit run src/app.py --server.port 8502
```

#### 4. Environment Variable Issues

**Issue**: API key not loaded
```python
# Debug environment loading
import os
from dotenv import load_dotenv

load_dotenv()
print("API Key loaded:", bool(os.getenv("GROQ_API_KEY")))
print("Working directory:", os.getcwd())
print("Env file exists:", os.path.exists(".env"))
```

### 🐛 Debugging Tools

#### Debug Mode
```python
# Enable debug mode in app.py
DEBUG = True

if DEBUG:
    st.sidebar.write("🔍 Debug Info")
    st.sidebar.json({
        "session_state": dict(st.session_state),
        "environment": {
            "python_version": sys.version,
            "working_dir": os.getcwd(),
            "api_key_set": bool(os.getenv("GROQ_API_KEY"))
        }
    })
```

#### Logging Configuration
```python
import logging

# Configure detailed logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# Log API calls
logger.info(f"Making API call with model: {model}")
logger.debug(f"Prompt: {prompt}")
```

#### Performance Monitoring
```python
import time

# Monitor response times
start_time = time.time()
response = generate_questions(...)
end_time = time.time()

st.sidebar.metric("Response Time", f"{end_time - start_time:.2f}s")
```

### 📞 Getting Help

#### Self-Help Resources
1. **Check Logs**: Review application logs for errors
2. **Verify Configuration**: Ensure all settings are correct
3. **Test Components**: Isolate issues to specific functions
4. **Update Dependencies**: Ensure latest package versions

#### Community Support
- **GitHub Issues**: Report bugs and feature requests
- **Streamlit Community**: Get UI/UX help
- **Groq Documentation**: API-specific questions

#### Professional Support
- **Code Review**: Submit PR for review
- **Custom Features**: Contact for paid development
- **Enterprise Support**: Dedicated support options

---

## Performance Optimization

### ⚡ Speed Optimization

#### Model Selection for Speed
```python
# Fast models for quick responses
SPEED_OPTIMIZED_MODELS = [
    "llama-3.1-8b-instant",  # Fastest
    "llama3-8b-8192",        # Fast and stable
]

# Quality models for better results
QUALITY_OPTIMIZED_MODELS = [
    "llama-3.3-70b-versatile",  # Best quality
    "llama3-70b-8192",          # Stable quality
]
```

#### Caching Strategies
```python
import streamlit as st

# Cache expensive operations
@st.cache_data(ttl=3600)  # Cache for 1 hour
def cached_api_call(prompt, model):
    return client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )

# Cache validation results
@st.cache_data
def validate_tech_stack_cached(tech_string):
    return validate_tech_stack(tech_string.split(','))
```

#### Async Processing
```python
import asyncio
import aiohttp

async def generate_questions_async(prompts):
    tasks = []
    for prompt in prompts:
        task = asyncio.create_task(api_call_async(prompt))
        tasks.append(task)
    
    results = await asyncio.gather(*tasks)
    return results
```

### 💾 Memory Optimization

#### Session State Management
```python
# Clean up old session data
def cleanup_session_state():
    keys_to_remove = []
    for key in st.session_state:
        if key.startswith('temp_') and 'timestamp' in st.session_state.get(key, {}):
            if time.time() - st.session_state[key]['timestamp'] > 3600:
                keys_to_remove.append(key)
    
    for key in keys_to_remove:
        del st.session_state[key]
```

#### Efficient Data Structures
```python
# Use generators for large datasets
def generate_questions_stream(tech_stack, position, count):
    for i in range(count):
        yield generate_single_question(tech_stack, position, i)

# Limit response sizes
MAX_RESPONSE_SIZE = 2000  # characters
```

### 📊 Monitoring & Analytics

#### Performance Metrics
```python
import time
from dataclasses import dataclass

@dataclass
class PerformanceMetrics:
    api_response_time: float
    total_request_time: float
    tokens_used: int
    cache_hit_rate: float

def track_performance():
    metrics = PerformanceMetrics(
        api_response_time=measure_api_time(),
        total_request_time=measure_total_time(),
        tokens_used=count_tokens(),
        cache_hit_rate=calculate_cache_rate()
    )
    
    # Display in sidebar
    st.sidebar.metrics("Performance", metrics)
```

#### Usage Analytics
```python
# Track user interactions
def log_usage(action, details):
    usage_data = {
        "timestamp": time.time(),
        "action": action,
        "details": details,
        "session_id": st.session_state.get('session_id')
    }
    
    # Log to file or analytics service
    logging.info(f"Usage: {usage_data}")
```

---

## Contributing Guidelines

### 🤝 How to Contribute

#### Getting Started
1. **Fork Repository**: Create your own fork on GitHub
2. **Clone Locally**: `git clone your-fork-url`
3. **Create Branch**: `git checkout -b feature/your-feature`
4. **Make Changes**: Implement your improvements
5. **Test Changes**: Ensure everything works
6. **Submit PR**: Create pull request with description

#### Development Setup
```bash
# Install development dependencies
pip3 install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run tests
python -m pytest tests/

# Check code style
black src/ --check
flake8 src/
mypy src/
```

### 📝 Code Standards

#### Python Style Guide
- **PEP 8**: Follow Python style guidelines
- **Type Hints**: Use type annotations
- **Docstrings**: Document all functions
- **Comments**: Explain complex logic

```python
def generate_questions(
    tech_stack: str, 
    position: str, 
    experience: int = 0
) -> str:
    """Generate interview questions based on parameters.
    
    Args:
        tech_stack: Comma-separated list of technologies
        position: Job role or position title
        experience: Years of experience (default: 0)
        
    Returns:
        Generated questions as formatted string
        
    Raises:
        ValueError: If tech_stack is empty
        APIError: If Groq API call fails
    """
    pass
```

#### File Organization
```python
# Standard import order
import os
import sys
from typing import List, Dict, Optional

import streamlit as st
from groq import Groq

from .config import DEFAULT_MODEL
from .utils.helpers import validate_input
```

### 🧪 Testing Guidelines

#### Unit Tests
```python
import pytest
from src.utils.helpers import validate_tech_stack

def test_validate_tech_stack_valid():
    """Test validation with valid tech stack."""
    tech_list = ["Python", "FastAPI", "PostgreSQL"]
    is_valid, message = validate_tech_stack(tech_list)
    assert is_valid is True
    assert message == ""

def test_validate_tech_stack_empty():
    """Test validation with empty tech stack."""
    tech_list = []
    is_valid, message = validate_tech_stack(tech_list)
    assert is_valid is False
    assert "required" in message.lower()
```

#### Integration Tests
```python
import pytest
from unittest.mock import patch
from src.prompts import generate_tech_questions

@patch('src.prompts.client')
def test_generate_tech_questions_success(mock_client):
    """Test successful question generation."""
    # Mock API response
    mock_client.chat.completions.create.return_value.choices[0].message.content = "Sample questions"
    
    result = generate_tech_questions("Python", "Developer", 2)
    assert "Sample questions" in result
    assert mock_client.chat.completions.create.called
```

### 📋 Feature Request Process

#### Proposing Features
1. **Check Existing Issues**: Avoid duplicates
2. **Create Issue**: Use feature request template
3. **Discuss Design**: Get community feedback
4. **Implement**: Follow coding standards
5. **Document**: Update relevant documentation

#### Feature Template
```markdown
## Feature Request: [Feature Name]

### Problem Statement
Describe the problem this feature solves.

### Proposed Solution
Explain your proposed implementation.

### Alternatives Considered
List other approaches you considered.

### Additional Context
Any other relevant information.
```

### 🐛 Bug Reporting

#### Bug Report Template
```markdown
## Bug Report: [Brief Description]

### Steps to Reproduce
1. Step one
2. Step two
3. Expected vs actual result

### Environment
- OS: [macOS/Linux/Windows]
- Python Version: [3.9/3.10/3.11]
- Package Versions: [streamlit, groq versions]

### Error Messages
```
Paste any error messages or logs here
```

### Screenshots
If applicable, add screenshots.
```

---

## Changelog

### Version 1.0.0 (Current)

#### ✨ Features Added
- **AI-Powered Question Generation**: Groq API integration
- **Multi-Model Support**: 5 different AI models available
- **Role-Specific Prompts**: Tailored questions for different positions
- **Experience-Based Difficulty**: Questions adapt to experience level
- **Modern UI**: Clean Streamlit interface with sidebar controls
- **Input Validation**: Comprehensive validation and sanitization
- **Error Handling**: User-friendly error messages and recovery
- **Documentation**: Complete setup and usage documentation

#### 🛠️ Technical Implementation
- **Modular Architecture**: Separated concerns across files
- **Configuration Management**: Centralized settings in config.py
- **Utility Functions**: Reusable helper functions
- **Environment Variables**: Secure API key management
- **Git Integration**: Ready for version control and collaboration

#### 📚 Documentation
- **README.md**: Quick start guide
- **INSTRUCTIONS.md**: Detailed setup instructions
- **PROJECT_SUMMARY.md**: Project completion overview
- **DOCUMENTATION.md**: Comprehensive technical documentation

#### 🔧 Development Tools
- **GitHub Integration**: Repository setup and upload helper
- **Environment Template**: .env.example for easy setup
- **Git Ignore**: Proper exclusions for Python projects
- **Requirements**: Pinned dependencies for stability

### Planned Features (Future Versions)

#### Version 1.1.0 (Planned)
- **Question Templates**: Pre-built question sets for common roles
- **Export Functionality**: Save questions as PDF or Word documents
- **Question Rating**: User feedback system for question quality
- **Bulk Generation**: Generate questions for multiple candidates

#### Version 1.2.0 (Planned)
- **Interview Scheduling**: Calendar integration
- **Candidate Database**: Store and manage candidate information
- **Analytics Dashboard**: Usage statistics and insights
- **Team Collaboration**: Multi-user support and sharing

#### Version 2.0.0 (Future)
- **Video Integration**: AI-powered video interview analysis
- **Custom Models**: Fine-tuned models for specific industries
- **Enterprise Features**: SSO, advanced security, compliance
- **Mobile App**: Native mobile application

---

## 📞 Support & Contact

### 🆘 Getting Help

#### Documentation
- **Quick Start**: See README.md for basic setup
- **Detailed Guide**: This documentation covers everything
- **Troubleshooting**: Check the troubleshooting section above

#### Community Support
- **GitHub Issues**: Report bugs and request features
- **Discussions**: Ask questions and share ideas
- **Community Forums**: Connect with other users

#### Professional Support
- **Custom Development**: Paid customization services
- **Enterprise Support**: Dedicated support for businesses
- **Training**: Workshops and training sessions

### 📧 Contact Information

- **GitHub**: [Alphabeast1707/talentscout-ai-chatbot](https://github.com/Alphabeast1707/talentscout-ai-chatbot)
- **Issues**: Use GitHub issues for bug reports
- **Features**: Submit feature requests via GitHub

### 🤝 Contributing

We welcome contributions! Please see the [Contributing Guidelines](#contributing-guidelines) section for details on how to contribute to this project.

---

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

*This documentation was last updated on May 29, 2025. For the most current information, please check the GitHub repository.*

---

## 🤖 Conversational Interface

### Overview
TalentScout AI features a natural conversational interface that guides users through the interview preparation process using intelligent conversation flow management.

### Conversation States
The chatbot operates through distinct conversation states:

1. **GREETING** - Initial welcome and information collection
2. **COLLECTING_INFO** - Gathering missing candidate details
3. **TECH_STACK_INPUT** - Technology stack specification
4. **GENERATING_QUESTIONS** - AI question generation process
5. **FOLLOW_UP** - Question type selection and customization
6. **ENDING** - Conversation conclusion and next steps

### Conversational Features

#### Natural Language Processing
- **Intent Recognition**: Detects greetings, endings, and help requests
- **Information Extraction**: Automatically parses names, emails, experience, and roles
- **Technology Detection**: Identifies tech stack from natural language descriptions
- **Context Awareness**: Maintains conversation context across interactions

#### Intelligent Flow Management
- **State Transitions**: Seamless progression through conversation stages
- **Error Recovery**: Handles incomplete information gracefully
- **Fallback Responses**: Provides helpful guidance when input is unclear
- **Conversation Memory**: Retains information throughout the session

#### User Experience Enhancements
- **Real-time Profile Updates**: Live candidate profile display in sidebar
- **Progress Tracking**: Visual progress indicators for profile completion
- **Conversation History**: Complete message history with proper formatting
- **Quick Actions**: Reset options and conversation controls

### API Reference - Conversation Classes

#### ConversationState (Enum)
```python
class ConversationState(Enum):
    GREETING = "greeting"
    COLLECTING_INFO = "collecting_info"
    TECH_STACK_INPUT = "tech_stack_input"
    GENERATING_QUESTIONS = "generating_questions"
    FOLLOW_UP = "follow_up"
    ENDING = "ending"
```

#### CandidateProfile (Dataclass)
```python
@dataclass
class CandidateProfile:
    name: str = ""
    email: str = ""
    position: str = ""
    experience: int = 0
    tech_stack: List[str] = None
    question_type: str = ""
```

#### ConversationManager Class

##### Key Methods:

**initialize_session()**
- Initializes session state for conversation management
- Sets up conversation history and candidate profile

**detect_conversation_ending(user_input: str) -> bool**
- Detects user intent to end conversation
- Recognizes keywords: "bye", "goodbye", "exit", "quit", "done"

**extract_tech_stack(user_input: str) -> List[str]**
- Extracts technology stack from natural language input
- Uses regex patterns and keyword matching
- Returns up to 10 identified technologies

**parse_user_info(user_input: str, profile: CandidateProfile) -> Tuple[CandidateProfile, List[str]]**
- Parses candidate information from natural language
- Extracts name, email, position, and experience
- Returns updated profile and list of missing information

**generate_fallback_response(user_input: str, state: ConversationState) -> str**
- Provides contextual help when user input is unclear
- Offers guidance specific to current conversation state

### Usage Examples

#### Starting a Conversation
```
User: "Hi, I'm Sarah Johnson applying for a Senior Python Developer role with 5 years of experience"

Bot: "Great! I got some information. Still needed: Email address
Please provide your email address for our records."
```

#### Tech Stack Input
```
User: "I work with Python, Django, React, PostgreSQL, Docker, and AWS"

Bot: "Excellent! I found these technologies: Python, Django, React, PostgreSQL, Docker, AWS
What type of questions would you like?"
```

#### Question Generation
```
User: "I'd like both technical and behavioral questions"

Bot: "Perfect! I've generated 12 personalized interview questions for you!
Your questions are now displayed in the sidebar."
```

### Conversation Controls

#### Sidebar Features
- **New Conversation**: Resets entire session
- **Reset Current Step**: Resets current conversation state
- **Current State Display**: Shows active conversation stage
- **Model Selection**: Choose AI model for question generation

#### User Commands
- **Help**: Type "help" for guidance at any stage
- **End Conversation**: Use "bye", "done", or "quit" to conclude
- **Reset**: Start over with new information anytime

### Error Handling

#### Graceful Degradation
- **API Failures**: Clear error messages with troubleshooting steps
- **Invalid Input**: Helpful prompts for correct information format
- **Missing Information**: Progressive collection with clear requirements
- **Network Issues**: Retry mechanisms and fallback responses

#### Validation Features
- **Email Format**: Validates email address patterns
- **Experience Range**: Ensures reasonable experience years (0-50)
- **Tech Stack**: Validates and cleans technology inputs
- **Name Format**: Filters common words that aren't names

### Advanced Features

#### Context Preservation
- **Session State**: Maintains conversation context across page refreshes
- **Profile Persistence**: Retains candidate information throughout session
- **History Management**: Stores complete conversation history
- **Progress Tracking**: Visual indicators for completion status

#### Intelligent Responses
- **Dynamic Prompts**: Context-aware response generation
- **Personalization**: Tailored messages based on user information
- **Multi-modal Input**: Handles various input formats and styles
- **Adaptive Guidance**: Adjusts help based on user confusion indicators
