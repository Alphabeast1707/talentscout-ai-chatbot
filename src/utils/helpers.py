"""
Utility functions for the TalentScout AI Chatbot
"""

def format_questions(questions_list):
    """Format a list of questions for display"""
    if not questions_list:
        return ["No questions generated."]
    
    formatted = []
    for i, question in enumerate(questions_list, 1):
        if question.strip():
            formatted.append(f"{i}. {question.strip()}")
    
    return formatted if formatted else ["No valid questions found."]

def validate_tech_stack(tech_stack):
    """Validate and clean tech stack input"""
    if not tech_stack or not tech_stack.strip():
        return False, "Tech stack cannot be empty"
    
    technologies = [tech.strip() for tech in tech_stack.split(',') if tech.strip()]
    
    if not technologies:
        return False, "Please enter at least one technology"
    
    if len(technologies) > 10:
        return False, "Please limit to 10 technologies or fewer"
    
    return True, technologies

def get_difficulty_description(experience):
    """Get difficulty description based on experience"""
    if experience < 2:
        return "Beginner"
    elif experience < 5:
        return "Intermediate" 
    else:
        return "Advanced"

def sanitize_input(text):
    """Basic input sanitization"""
    if not text:
        return ""
    return text.strip()[:500]  # Limit input length
