# 🧾 HSN Code Validation Agent (FastAPI + Google ADK)

This project implements an intelligent agent that validates Harmonized System Nomenclature (HSN) codes using a master Excel file. Built with **FastAPI** and Google's **Agent Developer Kit (ADK)**, the agent supports single and batch HSN validation and provides hierarchy checks.

---

## 📁 Project Structure

```

hsn\_agent/
├── HSN\_SAC.xlsx           # Master HSN data file
├── app.py                 # FastAPI application (entry point)
├── hsn\_validator.py       # Validation logic (tool functions)
├── requirements.txt       # Python dependencies

````

---

## ⚙️ Features

- ✅ Validate single or multiple HSN codes
- ✅ Format validation (numeric, 2/4/6/8 digits)
- ✅ Existence check from master data
- ✅ Hierarchical validation of parent codes
- ✅ Conversational API using Google ADK agent tools
- 🚀 Fast and efficient with pre-loaded in-memory dataset

---

## 🔍 Technologies Used

- **FastAPI** for API interface
- **pandas** for Excel processing
- **Google ADK** (`google.adk.agents.Agent`) for agent-based tool orchestration
- **Uvicorn** as the ASGI server


### 1. 📦 Install Dependencies

Create a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
````

Install dependencies:

```bash
pip install -r requirements.txt
```

> **requirements.txt**

```text
fastapi
uvicorn
pandas
openpyxl
google-adk  # hypothetical; if not available, mock or simulate tools
```

---

### 2. 🚀 Run the Server

```bash
uvicorn app:app --reload
```

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Swagger UI.

---

## 🧠 API Endpoints

### `POST /chat`

Simulated conversational chatbot using input text.

#### Request

```json
{
  "query": "What does HSN code 01012100 mean?"
}
```

#### Response

```json
{
  "response": {
    "status": "success",
    "report": "01012100: PURE-BRED BREEDING ANIMALS",
    "parent_codes": ["01", "0101", "010121"],
    "valid_parents": ["01", "0101", "010121"]
  }
}
```

---

### `POST /validate`

Validate a single HSN code using structured input.

```json
{
  "hsn_code": "01012100"
}
```

---

### `POST /validate/batch`

Validate multiple codes at once:

```json
{
  "hsn_codes": ["01012100", "99999999", "0101"]
}
```

---

## 🛠 Agent Tools (Google ADK)

The following functions are registered as tools in the ADK `Agent`:

* `validate_hsn_code`
* `validate_hsn_codes`
* `validate_hsn_hierarchy`

These tools are used internally and can be extended for LLM/NLP orchestration.

## 📄 Author

Kashish Gupta
Assessment: Google ADK – HSN Code Validation Agent
May 2025


