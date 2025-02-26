# 🏦 Tax Assistant Chatbot

## 📌 Problem Statement
A **Tax Assistant** that can automate tax filing processes, simplify complex calculations, identify deductions, and minimize errors.

## 🚀 Features
- Automates tax filing processes
- Provides tax calculations based on income
- Identifies possible tax deductions
- Minimizes errors in tax calculations
- Declines non-tax-related queries
- Built using **Flask**, **Python**, and **Google AI Studio**

## 🛠️ Tech Stack
- **Backend:** Python, Flask
- **AI Model:** Google Gemini API
- **Frontend:** HTML (Flask Templates)

## 💂️ Folder Structure
```
💾 tax_chatbot
 ├── 📁 templates  # Contains index.html
 ├── app.py       # Main Flask backend
 ├── README.md    # Project documentation
```

## 🔧 Installation & Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/SuryaMounika566/tax_chatbot.git
   cd tax_chatbot
   ```

2. **Create a Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install flask google-generativeai
   ```

4. **Set Up API Key**
   - Get a **Google Gemini API Key** from [Google AI Studio](https://aistudio.google.com/)
   - Add the API key in `app.py`:
     ```python
     API_KEY = "your-gemini-api-key"
     ```

5. **Run the Flask Application**
   ```bash
   python app.py
   ```

6. **Open in Browser**
   - Go to: `http://127.0.0.1:5000/`

## 📌 Usage
- Enter tax-related queries in the chatbot.
- Get automated responses regarding tax slabs, deductions, and calculations.
- Ask about income tax, exemptions, and filing processes.

