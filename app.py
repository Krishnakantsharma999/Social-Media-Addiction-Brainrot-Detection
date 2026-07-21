import streamlit as st
import pandas as pd
import pickle

# Load models
rf = pickle.load(open("addiction_model.pkl", "rb"))
lr = pickle.load(open("brainrot_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))  # VERY IMPORTANT

st.title("📱 Social Media Addiction & Brainrot Detection")

st.write("Enter user details:")

# Inputs
age = st.slider("Age", 15, 30, 20)
gender = st.selectbox("Gender", ["Male", "Female"])
academic = st.selectbox("Academic Level", ["High School", "Undergraduate", "Postgraduate"])
country = st.text_input("Country")

usage = st.slider("Avg Daily Usage (Hours)", 0.0, 12.0, 4.0)
platform = st.selectbox("Most Used Platform", ["Instagram", "TikTok", "Facebook", "Twitter"])

performance = st.selectbox("Affects Academic Performance", ["Yes", "No"])

sleep = st.slider("Sleep Hours Per Night", 3.0, 10.0, 7.0)
mental = st.slider("Mental Health Score", 1, 10, 5)

relationship = st.selectbox("Relationship Status", ["Single", "In Relationship"])

conflicts = st.slider("Conflicts Over Social Media", 0, 10, 2)

# 🔥 Convert input to dataframe
input_dict = {
    "Age": age,
    "Gender": gender,
    "Academic_Level": academic,
    "Country": country,
    "Avg_Daily_Usage_Hours": usage,
    "Most_Used_Platform": platform,
    "Affects_Academic_Performance": performance,
    "Sleep_Hours_Per_Night": sleep,
    "Mental_Health_Score": mental,
    "Relationship_Status": relationship,
    "Conflicts_Over_Social_Media": conflicts
}

input_df = pd.DataFrame([input_dict])

# 🔥 Apply same preprocessing
input_df = pd.get_dummies(input_df)

# 🔥 Align columns (CRITICAL STEP)
input_df = input_df.reindex(columns=columns, fill_value=0)

# 🔥 Scale
input_scaled = scaler.transform(input_df)

# Predict
if st.button("Predict"):
    
    addiction = rf.predict(input_scaled)[0]
    brainrot = lr.predict(input_scaled)[0]

    if brainrot < 10:
        level = "Low"
    elif brainrot < 25:
        level = "Medium"
    else:
        level = "High"

    st.subheader("📊 Results")
    st.write(f"Addiction Score: {addiction}")
    st.write(f"Brainrot Score: {brainrot:.2f}")
    st.write(f"Brainrot Level: {level}")