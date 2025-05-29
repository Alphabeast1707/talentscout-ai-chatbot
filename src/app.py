import streamlit as st
import os
from dotenv import load_dotenv
from prompts import generate_tech_questions, generate_behavioral_questions
from utils.helpers import validate_tech_stack, sanitize_input, get_difficulty_description
from conversation import (
    ConversationManager, ConversationState, CandidateProfile,
    format_conversation_message, display_candidate_profile
)

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="TalentScout AI Chatbot", 
    page_icon="🤖", 
    layout="wide"
)

# Initialize conversation manager
conv_manager = ConversationManager()
conv_manager.initialize_session()

# Main title
st.title("🤖 TalentScout AI Chatbot")
st.markdown("**Your AI-powered interview preparation assistant**")

# Display candidate profile in sidebar
display_candidate_profile(st.session_state.candidate_profile)

# Sidebar with settings and controls
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
    
    # Conversation controls
    st.markdown("### 🔄 Conversation Controls")
    
    if st.button("🆕 Start New Conversation", use_container_width=True):
        # Reset all session state
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        conv_manager.initialize_session()
        st.rerun()
    
    if st.button("🔄 Reset Current Step", use_container_width=True):
        if st.session_state.conversation_state == ConversationState.GREETING:
            st.session_state.conversation_state = ConversationState.GREETING
        elif st.session_state.conversation_state == ConversationState.COLLECTING_INFO:
            st.session_state.candidate_profile = CandidateProfile()
        elif st.session_state.conversation_state == ConversationState.TECH_STACK_INPUT:
            st.session_state.candidate_profile.tech_stack = []
        st.rerun()
    
    # Show conversation state
    st.markdown("### 🔍 Current State")
    state_names = {
        ConversationState.GREETING: "👋 Greeting",
        ConversationState.COLLECTING_INFO: "📝 Collecting Info",
        ConversationState.TECH_STACK_INPUT: "💻 Tech Stack",
        ConversationState.GENERATING_QUESTIONS: "⚡ Generating",
        ConversationState.FOLLOW_UP: "🎯 Question Type",
        ConversationState.ENDING: "👋 Ending"
    }
    current_state_name = state_names.get(st.session_state.conversation_state, "Unknown")
    st.info(f"**State:** {current_state_name}")
    
    st.markdown("### About TalentScout AI")
    st.info("AI-powered conversational interview question generator using Groq's fast inference.")
    
    st.markdown("### 💡 Tips")
    st.write("• Be natural - type as you would speak")
    st.write("• Provide complete information when asked") 
    st.write("• Say 'bye' or 'done' to end conversation")
    st.write("• Use 'help' if you need guidance")

# Main conversation area
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 💬 Conversation")
    
    # Display conversation history
    if st.session_state.conversation_history:
        with st.container():
            for message in st.session_state.conversation_history[-10:]:  # Show last 10 messages
                format_conversation_message(message["role"], message["content"])
    
    # Get current conversation prompt
    current_prompt = conv_manager.get_conversation_prompt(st.session_state.conversation_state)
    
    # Show current prompt if it's the first message or state changed
    if not st.session_state.conversation_history or \
       (st.session_state.conversation_history and 
        st.session_state.conversation_history[-1]["role"] != "assistant"):
        format_conversation_message("assistant", current_prompt)
        st.session_state.conversation_history.append({
            "role": "assistant", 
            "content": current_prompt
        })

with col2:
    st.markdown("### 🎯 Quick Actions")
    
    # Show generated questions if available
    if st.session_state.generated_questions:
        st.markdown("### 📝 Generated Questions")
        
        questions_by_type = {}
        for q_data in st.session_state.generated_questions:
            q_type = q_data.get("type", "General")
            if q_type not in questions_by_type:
                questions_by_type[q_type] = []
            questions_by_type[q_type].append(q_data["question"])
        
        for q_type, questions in questions_by_type.items():
            with st.expander(f"{q_type} Questions ({len(questions)})"):
                for i, question in enumerate(questions, 1):
                    st.write(f"**{i}.** {question}")
    
    # Show helpful info based on current state
    if st.session_state.conversation_state == ConversationState.TECH_STACK_INPUT:
        st.markdown("### 💻 Tech Stack Examples")
        st.code("Python, Django, PostgreSQL, Redis", language="text")
        st.code("React, Node.js, MongoDB, AWS", language="text")
        st.code("Java, Spring Boot, MySQL, Docker", language="text")
    
    elif st.session_state.conversation_state == ConversationState.FOLLOW_UP:
        st.markdown("### 🎯 Question Types")
        st.write("**Technical:** Coding, algorithms, system design")
        st.write("**Behavioral:** STAR method, leadership, problem-solving")
        st.write("**Both:** Complete interview preparation")

# User input area
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input(
        "💬 Your message:", 
        placeholder="Type your message here...",
        help="Be natural - I understand conversational language!"
    )
    
    col1, col2, col3 = st.columns([1, 1, 2])
    
    with col1:
        submit = st.form_submit_button("Send 📤", use_container_width=True)
    
    with col2:
        help_button = st.form_submit_button("Help ❓", use_container_width=True)
    
    if help_button:
        user_input = "help"
        submit = True

# Process user input
if submit and user_input.strip():
    # Add user message to history
    st.session_state.conversation_history.append({
        "role": "user",
        "content": user_input
    })
    
    # Check for conversation ending
    if conv_manager.detect_conversation_ending(user_input):
        st.session_state.conversation_state = ConversationState.ENDING
        response = conv_manager.get_conversation_prompt(ConversationState.ENDING)
        
        st.session_state.conversation_history.append({
            "role": "assistant",
            "content": response
        })
        st.rerun()
    
    # Process based on current state
    if st.session_state.conversation_state == ConversationState.GREETING:
        # Parse initial information
        profile, issues = conv_manager.parse_user_info(user_input, st.session_state.candidate_profile)
        st.session_state.candidate_profile = profile
        
        if not issues:
            # All basic info collected, move to tech stack
            st.session_state.conversation_state = ConversationState.TECH_STACK_INPUT
            response = conv_manager.get_conversation_prompt(ConversationState.TECH_STACK_INPUT)
        else:
            # Need more information
            st.session_state.conversation_state = ConversationState.COLLECTING_INFO
            response = conv_manager.get_conversation_prompt(ConversationState.COLLECTING_INFO)
            response += f"\n\n**Still needed:** {', '.join(issues)}"
    
    elif st.session_state.conversation_state == ConversationState.COLLECTING_INFO:
        # Continue collecting missing information
        profile, issues = conv_manager.parse_user_info(user_input, st.session_state.candidate_profile)
        st.session_state.candidate_profile = profile
        
        if not issues:
            st.session_state.conversation_state = ConversationState.TECH_STACK_INPUT
            response = conv_manager.get_conversation_prompt(ConversationState.TECH_STACK_INPUT)
        else:
            response = f"Great! I got some information. **Still needed:** {', '.join(issues)}\n\n"
            response += conv_manager.get_conversation_prompt(ConversationState.COLLECTING_INFO)
    
    elif st.session_state.conversation_state == ConversationState.TECH_STACK_INPUT:
        # Extract technologies
        techs = conv_manager.extract_tech_stack(user_input)
        
        if techs:
            st.session_state.candidate_profile.tech_stack = techs
            st.session_state.conversation_state = ConversationState.FOLLOW_UP
            response = f"Excellent! I found these technologies: **{', '.join(techs)}**\n\n"
            response += conv_manager.get_conversation_prompt(ConversationState.FOLLOW_UP)
        else:
            response = "I couldn't identify specific technologies from your input. "
            response += conv_manager.get_conversation_prompt(ConversationState.TECH_STACK_INPUT)
    
    elif st.session_state.conversation_state == ConversationState.FOLLOW_UP:
        # Determine question type and generate
        user_input_lower = user_input.lower()
        
        with st.spinner("🤖 Generating your personalized interview questions..."):
            try:
                questions_generated = []
                
                if any(word in user_input_lower for word in ['technical', 'tech', 'coding', 'programming']):
                    # Generate technical questions
                    tech_questions = generate_tech_questions(
                        ", ".join(st.session_state.candidate_profile.tech_stack),
                        st.session_state.candidate_profile.position,
                        st.session_state.candidate_profile.experience,
                        selected_model
                    )
                    
                    for q in tech_questions:
                        if q.strip():
                            questions_generated.append({"type": "Technical", "question": q.strip()})
                
                elif any(word in user_input_lower for word in ['behavioral', 'behaviour', 'soft', 'experience']):
                    # Generate behavioral questions
                    behavioral_questions = generate_behavioral_questions(
                        st.session_state.candidate_profile.position,
                        st.session_state.candidate_profile.experience,
                        selected_model
                    )
                    
                    for q in behavioral_questions:
                        if q.strip():
                            questions_generated.append({"type": "Behavioral", "question": q.strip()})
                
                else:
                    # Generate both types
                    tech_questions = generate_tech_questions(
                        ", ".join(st.session_state.candidate_profile.tech_stack),
                        st.session_state.candidate_profile.position,
                        st.session_state.candidate_profile.experience,
                        selected_model
                    )
                    
                    behavioral_questions = generate_behavioral_questions(
                        st.session_state.candidate_profile.position,
                        st.session_state.candidate_profile.experience,
                        selected_model
                    )
                    
                    for q in tech_questions:
                        if q.strip():
                            questions_generated.append({"type": "Technical", "question": q.strip()})
                    
                    for q in behavioral_questions:
                        if q.strip():
                            questions_generated.append({"type": "Behavioral", "question": q.strip()})
                
                st.session_state.generated_questions = questions_generated
                st.session_state.conversation_state = ConversationState.ENDING
                
                response = f"🎉 **Perfect! I've generated {len(questions_generated)} personalized interview questions for you!**\n\n"
                response += "**Your questions are now displayed in the sidebar.** ➡️\n\n"
                response += "**Interview Preparation Tips:**\n"
                response += "• **Practice STAR method** for behavioral questions (Situation, Task, Action, Result)\n"
                response += "• **Review fundamental concepts** related to your tech stack\n"
                response += "• **Prepare specific examples** from your experience\n"
                response += "• **Research the company** and role requirements\n\n"
                response += "**Would you like me to:**\n"
                response += "• Generate more questions for a different role?\n"
                response += "• Start over with new information?\n"
                response += "• End this session?\n\n"
                response += "*Just let me know! Say 'bye' when you're ready to finish.*"
                
            except Exception as e:
                response = f"❌ **I encountered an error generating questions:** {str(e)}\n\n"
                response += "This might be due to API connectivity. Please check:\n"
                response += "• Your internet connection\n"
                response += "• Groq API key configuration\n\n"
                response += "Would you like to try again or need help with setup?"
    
    else:
        # Fallback response
        response = conv_manager.generate_fallback_response(user_input, st.session_state.conversation_state)
    
    # Add response to history
    st.session_state.conversation_history.append({
        "role": "assistant",
        "content": response
    })
    
    st.rerun()

# Footer
st.markdown("---")
st.markdown("**🤖 TalentScout AI Chatbot** • Built with ❤️ using Streamlit and Groq AI • *Natural conversation, personalized questions*")