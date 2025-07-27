# MCP Smart Text Processor

A Python app that uses a Model Control Plane (MCP) to orchestrate three simple ML models (summarization, sentiment analysis, keyword extraction) via a REST API. All model versions and improvements are tracked with Git.

## Features
- Summarize text
- Analyze sentiment
- Extract keywords
- REST API (FastAPI)
- MCP server routes tasks to the correct model
- Git versioning for all model changes

## Example API Request
```json
{
  "task": "summarize",
  "text": "ChatGPT is a powerful AI developed by OpenAI. It can generate text and answer questions."
}
```

## Project Structure
```
mcp-smart-text-processor/
├── mcp_server.py
├── models/
│   ├── sentiment.py
│   ├── summarizer.py
│   └── keywords.py
├── api/
│   └── main.py
├── test_input.json
├── README.md
├── .gitignore
```

## Getting Started
1. Clone the repo
2. Install requirements
3. Run the API server
4. Send requests to `/process`

## Version Control
- Use Git to track all model changes and improvements. 