"""
Configuration settings for TalentScout AI Chatbot
"""

# Groq Model Settings - Updated May 2025
DEFAULT_MODEL = "llama-3.3-70b-versatile"
ALTERNATIVE_MODELS = [
    "llama-3.3-70b-versatile",      # Latest Meta model (128K context)
    "llama-3.1-8b-instant",         # Fast and efficient (128K context)
    "llama3-70b-8192",              # Stable production model
    "llama3-8b-8192",               # Fastest production model
    "gemma2-9b-it",                 # Google's efficient model
]

# Question Generation Settings
DEFAULT_TECH_QUESTIONS = 5
DEFAULT_BEHAVIORAL_QUESTIONS = 5
MAX_TECH_STACK_ITEMS = 10
MAX_INPUT_LENGTH = 500

# Temperature settings for different question types
TECH_TEMPERATURE = 0.7
BEHAVIORAL_TEMPERATURE = 0.6

# Token limits
MAX_TOKENS_TECH = 1000
MAX_TOKENS_BEHAVIORAL = 800

# Experience level mappings
EXPERIENCE_LEVELS = {
    "beginner": (0, 2),
    "intermediate": (2, 5), 
    "advanced": (5, float('inf'))
}

# Default role-specific prompts
ROLE_PROMPTS = {
    "software engineer": "Focus on coding, algorithms, and system design",
    "data scientist": "Emphasize statistics, ML, and data analysis",
    "devops engineer": "Concentrate on infrastructure, CI/CD, and monitoring",
    "product manager": "Focus on strategy, user experience, and stakeholder management",
    "designer": "Emphasize user experience, design principles, and tools"
}
