from groq import Groq
import os
from dotenv import load_dotenv

# Import config values directly to avoid import issues
DEFAULT_MODEL = "llama-3.3-70b-versatile"
TECH_TEMPERATURE = 0.7
BEHAVIORAL_TEMPERATURE = 0.6
MAX_TOKENS_TECH = 1000
MAX_TOKENS_BEHAVIORAL = 800
DEFAULT_TECH_QUESTIONS = 5
DEFAULT_BEHAVIORAL_QUESTIONS = 5
ROLE_PROMPTS = {
    "software engineer": "Focus on coding, algorithms, and system design",
    "data scientist": "Emphasize statistics, ML, and data analysis",
    "devops engineer": "Concentrate on infrastructure, CI/CD, and monitoring",
    "product manager": "Focus on strategy, user experience, and stakeholder management",
    "designer": "Emphasize user experience, design principles, and tools"
}

load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_tech_questions(tech_stack: str, position: str = "", experience: int = 0, model: str = None):
    """Generate technical interview questions based on tech stack and role"""
    
    difficulty = "beginner" if experience < 2 else "intermediate" if experience < 5 else "advanced"
    
    # Get role-specific guidance
    role_guidance = ROLE_PROMPTS.get(position.lower(), "Focus on technical proficiency and problem-solving")
    
    # Use provided model or default
    selected_model = model or DEFAULT_MODEL
    
    prompt = f"""
    Generate {DEFAULT_TECH_QUESTIONS} technical interview questions for a {position} role with {experience} years of experience.
    Tech stack: {tech_stack}
    Difficulty level: {difficulty}
    Role guidance: {role_guidance}
    
    Make questions practical and role-specific. Include:
    - 2 coding/problem-solving questions
    - 2 system design/architecture questions  
    - 1 troubleshooting/debugging question
    
    Format each question on a new line without numbering.
    """
    
    try:
        response = client.chat.completions.create(
            model=selected_model,
            messages=[{"role": "user", "content": prompt}],
            temperature=TECH_TEMPERATURE,
            max_tokens=MAX_TOKENS_TECH
        )
        
        questions = response.choices[0].message.content.strip().split('\n')
        return [q.strip() for q in questions if q.strip()]
        
    except Exception as e:
        return [f"Error generating questions: {str(e)}"]

def generate_behavioral_questions(position: str = "", experience: int = 0, model: str = None):
    """Generate behavioral interview questions based on role and experience"""
    
    # Use provided model or default
    selected_model = model or DEFAULT_MODEL
    
    prompt = f"""
    Generate {DEFAULT_BEHAVIORAL_QUESTIONS} behavioral interview questions for a {position} role with {experience} years of experience.
    
    Focus on:
    - Leadership and teamwork
    - Problem-solving and conflict resolution
    - Adaptability and learning
    - Communication and collaboration
    - Goal achievement and motivation
    
    Use the STAR method framework. Format each question on a new line without numbering.
    """
    
    try:
        response = client.chat.completions.create(
            model=selected_model, 
            messages=[{"role": "user", "content": prompt}],
            temperature=BEHAVIORAL_TEMPERATURE,
            max_tokens=MAX_TOKENS_BEHAVIORAL
        )
        
        questions = response.choices[0].message.content.strip().split('\n')
        return [q.strip() for q in questions if q.strip()]
        
    except Exception as e:
        return [f"Error generating questions: {str(e)}"]

def analyze_candidate_fit(tech_stack: str, position: str, experience: int):
    """Analyze how well candidate fits the role"""
    
    prompt = f"""
    Analyze the candidate fit for {position} role:
    - Tech stack: {tech_stack}
    - Experience: {experience} years
    
    Provide:
    1. Strengths alignment
    2. Potential gaps
    3. Interview focus areas
    4. Overall fit score (1-10)
    """
    
    try:
        response = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=600
        )
        
        return response.choices[0].message.content.strip()
        
    except Exception as e:
        return f"Error analyzing candidate: {str(e)}"