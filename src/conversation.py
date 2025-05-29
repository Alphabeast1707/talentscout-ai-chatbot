"""
Conversational chatbot interface for TalentScout AI
Handles natural conversation flow, greetings, and context management
"""

import streamlit as st
import re
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

class ConversationState(Enum):
    GREETING = "greeting"
    COLLECTING_INFO = "collecting_info"
    TECH_STACK_INPUT = "tech_stack_input"
    GENERATING_QUESTIONS = "generating_questions"
    FOLLOW_UP = "follow_up"
    ENDING = "ending"

@dataclass
class CandidateProfile:
    name: str = ""
    email: str = ""
    position: str = ""
    experience: int = 0
    tech_stack: List[str] = None
    question_type: str = ""
    
    def __post_init__(self):
        if self.tech_stack is None:
            self.tech_stack = []

class ConversationManager:
    """Manages the conversation flow and context"""
    
    def __init__(self):
        self.conversation_endings = [
            "bye", "goodbye", "exit", "quit", "end", "stop", "thank you", 
            "thanks", "that's all", "done", "finish", "no more questions"
        ]
        
        self.greeting_keywords = [
            "hello", "hi", "hey", "good morning", "good afternoon", 
            "good evening", "start", "begin", "ready"
        ]
    
    def initialize_session(self):
        """Initialize session state for conversation"""
        if 'conversation_state' not in st.session_state:
            st.session_state.conversation_state = ConversationState.GREETING
        
        if 'candidate_profile' not in st.session_state:
            st.session_state.candidate_profile = CandidateProfile()
        
        if 'conversation_history' not in st.session_state:
            st.session_state.conversation_history = []
        
        if 'generated_questions' not in st.session_state:
            st.session_state.generated_questions = []
        
        if 'current_step' not in st.session_state:
            st.session_state.current_step = 0
    
    def detect_conversation_ending(self, user_input: str) -> bool:
        """Detect if user wants to end conversation"""
        if not user_input:
            return False
        
        user_input_lower = user_input.lower().strip()
        return any(ending in user_input_lower for ending in self.conversation_endings)
    
    def detect_greeting(self, user_input: str) -> bool:
        """Detect greeting from user"""
        if not user_input:
            return False
        
        user_input_lower = user_input.lower().strip()
        return any(greeting in user_input_lower for greeting in self.greeting_keywords)
    
    def extract_tech_stack(self, user_input: str) -> List[str]:
        """Extract technology stack from user input"""
        # Common tech keywords and patterns
        tech_patterns = [
            r'\b(?:python|java|javascript|js|typescript|ts|react|angular|vue|node\.?js|django|flask|fastapi|spring|laravel|php|ruby|rails|go|golang|rust|c\+\+|c#|swift|kotlin|flutter|dart|sql|mysql|postgresql|mongodb|redis|docker|kubernetes|aws|azure|gcp|git|jenkins|terraform|ansible)\b',
            r'\b(?:html|css|sass|scss|bootstrap|tailwind|jquery|express|nest\.?js|next\.?js|nuxt\.?js|svelte|ember|backbone|d3\.?js|three\.?js|chart\.?js)\b',
            r'\b(?:machine learning|ml|ai|artificial intelligence|data science|pandas|numpy|scipy|scikit-learn|tensorflow|pytorch|keras|opencv)\b'
        ]
        
        found_techs = []
        user_input_lower = user_input.lower()
        
        for pattern in tech_patterns:
            matches = re.findall(pattern, user_input_lower, re.IGNORECASE)
            found_techs.extend(matches)
        
        # Also split by common separators
        separators = [',', ';', '&', 'and', 'with', 'using', 'plus']
        words = user_input.replace(',', ' ').replace(';', ' ').replace('&', ' ').split()
        
        # Filter potential tech terms (2-15 characters, alphanumeric with some symbols)
        potential_techs = [
            word.strip('.,!?()[]{}') for word in words 
            if 2 <= len(word.strip('.,!?()[]{}')) <= 15 and 
            re.match(r'^[a-zA-Z0-9\.\-\+#]+$', word.strip('.,!?()[]{}'))
        ]
        
        found_techs.extend(potential_techs)
        
        # Remove duplicates and clean up
        unique_techs = []
        seen = set()
        for tech in found_techs:
            tech_clean = tech.strip().lower()
            if tech_clean not in seen and len(tech_clean) > 1:
                unique_techs.append(tech.strip())
                seen.add(tech_clean)
        
        return unique_techs[:10]  # Limit to 10 technologies
    
    def get_conversation_prompt(self, state: ConversationState, user_input: str = "") -> str:
        """Get appropriate response prompt based on conversation state"""
        prompts = {
            ConversationState.GREETING: """
            👋 **Welcome to TalentScout AI!**
            
            I'm your AI interview assistant, designed to help generate personalized interview questions based on your background and the role you're applying for.
            
            **Here's how I can help:**
            • Generate technical questions tailored to your tech stack
            • Create behavioral questions based on your experience level
            • Provide role-specific interview preparation
            
            **To get started, please tell me:**
            • Your name
            • The position you're applying for
            • Your years of experience
            
            *Example: "Hi, I'm John Smith, applying for a Senior Python Developer role with 5 years of experience."*
            
            How would you like to begin? 🚀
            """,
            
            ConversationState.COLLECTING_INFO: """
            Great! I need a bit more information to personalize your interview questions.
            
            **Please provide any missing details:**
            • Your full name
            • Email address (for our records)
            • Specific job position/role
            • Years of experience (0-20+)
            
            *You can provide this information in a natural way, like: "My email is john@email.com and I have 3 years of experience as a Frontend Developer."*
            """,
            
            ConversationState.TECH_STACK_INPUT: """
            Perfect! Now I'd like to know about your **technical expertise**.
            
            **Please list the technologies, frameworks, and tools you work with:**
            • Programming languages (Python, JavaScript, Java, etc.)
            • Frameworks (React, Django, Spring, etc.)
            • Databases (MySQL, MongoDB, PostgreSQL, etc.)
            • Tools & Platforms (Docker, AWS, Git, etc.)
            
            *Example: "I work with Python, Django, React, PostgreSQL, Docker, and AWS."*
            
            What technologies do you specialize in? 💻
            """,
            
            ConversationState.FOLLOW_UP: """
            **Great! I can generate interview questions for you.**
            
            **What type of questions would you like?**
            • **Technical Questions** - Coding, system design, troubleshooting
            • **Behavioral Questions** - STAR method, leadership, problem-solving
            • **Both Types** - Complete interview preparation
            
            *Just let me know your preference, like: "I'd like both technical and behavioral questions" or "Only technical questions please."*
            
            What would be most helpful for your interview preparation? 🎯
            """,
            
            ConversationState.ENDING: """
            🎉 **Thank you for using TalentScout AI!**
            
            **Next Steps:**
            1. **Review Your Questions** - Take time to prepare thoughtful answers
            2. **Practice STAR Method** - For behavioral questions (Situation, Task, Action, Result)
            3. **Research the Company** - Learn about their culture and recent developments
            4. **Prepare Questions** - Have thoughtful questions ready for your interviewer
            
            **Best of luck with your interview!** 🍀
            
            *Feel free to return anytime for more interview preparation. Simply refresh the page to start a new session.*
            
            **Would you like to:**
            • Generate more questions for a different role?
            • Start over with new information?
            • End this session?
            """
        }
        
        return prompts.get(state, "I'm here to help with your interview preparation. What would you like to know?")
    
    def parse_user_info(self, user_input: str, profile: CandidateProfile) -> Tuple[CandidateProfile, List[str]]:
        """Parse user input to extract candidate information"""
        issues = []
        updated_profile = profile
        
        # Extract email
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email_match = re.search(email_pattern, user_input)
        if email_match and not updated_profile.email:
            updated_profile.email = email_match.group()
        
        # Extract experience years
        experience_patterns = [
            r'(\d+)\s*(?:years?|yrs?)\s*(?:of\s*)?(?:experience|exp)',
            r'(?:experience|exp)\s*(?:of\s*)?(\d+)\s*(?:years?|yrs?)',
            r'(\d+)\s*(?:years?|yrs?)\s*(?:in|working|coding|programming)',
            r'(?:have|with|got)\s*(\d+)\s*(?:years?|yrs?)'
        ]
        
        for pattern in experience_patterns:
            match = re.search(pattern, user_input.lower())
            if match and not updated_profile.experience:
                try:
                    years = int(match.group(1))
                    if 0 <= years <= 50:  # Reasonable range
                        updated_profile.experience = years
                        break
                except (ValueError, IndexError):
                    continue
        
        # Extract name (first capitalized words that aren't common words)
        if not updated_profile.name:
            name_patterns = [
                r'(?:i\'?m|name is|call me|i am)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
                r'^([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)'
            ]
            
            for pattern in name_patterns:
                match = re.search(pattern, user_input)
                if match:
                    potential_name = match.group(1).strip()
                    # Filter out common words that aren't names
                    common_words = {'Hi', 'Hello', 'Good', 'Thanks', 'Please', 'Senior', 'Junior', 'Lead'}
                    if potential_name not in common_words and len(potential_name.split()) <= 3:
                        updated_profile.name = potential_name
                        break
        
        # Extract position/role
        if not updated_profile.position:
            role_patterns = [
                r'(?:applying for|role of|position of|job of|as a|as an)\s+([^,.!?]+)',
                r'([A-Za-z\s]+(?:developer|engineer|designer|manager|analyst|scientist|architect|lead|director))',
                r'(?:i\'?m a|work as a|i am a)\s+([^,.!?]+)'
            ]
            
            for pattern in role_patterns:
                matches = re.findall(pattern, user_input, re.IGNORECASE)
                for match in matches:
                    potential_role = match.strip()
                    if 3 <= len(potential_role) <= 50:  # Reasonable length
                        updated_profile.position = potential_role.title()
                        break
                if updated_profile.position:
                    break
        
        # Validate completeness
        if not updated_profile.name:
            issues.append("Please provide your name")
        if not updated_profile.email:
            issues.append("Please provide your email address")
        if not updated_profile.position:
            issues.append("Please specify the job position/role")
        
        return updated_profile, issues
    
    def generate_fallback_response(self, user_input: str, state: ConversationState) -> str:
        """Generate meaningful fallback responses"""
        fallback_responses = {
            ConversationState.GREETING: """
            I'd be happy to help you prepare for your interview! 
            
            To get started, please share some basic information about yourself:
            • Your name
            • The position you're applying for  
            • Your years of experience
            
            *For example: "Hi, I'm Sarah Johnson, applying for a Data Scientist role with 4 years of experience."*
            """,
            
            ConversationState.COLLECTING_INFO: """
            I need a bit more information to help you better. Please provide:
            
            **Missing details I need:**
            • Your full name
            • Email address
            • Specific job position
            • Years of experience
            
            *You can share this naturally, like: "My name is Alex, email alex@company.com, applying for Backend Developer with 2 years experience."*
            """,
            
            ConversationState.TECH_STACK_INPUT: """
            I'd like to know about your technical skills to generate relevant questions.
            
            **Please list technologies you work with:**
            • Programming languages
            • Frameworks & libraries
            • Databases
            • Tools & platforms
            
            *Example: "I use React, Node.js, MongoDB, and Docker" or "Python, Django, PostgreSQL, AWS"*
            """,
            
            ConversationState.FOLLOW_UP: """
            I can help generate interview questions for you!
            
            **What type would be most helpful?**
            • "Technical questions" - for coding and system design
            • "Behavioral questions" - for soft skills and experience
            • "Both types" - complete interview prep
            
            Just let me know your preference! 🎯
            """
        }
        
        base_response = fallback_responses.get(state, 
            "I'm here to help with interview preparation. Could you please rephrase or provide more specific information?")
        
        # Add helpful context if user seems confused
        if any(word in user_input.lower() for word in ['confused', 'help', 'what', 'how', 'don\'t understand']):
            base_response += "\n\n💡 **Need help?** I'm designed to generate personalized interview questions. Just share your information naturally, and I'll guide you through the process!"
        
        return base_response

def format_conversation_message(role: str, message: str) -> None:
    """Format and display conversation messages"""
    if role == "assistant":
        st.markdown(f"🤖 **TalentScout AI:**")
        st.markdown(message)
    else:
        st.markdown(f"👤 **You:**")
        st.markdown(f"*{message}*")
    
    st.markdown("---")

def display_candidate_profile(profile: CandidateProfile) -> None:
    """Display current candidate profile information"""
    with st.sidebar:
        st.markdown("### 📋 Candidate Profile")
        
        if profile.name:
            st.write(f"**Name:** {profile.name}")
        if profile.email:
            st.write(f"**Email:** {profile.email}")
        if profile.position:
            st.write(f"**Position:** {profile.position}")
        if profile.experience:
            st.write(f"**Experience:** {profile.experience} years")
        if profile.tech_stack:
            st.write(f"**Tech Stack:** {', '.join(profile.tech_stack)}")
        
        # Progress indicator
        total_fields = 5
        completed_fields = sum([
            bool(profile.name),
            bool(profile.email), 
            bool(profile.position),
            bool(profile.experience),
            bool(profile.tech_stack)
        ])
        
        progress = completed_fields / total_fields
        st.progress(progress)
        st.write(f"Profile: {completed_fields}/{total_fields} complete")
