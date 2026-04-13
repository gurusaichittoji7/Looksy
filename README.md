# Looksy 🔍
An AI-powered search agent built with LangChain, Tavily, and Flask.

## What it does
- Takes a user query as input
- Uses Tavily API to search the live web
- Processes results through an LLM agent (GPT-3.5)
- Returns a smart, summarized answer

## Tech Stack
- **LangChain** — agent orchestration
- **Tavily API** — real-time web search
- **OpenAI GPT-3.5** — language model
- **Flask** — web framework
- **Python** — core language

## How to Run Locally

```bash
# Clone the repo
git clone https://github.com/gurusaichittoji7/looksy.git
cd looksy

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add your API keys
cp .env.example .env
# Edit .env with your keys

# Run the app
python3 app.py
```

## Environment Variables
TAVILY_API_KEY=your_tavily_key
OPENAI_API_KEY=your_openai_key

## Screenshots
Coming soon!


## Author
Gurusai Chittoji — [Portfolio](https://gurusaichittoji7.github.io/Portfolio_Project/)