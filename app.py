import numpy as np
import streamlit as st

import pickle

model = pickle.load(open("model.pkl", "rb"))

st.sidebar.info(
    """
    This project predicts whether a credit card transaction is:

    - Genuine Transaction
    - Fraudulent Transaction

    Model Used:
    Logistic Regression
    """
)

# Input Section
st.subheader("Enter Transaction Details")

col1, col2 = st.columns(2)

with col1:
    Time = st.number_input("Transaction Time", value=0.0)

with col2:
    Amount = st.number_input("Transaction Amount", value=0.0)

# Feature Inputs
# features = []

# st.subheader("Transaction Features")

# cols = st.columns(4)

# for i in range(1, 29):
#     with cols[(i - 1) % 4]:
#         value = st.number_input(f"V{i}", value=0.0)
#         features.append(value)

# Feature Inputs
features = []

st.subheader("Transaction Features")

feature_names = {
    "V1": "Transaction Behavior Score",
    "V2": "Spending Pattern Indicator",
    "V3": "Merchant Risk Signal",
    "V4": "Account Activity Variation",
    "V5": "Purchase Frequency Metric",
    "V6": "Location Consistency Score",
    "V7": "Transaction Velocity Indicator",
    "V8": "Device Usage Pattern",
    "V9": "Customer Spending Trend",
    "V10": "High Risk Activity Score",
    "V11": "Authorization Confidence Metric",
    "V12": "Payment Irregularity Indicator",
    "V13": "Transaction Sequence Score",
    "V14": "Fraud Probability Signal",
    "V15": "Card Usage Stability",
    "V16": "Suspicious Activity Measure",
    "V17": "Behavioral Deviation Score",
    "V18": "Purchase Authenticity Index",
    "V19": "Transaction Trust Factor",
    "V20": "Network Activity Score",
    "V21": "Digital Footprint Metric",
    "V22": "Transaction Consistency Indicator",
    "V23": "Purchase Validation Score",
    "V24": "Cardholder Reliability Metric",
    "V25": "Account Verification Signal",
    "V26": "Risk Exposure Indicator",
    "V27": "Security Pattern Score",
    "V28": "Fraud Detection Confidence"
}

cols = st.columns(4)

for i, (feature, label) in enumerate(feature_names.items(), start=1):
    with cols[(i - 1) % 4]:
        value = st.number_input(label, value=0.0)
        features.append(value)

# Prediction Button
if st.button("Predict Transaction"):

    input_data = [Time]
    input_data.extend(features)
    input_data.append(Amount)

    input_array = np.array(input_data).reshape(1, -1)

    prediction = model.predict(input_array)

    st.markdown("---")

    if prediction[0] == 1:
        st.error("⚠ Fraudulent Transaction Detected")
    else:
        st.success("✅ Genuine Transaction")

# Footer
st.markdown("---")

st.markdown(
    "<center>Developed by Amit Singh | Data Science Project</center>",
    unsafe_allow_html=True
)