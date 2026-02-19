# DevOps Incident Agent (Gemini + ChromaDB + Streamlit)

## Setup

### 1. Install dependencies
pip install -r requirements.txt

### 2. Setup environment variable

Copy:
.env.example → .env

Add your Gemini API key

### 3. Run app

streamlit run streamlit_app.py

## Features

• Gemini API
• ChromaDB vector database
• Guardrails
• Prompt template
• Streamlit UI
• SSL bypass support for hackathons

## Architecture

User → Streamlit → ChromaDB → Gemini → Guardrails → Output
# devops-agent-project
