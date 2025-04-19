import streamlit as st
import numpy as np
from joblib import load

st.markdown("""
    <style>
        /* Hide sidebar completely */
        [data-testid="stSidebar"] {
            display: none !important;
        }
        /* Optional: hide the top header too */
        header[data-testid="stHeader"] {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# Load trained model
with open("model.pkl", 'rb') as file:
    model = load(file)

st.markdown("<h1 style='text-align: center;'>🔍 Online Transaction Fraud Detection</h1>", unsafe_allow_html=True)
st.write("This app predicts whether a transaction is **fraudulent or legitimate** based on entered details.")

# Transaction type descriptions
type_descriptions = {
    "CASH_OUT": """👤 **CASH_OUT**  
Money is withdrawn from a user's account and sent to another user.  
➡️ Common in peer-to-peer transfers or withdrawals.  
⚠️ **Fraud Risk**: High — often exploited by scammers to steal funds.
""",
    "PAYMENT": """💸 **PAYMENT**  
Payment made by a customer to a merchant, biller, or service.  
➡️ Usually includes bills, shopping, utilities.  
✅ **Fraud Risk**: Low — mostly genuine transactions.
""",
    "CASH_IN": """💰 **CASH_IN**  
Money deposited **into** a user's account by another party.  
➡️ Includes salary, refunds, or received transfers.  
🟢 **Fraud Risk**: Very Low — receiving funds is usually not fraudulent.
""",
    "TRANSFER": """🔁 **TRANSFER**  
Funds transferred from one user to another (internal to the system).  
➡️ Like bank-to-bank transfer within the same platform.  
⚠️ **Fraud Risk**: High — used in laundering or unauthorized movement.
""",
    "DEBIT": """🏦 **DEBIT**  
System-initiated deductions like auto-debits, fees, or penalties.  
➡️ No user action — happens automatically.  
🟡 **Fraud Risk**: Medium — can be misused by faulty systems or exploits.
"""
}


type_encoding = {
    "CASH_OUT": 1,
    "PAYMENT": 2,
    "CASH_IN": 3,
    "TRANSFER": 4,
    "DEBIT": 5
}
transaction_type = st.selectbox("Transaction Type", list(type_encoding.keys()))
st.markdown(f"**ℹ️ {type_descriptions[transaction_type]}**")
# Input form
with st.form("transaction_form"):
    amount = st.text_input("💰 Transaction Amount",placeholder=0.00)
    old_balance = st.number_input("🏦 Sender's Balance Before Transaction", min_value=0.0, step=100.0,placeholder=0.00)
    new_balance = st.number_input("💳 Sender's Balance After Transaction", min_value=0.0, step=100.0,placeholder=0.00)
    old_dest = st.number_input("📥 Receiver's Balance Before Transaction", min_value=0.0, step=100.0,placeholder=0.00)
    new_dest = st.number_input("📤 Receiver's Balance After Transaction", min_value=0.0, step=100.0,placeholder=0.00)
    
    submitted = st.form_submit_button("🔍 Predict")

# On form submit
try:
    if submitted:
        try:
            amount = float(amount)
        except:
            st.warning("Please enter a valid amount.")
        # Derived features
        receiver_delta = new_dest - old_dest
        sender_emptied = int(new_balance == 0)
        receiver_gained = int(receiver_delta > amount)
        amount_mismatch = abs(receiver_delta - amount)

        input_data = np.array([[type_encoding[transaction_type], amount, old_balance, new_balance,
                                old_dest, new_dest, amount_mismatch, sender_emptied, receiver_gained]])

        proba = model.predict_proba(input_data)[0][1]
        st.write(proba)
        st.markdown("---")
        st.subheader("🔎 Prediction Result:")

        if proba < 0.1:
            st.error(f"🚨 Fraudulent Transaction Detected!\n\n**Confidence:** {proba:.2f}")
        else:
            st.success(f"✅ Legitimate Transaction\n\n**Confidence:** {1 - proba:.2f}")
except:
    st.error("please enter details.")
