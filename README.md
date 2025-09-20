# 📊 Smart Finance Tracker

An AI-powered personal finance assistant built with **Streamlit** and **Google Gemini API**.  
This app analyzes your **Paytm transaction history PDF** and generates **detailed financial insights** such as income/expenses, savings percentage, expense trends, and cost-cutting suggestions.

## 🚀 Features
- 📂 Upload **Paytm transaction history PDFs**
- 🔍 Extract text using **PyPDF2**
- 🤖 AI-driven financial insights powered by **Google Gemini**
- 📑 Detailed analysis report including:
  - Monthly income and expenses  
  - Unnecessary expense detection with recommendations  
  - Savings percentage  
  - Spending trends over time  
  - Category-wise expense breakdown  
- 🎨 Clean and interactive **Streamlit dashboard**

## 🛠️ Tech Stack
- **Python 3.9+**
- **Streamlit** – UI framework  
- **PyPDF2** – PDF text extraction  
- **Google Gemini API (genai)** – AI analysis  

## 📂 Project Structure
smart-finance-tracker/
│── app.py              # Main Streamlit app
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation

##📌 Example Insights

💰 Monthly income & expenses summary
🚫 Unnecessary expenses flagged (e.g., frequent food delivery)
📉 Expense trends (rising/falling categories)
💡 Budgeting tips for saving more
