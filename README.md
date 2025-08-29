# 🤖 AI-Powered Interview Question Generator

An interactive **Streamlit web application** that conducts **AI-powered technical interviews** for internship candidates.  
The app automatically generates **role-specific questions**, evaluates candidate answers using **OpenAI API**, and gives a **final score + eligibility result**.

---

## 🎯 Features
- **3-Page Streamlit App**
  - **Page 1:** Select Field (AI, Web Development, Game Development)
  - **Page 2:** Select Experience Level (Fresher / Experienced Intern)
  - **Page 3:** Interview Chat Interface with AI Evaluation
- **Question Bank (JSON-based):** Stores technical & behavioral questions
- **AI Evaluation:** Uses OpenAI GPT API to score answers (0–10) + feedback
- **Final Report:** Average score & eligibility status
- **Custom UI:** Styled with custom CSS (matching brand colors)

---

## 🖼️ Project UI
### Page 1 – Field Selection  
👉 User selects their field (AI / Web Dev / Game Dev)

### Page 2 – Experience Level  
👉 User selects Fresher or Experienced Intern

### Page 3 – Interview Chat Interface  
👉 Bot asks 5 questions, candidate answers in chat format, AI evaluates.

---

## 🛠️ Tech Stack
- **Frontend:** [Streamlit](https://streamlit.io)  
- **Backend:** Python  
- **AI Integration:** [OpenAI API](https://platform.openai.com/)  
- **Data Storage:** JSON question bank  
- **Styling:** Streamlit Components + Custom CSS  

---

## 📂 Project Structure
📦 ai-interview-generator
├── Home.py # Page 1: Field Selection
├── pages/
│ ├── Experience.py # Page 2: Experience Selection
│ └── Interview.py # Page 3: Interview Interface
├── question_bank.json # Question Bank (by field + level)
├── requirements.txt # Dependencies
└── README.md # Documentation
