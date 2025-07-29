# 🧠 Local Chatbot — RAG-Based JD Assistant using FAISS

A lightweight Retrieval-Augmented Generation (RAG) application built with FAISS and Streamlit that helps users quickly understand job descriptions by extracting meaningful insights — all through a simple web interface.

---

## 🚀 Features

- 📄 Upload any Job Description (JD) in PDF or text format directly from the UI
- 🧠 Embeds the JD content using Amazon Titan Text Embeddings
- 🔍 Retrieves the most relevant content chunks using FAISS similarity search
- 💬 Ask questions like "What skills are required?" or "Is remote work allowed?"
- 🤖 Uses Amazon Nova Pro (or any LLM of choice) to generate direct, helpful answers
- 💸 Cost-effective and fast — no need for hosted vector databases or heavy cloud infra
- 🖥️ Built with Streamlit — no manual file placement or CLI interaction needed

---

## 🎯 Purpose

When applying for jobs, candidates often find it hard to understand what companies are actually looking for. This app saves time by letting you ask *exactly* what you want to know about a job description:

- Does this JD match your skills?
- What are the core requirements?
- Is it worth applying?

Instead of reading line by line, just upload the JD file and ask!

---

## 🛠️ Tech Stack

- **UI**: Streamlit
- **Embeddings**: Amazon Titan Text Embeddings
- **Vector Store**: FAISS (Facebook AI Similarity Search)
- **LLM**: Amazon Bedrock – Nova Pro Model (or any compatible open-source model)
- **Backend**: Python
- **RAG Flow**: Local setup with low cost and fast inference

---

## 📁 Project Structure

faiss_project/
│
├── rag/
│ ├── embedding.py # Embedding logic
│ └── retrieving.py # Similarity search logic
│
├── faiss_index/ # Sample Stored FAISS index and metadata
│ ├── index.faiss
│ └── index.pkl
│
├── assets/ # Screenshots or example outputs
│ └── outputs.docx #Provide detail end to end UI flow Screenshots.
│
├── sample-input/ # Sample input document loaded for this Chatbot.
│ ├── Sample Job Description.pdf
├── streamlit_app.py # 🔥 Streamlit app (main entry point)
├── requirements.txt
└── README.md



---

## 📦 Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/chabburi/faiss_project.git

# 2. Navigate into the project folder
cd faiss_project

# 3. (Optional) Create and activate a virtual environment
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the application
streamlit run streamlit_app.py
