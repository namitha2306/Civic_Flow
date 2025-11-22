# CivicFlow.AI – Multi-Agent Citizen Helpdesk System

CivicFlow.AI is an AI-powered helpdesk system designed to simplify access to government information.
It uses a multi-agent architecture where different AI agents collaborate to search, verify, and summarize official information for citizens in clear and simple language.

The system automatically retrieves information from trusted government domains, processes it through specialized agents, and presents a verified response through a Streamlit interface. CivicFlow.AI aims to reduce the complexity involved in understanding government procedures, schemes, and public services.

---

## Key Features

### Multi-Agent Architecture

The system is composed of the following specialized agents:

* **Query Understanding Agent**
  Interprets the citizen's question and extracts key intent.

* **Research Agent**
  Uses SerpAPI to search for information from trusted government websites such as `.gov.in` and `.nic.in`.

* **Summarizer Agent**
  Uses Gemini Pro to convert complex government text into simple, readable explanations.

* **Verification Agent**
  Validates that the obtained sources are reliable and belong to official domains.

* **Reviewer Agent**
  Evaluates the clarity and accuracy of the final answer and provides feedback for improvement.

* **Finalizer Agent (optional extension)**
  Formats the response for display or storage.

### Verified and Trustworthy Information

All search results are filtered through domain verification to ensure accuracy and prevent misinformation.

### Clear and Simplified Outputs

Gemini Pro is used to rewrite complex government texts into simple and understandable language.

### Streamlit Web Interface

Provides a clean and minimal dashboard for users to ask questions and view structured answers with source links.

### Modular Workflow

The workflow is designed to support feedback loops for improved accuracy. Each agent can function independently or as part of a directed pipeline.

---

## System Architecture

CivicFlow.AI follows a directed workflow:

```
User Input
   ↓
Query Understanding Agent
   ↓
Research Agent (SerpAPI)
   ↓
Summarizer Agent (Gemini Pro)
   ↓
Verification Agent
   ↓
Reviewer Agent
   ↓
Final Response to Streamlit UI
```

Each stage passes processed data to the next agent, and responses are logged for transparency and debugging.

---

## Technology Stack

* Python
* Streamlit
* Gemini Pro (Google Generative AI)
* SerpAPI (Google Search API)
* CrewAI or LangGraph (optional orchestration)
* JSON / SQLite for storage (optional)

---

## Installation

### 1. Clone the Repository

```
git clone https://github.com/your-username/civicflow-ai.git
cd civicflow-ai
```

### 2. Create a Python Virtual Environment

```
python -m venv venv
```

Activate it:

* Windows: `venv\Scripts\activate`
* macOS/Linux: `source venv/bin/activate`

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Set Environment Variables

Configure your API keys:

```
setx SERPAPI_KEY "your_serpapi_key"        # Windows
setx GEMINI_API_KEY "your_gemini_key"

export SERPAPI_KEY="your_serpapi_key"      # macOS/Linux
export GEMINI_API_KEY="your_gemini_key"
```

---

## Running the Application

Run the Streamlit server:

```
streamlit run app.py
```

Open the displayed local URL in your browser.

You can enter any government-related question, such as:

* "How to renew Aadhaar"
* "How to apply for widow pension in Kerala"
* "What are the documents required for a ration card update"

The system will retrieve, summarize, and validate the information and display the response along with verified links.

---

## Project Structure

```
civicflow/
├── agents/
│   ├── research_agent.py
│   ├── summarizer_agent.py
│   ├── verification_agent.py
│   ├── reviewer_agent.py
├── workflow.py
├── app.py
├── requirements.txt
└── README.md
```

---

## How It Works

1. **User enters a query** in the Streamlit application.
2. **Query Understanding Agent** identifies the main intent and keywords.
3. **Research Agent** retrieves official information using SerpAPI.
4. **Summarizer Agent** uses Gemini Pro to generate a simplified explanation.
5. **Verification Agent** checks all URLs to ensure they belong to official government domains.
6. **Reviewer Agent** evaluates clarity and accuracy and provides feedback or triggers a re-run if needed.
7. The final refined answer is displayed to the user along with verified sources.

---

## Future Enhancements

* Support for multiple languages (Malayalam, Hindi, Tamil, etc.)
* Voice input and text-to-speech output
* Integration of more government APIs
* Session memory for conversational interaction
* Enhanced feedback loops with scoring metrics
* Deployable version for public use

---

## Contribution Guidelines

Contributions are welcome.
You can submit issues, feature requests, or pull requests to improve functionality.

---

## License

This project is released under the MIT License. You may use, modify, and distribute it freely under the license terms.
