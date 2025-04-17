import streamlit as st
import numpy as np
from joblib import load

# Load model
with open("model.pkl", 'rb') as file:
    model = load(file)

# Page config
st.set_page_config(page_title="Fraud Detection", page_icon="💳", layout="centered")

st.markdown("<h1 style='text-align: center; color: #2c3e50;'>🔍 Fraud Detection System</h1>", unsafe_allow_html=True)
st.write("Predict whether a transaction is **fraudulent or legitimate** based on financial details.")

# Setup default values in session_state
for key in ["type", "amount", "old_balance", "new_balance", "old_dest", "new_dest", "show_result"]:
    if key not in st.session_state:
        st.session_state[key] = None if key == "type" else 0.0 if key != "show_result" else False

# Transaction form
with st.form("transaction_form"):
    st.subheader("📝 Enter Transaction Details:")

    type_map = {"CASH_OUT": 1, "PAYMENT": 2, "CASH_IN": 3, "TRANSFER": 4, "DEBIT": 5}
    st.session_state.type = st.selectbox("Transaction Type", list(type_map.keys()), index=0)
    st.session_state.amount = st.number_input("💰 Transaction Amount", value=st.session_state.amount, min_value=0.0)
    st.session_state.old_balance = st.number_input("🏦 Sender's Balance Before", value=st.session_state.old_balance, min_value=0.0)
    st.session_state.new_balance = st.number_input("💸 Sender's Balance After", value=st.session_state.new_balance, min_value=0.0)
    st.session_state.old_dest = st.number_input("📥 Receiver's Balance Before", value=st.session_state.old_dest, min_value=0.0)
    st.session_state.new_dest = st.number_input("📤 Receiver's Balance After", value=st.session_state.new_dest, min_value=0.0)

    submitted = st.form_submit_button("🔍 Predict")

# On predict
if submitted:
    input_data = np.array([[type_map[st.session_state.type],
                            st.session_state.amount,
                            st.session_state.old_balance,
                            st.session_state.new_balance,
                            st.session_state.old_dest,
                            st.session_state.new_dest]])
    
    prediction = model.predict(input_data)[0]
    st.session_state.show_result = True
    st.session_state.prediction = prediction

# Simulated Pop-Up Result
if st.session_state.show_result:
    with st.container():
        st.markdown("---")
        st.subheader("🎯 Prediction Result")
        if st.session_state.prediction == 0:
            st.success("✅ Legitimate Transaction")
        else:
            st.error("🚨 Fraudulent Transaction Detected!")

        if st.button("❌ Clear"):
            # Reset all inputs
            for key in ["type", "amount", "old_balance", "new_balance", "old_dest", "new_dest", "show_result"]:
                st.session_state[key] = None if key == "type" else 0.0 if key != "show_result" else False
