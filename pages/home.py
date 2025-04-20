import streamlit as st

def home():
    st.set_page_config(page_title="Overview",page_icon="🏠",layout="wide")
    
    if st.session_state.page == "home":

        st.markdown("""
            <style>
            .section-header {
                font-size: 45px;
                font-weight: 800;
                color: #0080FF;
                margin-top: 40px;
                padding: 30px;
                background: linear-gradient(to right, #36d1dc, #5b86e5);
                -webkit-background-clip: text;
            }
            .sec-header{
                font-size: 25px;
                font-weight: 800;
                color: #0080FF;
                margin-top: 40px;
                background: linear-gradient(to right, #36d1dc, #5b86e5);
                -webkit-background-clip: text;
            }
            .step-box {
                background: linear-gradient(135deg, #ffffff, #f1faff);
                padding: 30px;
                border-radius: 14px;
                margin-bottom: 30px;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.07);
                font-size: 18px;
                line-height: 1.7;
                border-left: 5px solid #0080FF;
            }
            div.stButton > button {
                display: block;
                text-align: centre;
                margin: auto;
                padding: 14px 42px;
                font-size: 20px;
                background-color: #007BFF;
                color: white;
                border: none;
                border-radius: 10px;
            }
            .news-item {
                background-color: #eef6ff;
                border-left: 6px solid #007BFF;
                padding: 12px;
                margin-bottom: 12px;
                font-size: 17px;
                font-weight: 500;
                border-radius: 6px;
            }
            [data-testid="stExpander"] {
                background-color: white !important;
                border-radius: 10px;
                padding: 10px;
                font-size: 100px;
            }

            /* Title of the expander */
            [data-testid="stExpander"] div[role="button"] {
                font-size: 20px !important;
                font-weight: bold;
                color: black !important;
            }

            /* Content inside expander */
            [data-testid="stExpander"] .st-expanderContent p {
                font-size: 18px !important;
                color: black !important;
            }
            ul li {
                margin-bottom: 8px;
            }
            .stApp { color: black !important; }
        </style>
        """, unsafe_allow_html=True)

        style_heading = "text-align: center; color: #0080FF;font-size: 55px;"  # Add the desired color
        st.markdown(f"<h1 style='{style_heading}'>🛡️ AI-Powered Fraud Detection</h1>", unsafe_allow_html=True)

        

        # --- Metrics ---
        col1, col2, col3 = st.columns(3)
        col1.metric("💳 Credit Card Frauds", "₹120 Cr+")
        col2.metric("📉 Detection Accuracy", "97.6%")
        col3.metric("⚡ Real-time Detection", "< 2 seconds")

        st.markdown("---")

        # --- News ---
        st.markdown("<div class='section-header'>📰 Recent Credit Card Fraud Incidents</div>", unsafe_allow_html=True)
        with st.expander("📰 Latest Fraud-Related News"):
            st.markdown("""
        <div class='news-item'>
        🔹 <strong>April 2025</strong>: ₹1.26 crore siphoned using 55 credit cards obtained via forged documents. Mumbai Crime Branch arrested five individuals from Assam involved in the scam.<br>
        👉 <a href='https://indianexpress.com/article/cities/mumbai/gang-siphoned-rs-1-26-crore-using-55-credit-cards-arrested-from-assam-9950277/' target='_blank'>Read Full Article</a>
        </div>

        <div class='news-item'>
        🔹 <strong>March 2025</strong>: A Chandigarh resident lost ₹9 lakh in a sophisticated credit card scam while applying for a new card. Scammers posed as bank officials and exploited the victim's trust.<br>
        👉 <a href='https://www.livemint.com/money/personal-finance/chandigarh-man-falls-victim-to-major-credit-card-scam-5-crucial-lessons-to-avert-fraud-and-secure-your-money-11743591016930.html' target='_blank'>Read Full Article</a>
        </div>

        <div class='news-item'>
        🔹 <strong>March 2025</strong>: A 53-year-old woman from Hyderabad lost ₹2.29 lakh after sharing sensitive details with fraudsters posing as bank officials. The incident underscores the importance of vigilance.<br>
        👉 <a href='https://www.livemint.com/money/personal-finance/hyderabad-woman-falls-victim-to-2-29-lakh-credit-card-fraud-learn-how-to-stay-safe-from-rising-scams-in-india-11742897732069.html' target='_blank'>Read Full Article</a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='section-header'>📊 Fraud Risk by Transaction Type</div>", unsafe_allow_html=True)
        col_chart, col_desc = st.columns([1, 1])
        with col_chart:
            st.image("asset/pie.jpg", use_container_width=True)


        with col_desc:
            st.markdown('''
            <div style='color:#60B5FF; font-size:19px; line-height:1.7;'>
                <strong>CASH_OUT</strong> 🔴 - Money sent to another user. This type has the <strong>highest fraud risk</strong> because it often involves moving money to untraceable accounts, especially if followed by account closure or balance drain.
                <br><br>
                <strong>TRANSFER</strong> 🔴 - Bank-like internal transfers. These are also <strong>high risk</strong> due to impersonation attacks and fraudulent transfers between fake accounts.
                <br><br>
                <strong>DEBIT</strong> 🟡 - Automatic deductions like service charges or fees. These are <strong>medium risk</strong> as they can be exploited via unauthorized account access.
                <br><br>
                <strong>PAYMENT</strong> 🟢 - Used for bills, shopping or merchant payments. Generally considered <strong>low risk</strong>, but frauds do occur through fake merchant links.
                <br><br>
                <strong>CASH_IN</strong> 🟢 - Receiving funds. These are <strong>very low risk</strong> as fraud usually doesn't originate here, but sudden large deposits from unknown sources can trigger alerts.
            </div> ''', unsafe_allow_html= True)
        
        # Go to Predictor button
        st.markdown("""
            <div style='text-align: center; margin: 30px 0;
                    padding: 14px 42px; font-size: 20px;  color: white; border: none; border-radius: 10px;'>
        </div>""", unsafe_allow_html=True)
        if st.button("🔍 Go to Predictor"):
            st.session_state.page = "predictor"

        # --- ML Model Workflow ---
        st.markdown("<div class='section-header'>🤖 How Our ML Model Works</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class='sec-header'>🔍 Step 1: Data Collection</div>
        <div class='step-box'>
            We begin with a massive dataset of real and synthetic financial transactions. Each entry includes:
            <ul>
                <li><strong>Transaction Type</strong> – e.g., TRANSFER, PAYMENT</li>
                <li><strong>Amount</strong> – value of the transaction</li>
                <li><strong>Account Balances</strong> – before and after for both sender and receiver</li>
                <li><strong>Fraud Label</strong> – 0 or 1 indicating if it's fraudulent</li>
            </ul>
        </div>

        <div class='sec-header'>🧹 Step 2: Feature Engineering</div>
        <div class='step-box'>
            Raw data alone isn't enough. We create meaningful features such as:
            <ul>
                <li><strong>Amount mismatch</strong> – between sender and receiver balance</li>
                <li><strong>Sender emptied flag</strong> – indicates account drain</li>
                <li><strong>Receiver gained extra flag</strong> – unusual deposits</li>
                <li><strong>Zero balance indicators</strong> – signs of fake accounts</li>
            </ul>
        </div>

        <div class='sec-header'>🧠 Step 3: Model Training</div>
        <div class='step-box'>
            We train the model using <strong>XGBoost</strong>, known for its speed and accuracy on tabular data. We use stratified cross-validation and fine-tune:
            <ul>
                <li>Learning rate, depth, estimators</li>
                <li>Class imbalance adjustments (e.g., <code>scale_pos_weight</code>)</li>
            </ul>
            The model learns fraud patterns that are difficult to detect manually.
        </div>

        <div class='sec-header'>📊 Step 4: Testing & Evaluation</div>
        <div class='step-box'>
            We test using metrics that matter:
            <ul>
                <li><strong>Accuracy</strong> – overall correctness</li>
                <li><strong>Recall</strong> – ability to catch frauds (priority)</li>
                <li><strong>Precision</strong> – how often flagged frauds are real</li>
                <li><strong>AUC-ROC</strong> – balance between true/false positives</li>
            </ul>
            All models are stress-tested on real-world imbalance.
        </div>

        <div class='sec-header'>⚙️ Step 5: Real-Time Detection</div>
        <div class='step-box'>
            In deployment, the model receives live transaction inputs:
            <ul>
                <li>Extracts relevant features from input</li>
                <li>Applies trained model using <code>predict_proba()</code></li>
                <li>Outputs fraud probability (e.g., 0.82)</li>
                <li>App displays result with alert if risk is high</li>
            </ul>
        </div>

        <div class='sec-header'>🛡️ Final Impact</div>
        <div class='step-box'>
            <strong>⏱️ Speed:</strong> Less than 2 seconds per transaction  <br>
            <strong>🎯 Accuracy:</strong> Up to 96% on curated datasets  <br>
            <strong>🚨 Prevention:</strong> High-risk transactions flagged for action  <br><br>
            <strong>Result:</strong> Fewer losses. Safer banking. Happy users. ✅
        </div>
        """, unsafe_allow_html=True)