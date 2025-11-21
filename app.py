import streamlit as st
import ollama
import time
from datetime import datetime
# import logging
# logging.basicConfig(level=logging.INFO)

# Page Config
st.set_page_config(
    page_title="Dual Gemma Model Chat",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Gray robot icon path
ICON_GRAY = "icons/robot.svg"  # Make sure this SVG is dark gray
ICON_REFRESH = "icons/refresh.svg"

# Custom CSS (English font + kept RTL for messages)
st.markdown("""
<style>
    /* --- English Font --- */
    @font-face {
        font-family: 'MyEnglishFont';
        src: url('fonts/Dana-Regular.ttf') format('truetype');
    }

    body, .stApp, .css-1lnq5k9, .css-ffhzg2 {
        font-family: 'MyEnglishFont', sans-serif !important;
    }

    /* --- RTL only for message content --- */
    .rtl {
        direction: rtl;
        text-align: right;
    }

    /* --- LTR for everything else --- */
    .ltr {
        direction: ltr;
        text-align: left;
    }

    /* --- Gradient background gray to white --- */
    .stApp {
        background: linear-gradient(135deg, #b0b0b0 0%, #ffffff 100%) !important;
    }

    /* --- Message cards --- */
    .model-card {
        background: white;
        padding: 1.5rem;
        border-radius: 14px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.15);
        margin-bottom: 1rem;
        direction: rtl;
    }

    /* --- Model 1 message --- */
    .message-model1 {
        background: linear-gradient(135deg, #d0eaff, #e8f5ff);
        border-right: 5px solid #1890ff;
        padding: 1rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        direction: rtl;
        text-align: right;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    /* --- Model 2 message --- */
    .message-model2 {
        background: linear-gradient(135deg, #e1ffd4, #f4fff1);
        border-right: 5px solid #52c41a;
        padding: 1rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        direction: rtl;
        text-align: right;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    /* --- Speaker name with gray icon --- */
    .speaker-name img {
        width: 20px;
        height: 20px;
        filter: grayscale(100%) brightness(50%);
        vertical-align: middle;
    }

    .speaker-name {
        font-weight: bold;
        color: #333;
        margin-bottom: 0.5rem;
        font-size: 1.1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .timestamp {
        font-size: 0.8rem;
        color: #777;
        margin-top: 4px;
    }

    /* --- Buttons with purple-blue gradient --- */
    .stButton>button {
        background: linear-gradient(135deg, #6a11cb, #2575fc);
        color: white;
        border-radius: 10px;
        padding: 0.6rem 1.2rem;
        font-size: 1rem;
        border: none;
        transition: 0.25s;
    }

    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(135deg, #5b0eb2, #1d63d6);
    }
</style>
""", unsafe_allow_html=True)

# Session state initialization
if 'conversation' not in st.session_state:
    st.session_state.conversation = []
if 'is_running' not in st.session_state:
    st.session_state.is_running = False
if 'stop_requested' not in st.session_state:
    st.session_state.stop_requested = False

def call_model(model_name, system_prompt, user_message, conversation_history=""):
    """Call model via Ollama"""
    try:
        full_prompt = f"""{system_prompt}

Conversation History:
{conversation_history}

New Message: {user_message}

Response (concise and natural):"""

        response = ollama.generate(
            model=model_name,
            prompt=full_prompt,
            options={'temperature': 0.8, 'num_predict': 150, 'top_p': 0.9}
        )
        return response['response'].strip()
    except Exception as e:
        return f"❌ Model call error: {str(e)}"

def format_conversation_history(messages, max_messages=4):
    recent = messages[-max_messages:] if len(messages) > max_messages else messages
    history = ""
    for msg in recent:
        history += f"{msg['speaker']}: {msg['message']}\n"
    return history

# Header
st.markdown("<h1 style='text-align: center; color: black;'>🤖 Dual Gemma Model Chat</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray; margin-bottom: 2rem;'>Automatic conversation between two language models</p>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## ⚙️ Settings")
    model1_name = st.selectbox("Model 1:", ["gemma3:4b", "gemma3n:e4b"])
    model1_role = st.text_input("Model 1 Role:", "Physics Teacher")
    model1_prompt = st.text_area("Model 1 System Prompt:", "You are a patient physics teacher...", height=120)

    st.markdown("---")
    model2_name = st.selectbox("Model 2:", ["gemma3:4b", "gemma3n:e4b"], index=1)
    model2_role = st.text_input("Model 2 Role:", "Curious Student")
    model2_prompt = st.text_area("Model 2 System Prompt:", "You are a curious student...", height=120)

    st.markdown("---")
    max_turns = st.slider("Number of turns:", 2, 15, 8)
    initial_message = st.text_input("Initial message:", "Hi! Let's talk about gravity.")

    st.markdown("---")
    st.info(f"Messages count: {len(st.session_state.conversation)}")
    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.conversation = []
        st.session_state.is_running = False
        st.session_state.stop_requested = False
        st.rerun()

# Control buttons
col1, col2, col3 = st.columns([1,1,1])
with col1:
    start_button = st.button("▶ Start Chat", use_container_width=True, disabled=st.session_state.is_running)
with col2:
    stop_button = st.button("⏸ Stop", use_container_width=True, disabled=not st.session_state.is_running)
with col3:
    if st.button("🔄️ Refresh View", use_container_width=True , ):
        st.rerun()

# Conversation logic
if start_button:
    st.session_state.is_running = True
    st.session_state.stop_requested = False
    st.session_state.conversation = []
    conversation_container = st.container()
    current_message = initial_message
    progress_bar = st.progress(0)
    status_text = st.empty()

    for turn in range(max_turns):
        if st.session_state.stop_requested:
            status_text.warning("⏸ Conversation stopped")
            break
        progress_bar.progress((turn+1)/max_turns)

        # Model 1
        status_text.info(f"🔵 {model1_role} is responding...")
        history = format_conversation_history(st.session_state.conversation)
        response1 = call_model(model1_name, model1_prompt, current_message, history)
        st.session_state.conversation.append({
            'speaker': model1_role,
            'message': response1,
            'model': model1_name,
            'timestamp': datetime.now().strftime("%H:%M:%S"),
            'type': 'model1'
        })
        with conversation_container:
            st.markdown(f"""
            <div class="message-model1">
                <div class="speaker-name">
                    <img src="{ICON_GRAY}">
                    {model1_role} ({model1_name})
                </div>
                <div class="rtl">{response1}</div>
                <div class="timestamp">{st.session_state.conversation[-1]['timestamp']}</div>
            </div>
            """, unsafe_allow_html=True)
        time.sleep(1)
        if st.session_state.stop_requested: break

        # Model 2
        status_text.info(f"🟢 {model2_role} is responding...")
        history = format_conversation_history(st.session_state.conversation)
        response2 = call_model(model2_name, model2_prompt, response1, history)
        st.session_state.conversation.append({
            'speaker': model2_role,
            'message': response2,
            'model': model2_name,
            'timestamp': datetime.now().strftime("%H:%M:%S"),
            'type': 'model2'
        })
        with conversation_container:
            st.markdown(f"""
            <div class="message-model2">
                <div class="speaker-name">
                    <img src="{ICON_GRAY}">
                    {model2_role} ({model2_name})
                </div>
                <div class="rtl">{response2}</div>
                <div class="timestamp">{st.session_state.conversation[-1]['timestamp']}</div>
            </div>
            """, unsafe_allow_html=True)
        current_message = response2
        time.sleep(1)

    st.session_state.is_running = False
    progress_bar.progress(1.0)
    status_text.success(f"✅ Conversation finished ({len(st.session_state.conversation)} messages)")

if stop_button:
    st.session_state.stop_requested = True
    st.session_state.is_running = False

# Display conversation history
if st.session_state.conversation:
    st.markdown("---")
    st.markdown("## 💬 Conversation History")
    for msg in st.session_state.conversation:
        cls = "message-model1" if msg['type'] == 'model1' else "message-model2"
        st.markdown(f"""
        <div class="{cls}">
            <div class="speaker-name">
                <img src="{ICON_GRAY}">
                {msg['speaker']} ({msg['model']})
            </div>
            <div class="rtl">{msg['message']}</div>
            <div class="timestamp">{msg['timestamp']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    if st.button("💾 Save Conversation", use_container_width=True):
        text = f"Conversation between {model1_role} and {model2_role}\nDate: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n" + "="*50 + "\n\n"
        for msg in st.session_state.conversation:
            text += f"{msg['speaker']} ({msg['timestamp']}):\n{msg['message']}\n\n"
        st.download_button(
            "📥 Download Text File",
            data=text,
            file_name=f"conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
            use_container_width=True
        )
else:
    st.info("💡 Configure settings in the sidebar and click 'Start Chat' to begin.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; padding: 1rem;'>
    <p>Made by Zahra</p>
    <p style='font-size: 0.8rem;'>Models: Gemma 3 & Gemma 3n | Framework: Ollama + Streamlit</p>
</div>
""", unsafe_allow_html=True)