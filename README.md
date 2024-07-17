# Setup

**Virtual environment**

python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

**API Keys**

Create a .streamlit/secrets.toml file with the API keys:

```
GROQ_API_KEY="YOUR_GROQ_API_KEY"
OPENAI_API_KEY="YOUR_OPEAI_API_KEY"
```

# Run
streamlit run app.py