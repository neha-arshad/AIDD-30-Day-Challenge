# Project Specification 

**Role**: Senior Python AI Engineer  
**Objective**: Build a complete “PDF Study Notes Summarizer & Quiz Generator Agent” using:

- OpenAgents SDK  
- Gemini API  
- Streamlit (recommended UI)  
- PyPDF  
- Context7 MCP Server  
- Gemini CLI  

The CLI must follow this specification step by step to generate the entire project.

## 1. Project Overview
Create an AI agent that reads PDF files, generates clean summaries, and produces quizzes based on the original content. The agent runs through a simple, clean UI and connects to Gemini via the OpenAgents SDK.

**Features**
- PDF upload
- Text extraction with PyPDF
- High-quality summary generation
- Quiz generation (MCQs + optional mixed styles)
- Streamlit UI (or minimal HTML/CSS if preferred)
- Context7 MCP Server for up-to-date tool documentation

This project serves as a complete, working example for students and developers.

## 2. Critical Technical Constraints (Mandatory)
1. **Zero-Bloat Protocol**
   - No extra features
   - No unnecessary comments or print statements
   - No invented SDK syntax
   - Use only documented OpenAgents SDK patterns

2. **API Configuration**
   - Use OpenAgents SDK exclusively
   - Connect Gemini via OpenAI-compatible endpoint
   - Base URL: `https://generativelanguage.googleapis.com/v1beta/openai/`
   - API key from environment variable: `GEMINI_API_KEY`
   - Model: `gemini-2.0-flash`
   - Follow official agent + tool calling syntax

3. **MCP Server Requirement**
   - Connect to Context7 MCP server before writing any agent code
   - Use MCP docs to validate tool structure and function calling
   - Never guess syntax

4. **Recovery Protocol**
   - On any error (SyntaxError, ImportError, AttributeError, etc.): stop, re-query MCP docs, rewrite using only documented patterns

5. **Dependency Management**
   - Use `uv` for environment and packages
   - Install only required libraries
   - No extras

## 3. Project Architecture & File Structure
```text
.
.
├── GEMINI.md                     # Gemini usage rulebook & formatting protocol
├── .env                          # Contains GEMINI_API_KEY (not committed)
├── app.py                        # Main Streamlit application
├── modules/                      # All system logic
│   ├── ai_engine.py              # Summary + quiz generation logic using Gemini
│   ├── pdf_handler.py            # PDF extraction utilities
│   ├── ui_components.py          # UI layout abstractions (buttons, sections)
│   └── utils.py                  # Optional shared helpers
├── requirements.txt              # Auto-generated dependency list
├── README.md                     # Usage instructions
└── run.sh                        # Optional automation script (optional)
