import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.markdown("""
<style>

/* 🌸 Background */
.stApp {
    background: linear-gradient(135deg, #f9fafb, #fce7f3);
}

/* 🧾 Sidebar */
section[data-testid="stSidebar"] {
    background: #fff1f2;
    border-right: 1px solid #fbcfe8;
}

/* ✨ Title */
h1 {
    color: #1f2937 !important;
    text-align: center;
    font-size: 36px;
    font-weight: 700;
}

/* 🧴 Labels */
label, .stMarkdown, p {
    color: #111827 !important;
}


/* 🔘 Button */
.stButton>button {
    background: linear-gradient(90deg, #ec4899, #f472b6);
    color: white !important;
    border-radius: 12px;
    height: 45px;
    font-size: 16px;
    border: none;
}

/* 🌟 Container */
.block-container {
    padding: 2rem;
    border-radius: 15px;
    background: #ffffff;
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);
}

/* ✅ SUCCESS / ERROR FIX */
div[data-testid="stAlert"] * {
    color: #111827 !important;
}

div[data-testid="stAlert"][class*="success"] {
    background-color: #dcfce7 !important;
    color: #166534 !important;
}

div[data-testid="stAlert"][class*="error"] {
    background-color: #fee2e2 !important;
    color: #991b1b !important;
}

</style>
""", unsafe_allow_html=True)
st.set_page_config(page_title="Salon-Predict-form", layout="wide")
# ✅ TITLE
st.markdown("<h1>💄 Salon Customer Prediction App</h1>", unsafe_allow_html=True)

# ✅ SIDEBAR

st.markdown("✨ Glow with confidence, not perfection ✨")

# ✅ LOAD MODEL
er = joblib.load("salon.pkl")

# ✅ INPUTS
age = st.slider("Age", 18, 60)
gender = st.selectbox("Gender", ["Male", "Female"])
budget = st.selectbox("Budget", ["Low", "Medium", "High"])
distance = st.slider("Distance (km)", 0.5, 10.0)
rating = st.slider("Rating", 2.5, 5.0)
service = st.selectbox("Service Type", ["Haircut", "Facial", "Makeup", "Hair Spa"])
waiting = st.slider("Waiting Time", 5, 60)
offers = st.selectbox("Offers", ["Yes", "No"])
visits = st.slider("Previous Visits", 0, 10)
occasion = st.selectbox("Occasion", ["Regular", "Wedding", "Party"])

# ✅ ENCODING
gender = 1 if gender == "Male" else 0
budget = {"Low": 0, "Medium": 1, "High": 2}[budget]
service = {"Haircut": 0, "Facial": 1, "Makeup": 2, "Hair Spa": 3}[service]
offers = 1 if offers == "Yes" else 0
occasion = {"Regular": 0, "Wedding": 1, "Party": 2}[occasion]

# ✅ PREDICTION
if st.button("✨ Predict", use_container_width=True):
    input_data = np.array([[age, gender, budget, distance, rating, service, waiting, offers, visits, occasion]])
    result = er.predict(input_data)

    if result[0] == 1:
        st.success("✅ Customer WILL choose this salon")
    else:
        st.error("❌ Customer will NOT choose this salon")
