import streamlit as st
import numpy as np
from joblib import load

# Load trained model
with open("model.pkl", 'rb') as file:
    model = load(file)

# App Title and Design
st.set_page_config(page_title="Fraud Detection System", page_icon="💳", layout="centered")

st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
        }
        .title {
            text-align: center;
            color: #2c3e50;
        }
        .stButton > button {
            background-color: #2ecc71;
            color: white;
            font-weight: bold;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #2c3e50;'>🔍 Fraud Detection System</h1>", unsafe_allow_html=True)
st.write("Predict whether a transaction is **fraudulent or legitimate** based on financial details.")
# Input Form
with st.form("transaction_form"):
    st.subheader("📝 Enter Transaction Details:")
    
    type_options = {"CASH_OUT": 1, "PAYMENT": 2, "CASH_IN": 3, "TRANSFER": 4, "DEBIT": 5}
    transaction_type = st.selectbox("Transaction Type", list(type_options.keys()))
    
    amount = st.number_input("💰 Transaction Amount", min_value=0.0, step=1.0)
    old_balance = st.number_input("🏦 Sender's Balance Before Transaction", min_value=0.0, step=1.0)
    new_balance = st.number_input("💸 Sender's Balance After Transaction", min_value=0.0, step=1.0)
    old_dest_balance = st.number_input("📥 Receiver's Balance Before Transaction", min_value=0.0, step=1.0)
    new_dest_balance = st.number_input("📤 Receiver's Balance After Transaction", min_value=0.0, step=1.0)

    submitted = st.form_submit_button("🔍 Predict")

if submitted:
    # Prepare input data
    type_encoded = type_options[transaction_type]
    input_data = np.array([[type_encoded, amount, old_balance, new_balance, old_dest_balance, new_dest_balance]])

    # Predict
    prediction = model.predict(input_data)[0]

    # Result
    st.subheader("🔎 Prediction Result:")
    if prediction == 0:
        st.success("✅ This transaction is **Legitimate**.")
    else:
        st.error("🚨 Fraudulent Transaction Detected!")
    
    st.markdown("---")
    st.markdown("👨‍💻 *Final Year Project - Fraud Detection using Machine Learning*")

