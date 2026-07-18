
import streamlit as st
import pandas as pd
import sqlite3
import google.generativeai as genai

# Gemini API
genai.configure(api_key="AIzaSyCHM-2DuSOg0bIa7TQ-vQs4gMGbHH_aDQg")

model = genai.GenerativeModel("gemini-2.5-flash")

# Database Connection
conn = sqlite3.connect("retail_sales.db")

# Streamlit UI
st.title("ABC Retail Sales Chatbot")

question = st.text_input("Ask a sales question")

if question:

    query = """
    SELECT product_name,
           SUM(sales_amount) AS total_sales
    FROM sales_data
    GROUP BY product_name
    ORDER BY total_sales DESC
    LIMIT 5
    """

    result = pd.read_sql(query, conn)

    prompt = f"""
    Analyze this sales data:

    {result}

    User Question:
    {question}

    Give short business insights.
    """

    response = model.generate_content(prompt)

    st.write(response.text)
