import streamlit as st
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
features = []

st.subheader("Transaction Features")

cols = st.columns(4)

for i in range(1, 29):
    with cols[(i - 1) % 4]:
        value = st.number_input(f"V{i}", value=0.0)
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