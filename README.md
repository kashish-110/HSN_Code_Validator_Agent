# 🧾 HSN Code Validation Agent (FastAPI + Google ADK)

This project implements an intelligent agent that validates Harmonized System Nomenclature (HSN) codes using a master Excel file. Built with **FastAPI** and Google's **Agent Developer Kit (ADK)**, the agent supports single and batch HSN validation and provides hierarchy checks.

---

## 📁 Project Structure

hsn_agent/
├── HSN_SAC.xlsx # Master HSN data file
├── app.py # FastAPI application (entry point)
├── hsn_validator.py # Validation logic (tool functions)
├── requirements.txt # Python dependencies

yaml
Copy
Edit

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

---

## 🏁 Getting Started

### 1. 📦 Install Dependencies

Create a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
requirements.txt

text
Copy
Edit
fastapi
uvicorn
pandas
openpyxl
google-adk  # hypothetical; if not available, mock or simulate tools
2. 🚀 Run the Server
bash
Copy
Edit
uvicorn app:app --reload
Visit: http://127.0.0.1:8000/docs for Swagger UI.

🧠 API Endpoints
POST /chat
Simulated conversational chatbot using input text.

Request
json
Copy
Edit
{
  "query": "What does HSN code 01012100 mean?"
}
Response
json
Copy
Edit
{
  "response": {
    "status": "success",
    "report": "01012100: PURE-BRED BREEDING ANIMALS",
    "parent_codes": ["01", "0101", "010121"],
    "valid_parents": ["01", "0101", "010121"]
  }
}
POST /validate
Validate a single HSN code using structured input.

json
Copy
Edit
{
  "hsn_code": "01012100"
}
POST /validate/batch
Validate multiple codes at once:

json
Copy
Edit
{
  "hsn_codes": ["01012100", "99999999", "0101"]
}
🛠 Agent Tools (Google ADK)
The following functions are registered as tools in the ADK Agent:

validate_hsn_code

validate_hsn_codes

validate_hsn_hierarchy

These tools are used internally and can be extended for LLM/NLP orchestration.

📌 Notes
Make sure your HSN_SAC.xlsx file includes HSNCode and Description columns.

The agent.chat() method does not exist in Google ADK. Chat is simulated via rule-based routing of the query.

📄 Author
Kashish Gupta
Assessment: Google ADK – HSN Code Validation Agent
May 2025

📬 Future Improvements
Integrate with Gemini chat model for true conversational NLP.

Add /reload-data endpoint to update Excel data without restart.

Log frequent invalid codes to identify data quality issues.
