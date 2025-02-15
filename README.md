# llm-automation-agent
# LLM-Based Automation Agent

## Overview
The **LLM-Based Automation Agent** is a FastAPI-based system that automates various operational and business tasks using a Large Language Model (LLM). The agent accepts natural language commands and executes multi-step processes to generate precise and verifiable outputs.

## Features
- Executes **Phase A tasks (A1-A10)** related to file handling, data extraction, formatting, sorting, and computation.
- Handles **Phase B tasks (B1-B10)** including security enforcement, API calls, Git operations, SQL queries, web scraping, and media processing.
- Uses **GPT-4o-Mini** for natural language parsing and specific AI-driven tasks.
- Provides **REST API endpoints** for task execution and file retrieval.
- Fully containerized using **Docker** for easy deployment.

## Folder Structure
```
llm-automation-agent/
│── src/
│   ├── api.py                # FastAPI API endpoints
│   ├── agent.py              # Task execution logic
│   ├── llm_handler.py        # GPT-4o-Mini integration
│   ├── utils.py              # Helper functions
│── data/                     # Working directory for task-related files
│── tests/                    # Unit and integration tests
│── Dockerfile                 # Docker containerization
│── requirements.txt           # Dependencies
│── config.py                  # Configuration management
│── README.md                  # Documentation
│── LICENSE                    # MIT License
```

## Installation & Setup
### 1️⃣ Clone the repository
```sh
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Install dependencies
Ensure you have **Python 3.9+** installed.
```sh
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Set API Token
Export your AI Proxy token for GPT-4o-Mini integration.
```sh
export AIPROXY_TOKEN="your-token-here"
```

### 4️⃣ Run the API Server
```sh
uvicorn src.api:app --host 0.0.0.0 --port 8000
```
The API is now available at `http://localhost:8000`.

### 5️⃣ Running with Docker
```sh
docker build -t llm-automation-agent .
docker run -e AIPROXY_TOKEN="your-token-here" -p 8000:8000 llm-automation-agent
```

## API Usage
### Execute a Task
```sh
curl -X POST "http://localhost:8000/run?task=Format+/data/format.md+with+prettier+3.4.2"
```

### Read a File
```sh
curl -X GET "http://localhost:8000/read?path=/data/format.md"
```

## Task Implementations
### Phase A: Operational Tasks
- **A1**: Install `uv` and execute `datagen.py`
- **A2**: Format `/data/format.md` using `prettier`
- **A3**: Count Wednesdays in `/data/dates.txt`
- **A4**: Sort contacts in `/data/contacts.json`
- **A5**: Extract first lines of the latest logs
- **A6**: Index markdown files
- **A7**: Extract email sender using an LLM
- **A8**: Extract credit card number using OCR
- **A9**: Find the most similar comments using embeddings
- **A10**: Compute total sales of "Gold" tickets in a SQLite database

### Phase B: Business Tasks
- **B1**: Security checks (preventing unauthorized data access/deletion)
- **B2**: Fetch data from an API
- **B3**: Clone a Git repository and make a commit
- **B4**: Execute SQL queries in SQLite/DuckDB
- **B5**: Scrape data from a website
- **B6**: Compress or resize an image
- **B7**: Transcribe audio from an MP3 file
- **B8**: Convert Markdown to HTML
- **B9**: Filter and return JSON data from a CSV

## License
This project is licensed under the MIT License.
