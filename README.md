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

Or set environment variables:

$env:GROQ_API_KEY="GROQ API KEY"
$env:OPENAI_API_KEY="OPEN AI APK KEY"

To reset:

$env:GROQ_API_KEY = $null
$env:OPENAI_API_KEY = $null


# Run
streamlit run app.py