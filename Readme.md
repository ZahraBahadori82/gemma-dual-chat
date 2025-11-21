# 🤖 Dual Gemma Model Chat

An interactive user interface for automatic conversation between two Gemma language models running locally.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Ollama](https://img.shields.io/badge/Ollama-Latest-green.svg)

---

## 📋 Table of Contents

- [Introduction](#-introduction)
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation & Setup](#-installation--setup)
- [Usage Guide](#-usage-guide)
- [Project Structure](#-project-structure)
- [Screenshots](#-screenshots)
- [Technical Architecture](#-technical-architecture)
- [Troubleshooting](#-troubleshooting)
- [Advanced Settings](#-advanced-settings)

---

## 🎯 Introduction

This project was developed as part of a job interview task and enables **automatic dialogue** between two Gemma language models. Users can define a **Role** and **System Prompt** for each model and observe natural, intelligent interaction between them.

### 🎓 Use Cases:
- Simulating educational conversations (teacher-student)
- Testing and comparing different model behaviors
- Generating creative content (storytelling, debates)
- Research in Multi-Agent Dialogue Systems

---

## ✨ Features

- ✅ **Fully Local Execution**: No internet, API keys, or external services required
- ✅ **Gemma Model Support**: Gemma 3 (4B), Gemma 3n (4B)
- ✅ **Role & Prompt Configuration**: Complete control over each model's behavior
- ✅ **Persian UI**: Designed for Persian-speaking users
- ✅ **Real-time Display**: Live conversation view with distinct color coding
- ✅ **Context Management**: Intelligent conversation history maintenance
- ✅ **Flow Control**: Start, Stop, and Clear buttons
- ✅ **Save Conversations**: Download history as `.txt` file
- ✅ **Progress Tracking**: Visual progress bar during conversation
- ✅ **Stats & Reports**: Display message count and response times

---

## 📦 Prerequisites

### Recommended Hardware:
```
💾 RAM: Minimum 8GB (16GB for optimal performance)
💿 Disk Space: 5-10GB for models
🖥️ CPU: Modern processor (GPU optional for faster inference)
```

### Software:
- **Python**: Version 3.8 or higher
- **Ollama**: For running Gemma models locally
- **Python Packages**: Streamlit and Ollama

---

## 🚀 Installation & Setup

### Step 1️⃣: Install Ollama

#### Windows:
1. Visit [ollama.com/download](https://ollama.com/download)
2. Download and run the Windows installer
3. Ollama will install and start automatically

#### Linux/Mac:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Test Installation:**
```bash
ollama --version
```

---

### Step 2️⃣: Download Gemma Models

```bash
# Start Ollama service (runs in background)
ollama serve

# Download models (in a new terminal)
ollama run gemma3n
ollama run gemma3n:e4b

# Check installed models
ollama list
```

**Expected Output:**
```
NAME            ID              SIZE    MODIFIED
gemma3:4b       abc123def456    3.3GB   2 minutes ago
gemma3n:e4b     def789ghi012    7.5GB   5 minutes ago
```

---

### Step 3️⃣: Install Python Packages

```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**Contents of `requirements.txt`:**
```txt
streamlit>=1.28.0
ollama>=0.1.0
```

---

### Step 4️⃣: Test System

```bash
# Run test script
python test_script.py
```

This script checks:
- ✅ Python version
- ✅ Ollama installation
- ✅ Ollama service status
- ✅ Installed models
- ✅ Model inference (functionality test)
- ✅ Streamlit installation
- ✅ Disk space

---

### Step 5️⃣: Run Application

```bash
streamlit run app.py
```

The application will run at:
```
🌐 Local URL: http://localhost:8501
🔗 Network URL: http://192.168.x.x:8501
```

---

## 📖 Usage Guide

### 1. Initial Settings (Sidebar)

#### 🔵 Model 1:
- **Select Model**: `gemma3:4b`, `gemma3n:e4b`
- **Model Role**: e.g., "Physics Teacher"
- **System Prompt**: 
  ```
  You are a patient and precise physics teacher who explains 
  concepts in simple language. Give short and helpful answers.
  ```

#### 🟢 Model 2:
- **Select Model**: Choose a different model for variety
- **Model Role**: e.g., "Curious Student"
- **System Prompt**:
  ```
  You are a curious student who asks many questions and wants 
  to learn more. Ask short and relevant questions.
  ```

#### ⚙️ Conversation Settings:
- **Number of Turns**: 2 to 15 (default: 8)
- **Initial Message**: Message that starts the conversation

---

### 2. Start Conversation

1. Click **"▶️ Start Conversation"** button
2. Model 1 receives initial message and responds
3. Model 2 receives Model 1's response and replies
4. Process continues for the specified number of turns

---

### 3. Control Conversation

- **⏸️ Stop**: Pause conversation at any time
- **🔄 View Conversation**: Refresh page to view history
- **🗑️ Clear**: Delete all history and start fresh

---

### 4. Save & Export

After conversation ends:
- Click **"💾 Save Conversation"**
- `.txt` file containing full conversation will be downloaded

**Output File Format:**
```
Conversation between Physics Teacher and Curious Student
Date: 2025-11-21 21:53:12
==================================================

Physics Teacher (21:53:15):
Gravity is one of the four fundamental forces in nature...

Curious Student (21:53:20):
Why do all objects fall at the same speed?
...
```

---

## 📂 Project Structure

```
PROJECT/
│
├── 📁 fonts/                          # Project fonts
│   └── Dana-Regular.ttf
│
├── 📁 icons/                          # SVG icons
│   ├── checkmark.svg
│   ├── clear.svg
│   ├── download.svg
│   ├── model.svg
│   ├── pause.svg
│   ├── play.svg
│   ├── play1.svg
│   ├── refresh.svg
│   ├── robot.svg
│   ├── save.svg
│   ├── setting.svg
│   └── trash.svg
│
├── 📁 result/                         # Results and outputs
│   ├── conversation_20251121_021235.txt
│   ├── conversation_20251121_021649.txt
│   ├── Screenshot 2025-11-21 021420.png
│   ├── Screenshot 2025-11-21 021449.png
│   ├── Screenshot 2025-11-21 021503.png
│   ├── Screenshot 2025-11-21 021551.png
│   ├── Screenshot 2025-11-21 021809.png
│   ├── Screenshot 2025-11-21 022145.png
│   ├── Screenshot 2025-11-21 024324.png
│   ├── Screenshot 2025-11-21 111606.png
│   └── streamlit-app-2025-11-21-02-11-44.webm
│
├── 📄 app.py                          # Main Streamlit file
├── 📄 requirements.txt                # Python dependencies
├── 📄 test_script.py                  # System test script
└── 📄 README.md                       # This file
```

---

## 📸 Screenshots

Sample screenshots from the UI and results are available in the `result/` folder:

### Main UI:
![Main UI](result/Screenshot%202025-11-21%20111606.png)

### Conversation in Progress:
![Conversation](result/Screenshot%202025-11-21%20024324.png)

### Settings Panel:
![Settings](result/Screenshot%2025-11-21%021503.png)
![Settings](result/Screenshot%2025-11-21%021551.png)


**Demo Video:**
- `result/streamlit-app-2025-11-21-02-11-44.webm`

---

## 🏗️ Technical Architecture

### Workflow:

```
┌─────────────┐
│    User     │
│  User Input │
└──────┬──────┘
       │
       ▼
┌─────────────────────────┐
│   Streamlit Frontend    │
│  - UI Components        │
│  - Session State        │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│   Conversation Loop     │
│  - Turn Management      │
│  - Context Building     │
└──────┬──────────┬───────┘
       │          │
       ▼          ▼
┌──────────┐  ┌──────────┐
│ Model 1  │  │ Model 2  │
│ (Gemma)  │  │ (Gemma)  │
└────┬─────┘  └─────┬────┘
     │              │
     └──────┬───────┘
            ▼
    ┌───────────────┐
    │ Ollama Server │
    │  (localhost)  │
    └───────────────┘
```

### Conversation Mechanism:

```python
# Turn 1
Message_0 = "Hello! Let's talk about gravity."
Response_1 = Model_1(system_prompt_1 + Message_0)

# Turn 2
Response_2 = Model_2(system_prompt_2 + Response_1 + History)

# Turn 3
Response_3 = Model_1(system_prompt_1 + Response_2 + History)

# ... continues for N turns
```

### Context Management:

To prevent prompt length issues and maintain coherence:
- **Last 4 messages** are provided as context to the model
- Complete history is stored in `st.session_state`
- Each message includes: `speaker`, `message`, `model`, `timestamp`

---

## 🔧 Troubleshooting

### ❌ "Connection Refused" Error

**Cause:** Ollama service is not running

**Solution:**
```bash
# Start Ollama
ollama serve
```

---

### ❌ "Model not found" Error

**Cause:** Model has not been downloaded

**Solution:**
```bash
# Check available models
ollama list

# Download required model
ollama pull gemma3:4b
ollama pull gemma3n:e4b

```

---

### ⚠️ Very Slow Performance

**Cause:** Using CPU for inference

**Solutions:**
1. Use smaller models (`gemma2:2b`)
2. Reduce `num_predict` (in `app.py`)
3. Decrease number of turns
4. Use GPU if available

```python
# In app.py, line ~220
options={
    'temperature': 0.8,
    'num_predict': 100,  # Reduced from 150 to 100
}
```

---

### ⚠️ Repetitive Responses

**Solutions:**
1. Increase `temperature`:
```python
'temperature': 0.9  # Instead of 0.8
```

2. Write more specific system prompts
3. Use different models for each role

---

### ❌ "Out of Memory" Error

**Solutions:**
- Use the same model for both roles instead of two different ones
- Choose a smaller model
- Close other applications

---

## ⚙️ Advanced Settings

### Adjusting Model Parameters:

In `app.py`, function `call_model`:

```python
response = ollama.generate(
    model=model_name,
    prompt=full_prompt,
    options={
        'temperature': 0.8,      # 0.0 (deterministic) to 1.0 (creative)
        'num_predict': 150,      # Maximum response tokens
        'top_p': 0.9,           # Nucleus sampling
        'top_k': 40,            # Number of candidate tokens
        'repeat_penalty': 1.1,  # Repetition penalty
    }
)
```

### Adding New Models:

```bash
# Download other models
ollama pull llama2:7b
ollama pull mistral:7b
ollama pull codellama:7b
```

Then add to model list in `app.py`:

```python
model1_name = st.selectbox(
    "Select Model:",
    ["gemma3:4b","gemma3n:e4b" ,"gemma2:9b", "gemma2:2b", 
     "llama2:7b", "mistral:7b"],  # Added
    key="model1_select"
)
```

---

## 📊 Model Comparison

| Model | Size | Speed (CPU) | Response Quality | RAM Required |
|-------|------|-------------|------------------|--------------|
| **gemma2:2b** | 1.5GB | ⭐⭐⭐⭐⭐ Fast | ⭐⭐⭐ Good | 4GB |
| **gemma3:4b** | 3.3GB | ⭐⭐⭐⭐ Fast | ⭐⭐⭐⭐ Excellent | 9GB |
| **gemma3n:e4b** | 7.5GB | ⭐⭐⭐ Medium | ⭐⭐⭐⭐⭐ Outstanding | 13GB |

**Recommendations:**
- For quick testing: `gemma2:2b`
- For speed/quality balance: `gemma3:4b`
- For best quality: `gemma3n:e4b`

---

## 🎯 Usage Scenarios

### 1. Education:
```
Role 1: Math Teacher
Role 2: Student
Topic: Teaching mathematical concepts
```

### 2. Debate:
```
Role 1: Technology Advocate
Role 2: Technology Critic
Topic: Impact of AI
```

### 3. Storytelling:
```
Role 1: Story Narrator
Role 2: Main Character
Topic: A sci-fi adventure
```

### 4. Job Interview:
```
Role 1: Interviewer
Role 2: Candidate
Topic: Programming interview
```

---

## 📝 Developer Notes

### Development Time:
- Design & Programming: **6 hours**
- Testing & Debugging: **3 hours**
- Documentation: **2 hours**

### Main Challenges:
1. ✅ Memory management for two simultaneous models
2. ✅ Preventing repetitive loops
3. ✅ Designing responsive UI with Streamlit
4. ✅ Context management for coherence

### Future Improvements:
- [ ] Support for multiple models (3+)
- [ ] Export to JSON/PDF
- [ ] Display metrics (tokens/sec, latency)
- [ ] Multi-language support
- [ ] Langchain integration

---

## 📚 Resources

- [Ollama Documentation](https://github.com/ollama/ollama)
- [Streamlit Documentation](https://docs.streamlit.io)
- [Gemma Models](https://ai.google.dev/gemma)
- [Python Ollama Library](https://github.com/ollama/ollama-python)

---

## 📧 Contact & Support

For questions and support:
- **Developer**: [Zahra Bahadori]
- **Email**: Zbahadori107@gmail.com

---

## 🙏 Acknowledgments

- **Ollama Team** for the excellent local model execution tool
- **Streamlit** for the simple yet powerful framework
- **Google DeepMind** for open-source Gemma models

---

## 📜 License

This project is free for personal and educational use.

---

<div align="center">

**Built for Job Interview Task**

`Version 1.0.0 | November 2025`

</div>
