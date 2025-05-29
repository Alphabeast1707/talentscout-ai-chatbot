import streamlit as st
import os
from dotenv import load_dotenv
from prompts import generate_tech_questions, generate_behavioral_questions
from utils.helpers import validate_tech_stack, sanitize_input, get_difficulty_description

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="TalentScout AI", 
    page_icon="🚀", 
    layout="centered"
)

# Sidebar with settings
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Model selection
    ALTERNATIVE_MODELS = [
        "llama-3.3-70b-versatile",      # Latest Meta model (128K context)
        "llama-3.1-8b-instant",         # Fast and efficient (128K context)
        "llama3-70b-8192",              # Stable production model
        "llama3-8b-8192",               # Fastest production model
        "gemma2-9b-it",                 # Google's efficient model
    ]
    DEFAULT_MODEL = "llama-3.3-70b-versatile"
    
    selected_model = st.selectbox(
        "🤖 AI Model",
        ALTERNATIVE_MODELS,
        index=ALTERNATIVE_MODELS.index(DEFAULT_MODEL),
        help="Choose the AI model for question generation"
    )
    
    st.markdown("### About TalentScout AI")
    st.info("AI-powered interview question generator using Groq's fast inference.")
    
    st.markdown("### Model Info")
    model_info = {
        "llama-3.3-70b-versatile": "🦙 Latest Meta model, best reasoning (128K context)",
        "llama-3.1-8b-instant": "⚡ Fast and efficient (128K context)",
        "llama3-70b-8192": "🎯 Stable production model (8K context)",
        "llama3-8b-8192": "🚀 Fastest production model (8K context)",
        "gemma2-9b-it": "💎 Google's efficient model (8K context)"
    }
    st.write(model_info.get(selected_model, "Advanced AI model"))
    
    st.markdown("### Quick Tips")
    st.write("• Enter specific technologies for better questions")
    st.write("• Higher experience = more complex questions") 
    st.write("• Try different question types for variety")
    
    st.markdown("### Tech Stack Examples")
    st.code("Python, Django, PostgreSQL, Redis")
    st.code("React, Node.js, MongoDB, AWS")
    st.code("Java, Spring Boot, MySQL, Docker")

st.title("🚀 TalentScout AI Hiring Assistant")
st.markdown("Generate personalized interview questions based on candidate profile")

# Main form
with st.form("candidate_form"):
    st.subheader("📋 Candidate Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
    
    with col2:
        experience = st.slider("Experience (years)", 0, 30, 2)
        position = st.text_input("Desired Position")
        location = st.text_input("Current Location")
    
    tech_stack = st.text_area(
        "Tech Stack (comma-separated)", 
        placeholder="e.g., Python, React, AWS, Docker"
    )
    
    question_type = st.selectbox(
        "Question Type",
        ["Technical Questions", "Behavioral Questions", "Both"]
    )
    
    submit = st.form_submit_button("🔥 Generate Questions", use_container_width=True)

# Generate questions when form is submitted
if submit:
    # Validate required fields
    if not name.strip():
        st.error("Please enter your full name!")
    elif not tech_stack.strip():
        st.error("Please enter at least one technology in the tech stack!")
    else:
        # Validate tech stack
        is_valid, result = validate_tech_stack(tech_stack)
        if not is_valid:
            st.error(result)
        else:
            # Sanitize inputs
            clean_name = sanitize_input(name)
            clean_position = sanitize_input(position)
            clean_tech_stack = ", ".join(result)
            
            # Show difficulty level
            difficulty = get_difficulty_description(experience)
            st.info(f"Generating {difficulty} level questions for {clean_name}")
            
            with st.spinner("Generating personalized questions..."):
                try:
                    if question_type == "Technical Questions":
                        questions = generate_tech_questions(clean_tech_stack, clean_position, experience, selected_model)
                        st.success("🎯 Technical Questions Generated!")
                        for i, q in enumerate(questions, 1):
                            if q.strip():
                                st.write(f"**{i}.** {q}")
                        
                    elif question_type == "Behavioral Questions":
                        questions = generate_behavioral_questions(clean_position, experience, selected_model)
                        st.success("🧠 Behavioral Questions Generated!")
                        for i, q in enumerate(questions, 1):
                            if q.strip():
                                st.write(f"**{i}.** {q}")
                        
                    else:  # Both
                        tech_questions = generate_tech_questions(clean_tech_stack, clean_position, experience, selected_model)
                        behavioral_questions = generate_behavioral_questions(clean_position, experience, selected_model)
                        
                        st.success("🎯 All Questions Generated!")
                        
                        st.subheader("💻 Technical Questions")
                        for i, q in enumerate(tech_questions, 1):
                            if q.strip():
                                st.write(f"**{i}.** {q}")
                        
                        st.subheader("🧠 Behavioral Questions") 
                        for i, q in enumerate(behavioral_questions, 1):
                            if q.strip():
                                st.write(f"**{i}.** {q}")
                                
                except Exception as e:
                    st.error(f"Error generating questions: {str(e)}")
                    st.info("Please check your Groq API key in the .env file")
                    
# Add footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and Groq AI")