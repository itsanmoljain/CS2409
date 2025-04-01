import streamlit as st

st.set_page_config(page_title="Overview",layout="wide")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.markdown(
    "<h1 style='text-align: center;'>Credit Card Fraud Detection System</h1>", 
    unsafe_allow_html=True
)
st.header("**Credit Card Fraud: A Detailed Explanation**")
st.markdown("""<p style='font-size:18px;'> Credit card fraud is an illegal activity where someone obtains and uses a credit card or its information without authorization to make purchases or withdraw funds. It has become a significant concern globally, given the widespread use of credit cards and the growth of online transactions. This write-up explores the types of credit card fraud, methods used by fraudsters, consequences, and preventative measures.</p>
""", unsafe_allow_html=True)

st.divider()
st.header("Types of Credit Card Fraud")
st.write("""
<p style='font-size:18px;'>Here’s a detailed breakdown of various types of fraud:

<p style='font-size:20px;'><b>1.Card Not Present (CNP) Fraud:</b></p>
Fraudsters primarily target online or phone transactions where the physical card isn't needed.
Techniques include acquiring card details through data breaches, spyware, phishing, or unauthorized access to e-commerce platforms.
CNP fraud is particularly hard to detect because the absence of a physical card makes it challenging to verify the user.

<p style='font-size:20px;'><b>2. Skimming and Cloning:</b></p>
Skimmers are small devices attached to ATMs or point-of-sale terminals that read and copy data from the magnetic strip when the card is swiped.
Advanced techniques include “shimming,” which targets chip-enabled cards by intercepting the communication between the card’s chip and the payment terminal.
Once the data is stolen, fraudsters create counterfeit cards or use the details for online transactions.

<p style='font-size:20px;'><b>3. Phishing:</b></p>
A social engineering technique where criminals send fake emails or create fraudulent websites imitating trusted organizations.
The goal is to trick cardholders into sharing card numbers, CVVs, and other sensitive information.
Examples include emails claiming that the cardholder’s account needs urgent verification.

<p style='font-size:20px;'><b>4. Identity Theft:</b></p>
Involves the theft of personal information such as name, address, social security numbers (in relevant countries), or Aadhaar numbers (in India).
Fraudsters use this data to open new credit card accounts or manipulate existing accounts.
It can occur through hacking, data breaches, or simple theft of documents.

<p style='font-size:20px;'><b>5. Physical Card Theft:</b></p>
If a card is lost or stolen, it can be used for fraudulent transactions until reported.
Many modern cards use PINs and two-factor authentication to reduce the risk, but this is not foolproof.

<p style='font-size:20px;'><b>6. Application Fraud:</b></p>
Criminals use forged documents, fake identities, or stolen information to apply for new credit cards.
Common in situations where the identity verification process is lax.

<p style='font-size:20px;'><b>7. Account Takeover:</b></p>
The fraudster gains control of an existing credit card account by obtaining login credentials.
They might change contact information to prevent alerts, enabling unrestricted use of the account.</p>

""",unsafe_allow_html=True)

st.divider()
st.header("How Do Fraudsters Operate?")
st.write("""
<p style='font-size:18px;'>Fraudsters employ diverse methods. Let’s examine these:</p>
""", unsafe_allow_html=True)
st.subheader("Technological Methods:")
st.write("""
<p style='font-size:18px;'>
<p style='font-size:20px;'><b>1. Skimming:</b></p>

Criminals install skimming devices on ATMs or POS systems.
Some advanced skimmers work wirelessly, capturing data without physical contact.

<p style='font-size:20px;'><b>2. Data Breaches:</b></p>

Large-scale breaches target companies storing sensitive financial data, exposing millions of credit card records.

<p style='font-size:20px;'><b>3. Malware:</b></p>

Fraudsters use malicious software to infect devices, tracking keystrokes and accessing sensitive files.

<p style='font-size:20px;'><b>4. Public Wi-Fi Exploitation:</b></p>

Public Wi-Fi networks are often unsecured, making them a target for intercepting credit card details during online transactions.</p>""",unsafe_allow_html=True)

st.subheader("Social Engineering Methods:")
st.write("""
<p style='font-size:18px;'>

<p style='font-size:20px;'><b>1. Phishing:</b></p>
Fraudsters create convincing emails or websites to impersonate banks.
They may claim that urgent action is needed, enticing users to share sensitive details.

<p style='font-size:20px;'><b>2. Vishing (Voice Phishing):</b></p>
A fraudulent caller pretends to be a representative from your bank, asking for card details or PINs.

<p style='font-size:20px;'><b>3. Smishing (SMS Phishing):</b></p>
Fake text messages claiming to be from your bank contain links to malicious websites.</p>
""", unsafe_allow_html=True)

st.divider()
st.header("Consequences of Credit Card Fraud")
st.write("""
<p style='font-size:18px;'>The impact of credit card fraud can be devastating:

<p style='font-size:18px;'><b>For Individuals:</b></p>
1.Financial losses until the fraud is resolved.<br>
2.Emotional stress and anxiety caused by compromised financial security.<br>
3.Damaged credit scores if fraudulent activities go unnoticed.

<p style='font-size:18px;'><b>For Businesses:</b></p>
1.Increased costs due to chargebacks and fraud prevention measures.<br>
2.Loss of customer trust if fraud occurs on their platforms.<br>
3.Reputation damage, especially for financial service providers.

<p style='font-size:18px;'><b>For Financial Institutions:</b></p>
1. Depletion of resources dealing with fraud claims.<br>
2. Significant investment in fraud detection and prevention technologies.</p>
""",unsafe_allow_html=True)

st.divider()
