import streamlit as st
import numpy as np
from joblib import load
st.set_page_config(page_title="Predict", layout= "centered")
hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


with open("model.joblib", 'rb') as file:
            info = load("model.joblib")
model = info["model"]
type_encod = info["type_encod"]

st.title("Online Transaction Fraud Detection")

with st.form("transaction_form"):
    type_options = ["CASH_OUT", "PAYMENT", "CASH_IN", "TRANSFER", "DEBIT"]
    transaction_type = st.selectbox("Type of online transaction", type_options)
    amount = st.number_input("The amount of transaction", min_value=0, step=1, format="%d")
    old_balance = st.number_input("Initial balance of recipient before the transaction", min_value=0, step=1, format="%d")
    new_balance = st.number_input("The new balance of recipient after the transaction", min_value=0, step=1, format="%d")
    
    submitted = st.form_submit_button("Predict")

if submitted:
    # Prepare the input data
    input_data = np.array([[type_encod, amount, old_balance, new_balance]])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Display the result
    if prediction == 0:
        st.success("Transaction is Legitimate ✅")
    else:
        st.error("Fraudulent Transaction Detected! 🚨")
