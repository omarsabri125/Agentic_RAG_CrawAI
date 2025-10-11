# 🧠 Intelligent RAG Crew — Multi-Agent Information Retrieval System

## 📄 Overview

This project implements a **multi-agent RAG (Retrieval-Augmented Generation) pipeline** using **CrewAI**.  
The system intelligently routes user questions, retrieves relevant information from PDFs or the web, evaluates factual accuracy, and produces a final concise answer.

The workflow is structured into **five coordinated agents**, each responsible for a specific reasoning and validation step.

---

## 🧩 System Architecture
```

│ 1️⃣ Router Agent │ → Decides whether to search the web or use local data
└─────────┬────────────┘
           │
┌─────────▼────────────┐
│ 2️⃣ Retriever Agent │ → Retrieves information using Tavily or PDFSearch
└─────────┬────────────┘
           │
┌─────────▼────────────┐
│ 3️⃣ Grader Agent │ → Evaluates semantic relevance of retrieved content
└─────────┬────────────┘
           │
┌─────────▼────────────┐
│ 4️⃣ Hallucination Grader │ → Checks factual grounding ("yes" / "no")
└─────────┬────────────┘
           │
┌─────────▼────────────┐
│ 5️⃣ Answer Agent │ → Produces final concise answer or triggers web search
└──────────────────────┘
```

---

## ⚙️ Components

| Component     | Description |
|---------------|-------------|
| `agents`   | Defines and initializes all agents (Router, Retriever, Grader, Hallucination, Answer). |
| `tasks`    | Defines structured **Pydantic-based tasks** for each agent. Each task specifies input/output schema and logic. |
| `tools`    | Provides the tools used by the agents — including `PDFSearchTool` and `TavilySearch`. |
| `workflow.py`     | Orchestrates the workflow: initializes tools, agents, tasks, and executes them sequentially using the CrewAI process. |

---

## 🧱 Pipeline Logic

**Router Agent**  
Determines whether the query should be answered from the PDF (vectorstore) or via a web search.

**Retriever Agent**  
Fetches relevant content using the appropriate tool:  
- `pdf_tool` for local vectorstore retrieval  
- `create_tavily_search` for live web retrieval  

**Grader Agent**  
Assesses semantic relevance of retrieved results to the input question.

**Hallucination Grader**  
Ensures that the answer is factually grounded in the retrieved evidence (returns `"yes"` or `"no"`).

**Answer Agent**  
Produces a clean final JSON response:  
- If `grounded = "yes"` → returns a concise answer  
- If `grounded = "no"` → triggers a web search and returns an updated answer

---

## 🧩 JSON Schemas (Pydantic)

Each task defines its own structured output to maintain control and consistency across the pipeline.

**Examples:**

```python
from pydantic import BaseModel, Field

class HallucinationDecision(BaseModel):
    grounded: str = Field(
        ...,
        description="Must be 'yes' if the answer is factual, 'no' otherwise.",
        pattern="^(yes|no)$"
    )

class FinalAnswer(BaseModel):
    answer: str = Field(
        ...,
        description="The final answer to the question. Concise and factual."
    )
```
---
## 📂 Project Structure
```
Agentic_RAG_CrawAI/
│
├─ src/
│   ├─ __init__.py
│   ├─ workflow.py                
│   ├─ agents/                 
│   ├─ tasks/                 
│   └─ tools/
│   └─ .env.example              
│
├─ assets/
│   └─ Transformer_paper.pdf      
│
├─ README.md
├─ requirements.txt
└─ .gitignore
```

## ✨ Key Features  

- ✅ Multi-agent reasoning using CrewAI 
- ✅ Integrated hallucination detection and correction
- ✅ Automatic fallback to web search when data is missing
- ✅ Structured Pydantic-based validation for all task outputs
- ✅ Supports PDF + Web hybrid retrieval

---

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/omarsabri125/Agentic_RAG_CrawAI.git
   cd Agentic_RAG_CrawAI
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv myenv
   source myenv/bin/activate   # Linux/Mac
   myenv\Scripts\activate      # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Running the Pipeline

### 🧰 Prerequisites

- Python 3.10+
- CrewAI
- Tavily API key (`TAVILY_API_KEY`)
- OpenRouter API key (`OPENROUTER_API_KEY`)
- Required packages in `requirements.txt`

### ▶️ Run the script
```bash
cd src
python workflow.py
```
### 🧪 Example
```python
test_question = "What are the latest advancements in AI released by OpenAI this month?"
result = main(question=test_question)
print(result)
```
### 💬 Example Output
```python
{
  "answer": "According to OpenAI’s official announcements in October 2025, the latest advancements include GPT-4.5 release, new multimodal features, and improved API integration."
}
```
