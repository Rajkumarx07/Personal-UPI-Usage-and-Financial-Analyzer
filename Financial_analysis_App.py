import os
import streamlit as st
import PyPDF2
from google import genai

st.set_page_config(page_title="Smart Finance Tracker", page_icon="📈", layout="wide")

GEMINI_API_KEY = "Give_your_API_Key"
client = genai.Client(api_key=GEMINI_API_KEY)


st.markdown('<h1 class="main-title">📊 Smart Personal Finance Assistant</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Upload your Paytm transaction history PDF for AI-driven financial insights</p>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("📂 Select Paytm transaction history PDF", type=["pdf"])

def extract_text_from_pdf(file_path):
    text = []
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
    return "\n".join(text).strip()

def get_financial_report(text):
    prompt = f"""
You are a financial assistant. Analyze this Paytm transaction history text and provide detailed insights including:

- Monthly income and expenses
- Identification of unnecessary expenses with recommendations
- Savings percentage
- Expense trends over time
- Suggestions to control costs
- Breakdown of spending by category

Transaction History:
{text}
"""
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",    
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error generating report: {e}"

if uploaded_file is not None:
    temp_path = f"temp_{uploaded_file.name}"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("📥 File uploaded successfully!")

    with st.spinner("📄 Extracting text from PDF..."):
        extracted_text = extract_text_from_pdf(temp_path)

    if not extracted_text:
        st.error("⚠️ No readable text found. Please ensure the PDF is not scanned image-based.")
    else:
        with st.spinner("🤖 Generating financial insights..."):
            progress = st.progress(0)
            report = get_financial_report(extracted_text)
            progress.progress(100)

        st.subheader("📑 Financial Insights Report")
        st.markdown(f'<div class="result-card"><b>Report for:</b> {uploaded_file.name}</div>', unsafe_allow_html=True)
        st.write(report)
        st.markdown('<div class="banner">✅ Analysis complete! Use this to budget smarter. 🚀</div>', unsafe_allow_html=True)
        

    os.remove(temp_path)

