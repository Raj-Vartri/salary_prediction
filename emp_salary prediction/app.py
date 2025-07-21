import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Employee Salary Predictor (INR)", page_icon="💼", layout="centered")

# Optional: Logo
try:
    st.image("assets/logo.png", width=80)
except:
    pass

st.title("💼 Employee Annual Salary Predictor (INR)")
st.markdown("Estimate your yearly salary in **Indian Rupees (₹)** based on your professional profile.")

with st.form("user_input_form"):
    col1, col2 = st.columns(2)
    age = col1.slider("Age", 18, 70, 30)
    exp = col2.slider("Years of Experience", 2, 30, 2)  # restricted to 2–30
    education = col1.selectbox(
        "Education Level",
        ["HS-grad", "Some-college", "Bachelors", "Masters", "Doctorate"]
    )
    occupation = col2.selectbox(
        "Occupation",
        [
            "Exec-managerial", "Tech-support", "Craft-repair",
            "Other-service", "Sales", "Prof-specialty"
        ]
    )
    hours = col1.slider("Hours Worked per Week", 20, 70, 40)
    gender = col2.radio("Gender", ["Male", "Female"])
    submit = st.form_submit_button("🔮 Predict Salary")

if submit:
    input_df = pd.DataFrame({
        "age": [age],
        "years_experience": [exp],
        "education": [education],
        "occupation": [occupation],
        "hours-per-week": [hours],
        "gender": [gender]
    })
    model = joblib.load("salary_model.pkl")
    salary = int(model.predict(input_df)[0])
    st.markdown("---")
    st.subheader("💰 Predicted Annual Salary")
    st.markdown(f"<h2 style='color: green;'>₹ {salary:,.0f}</h2>", unsafe_allow_html=True)
    st.caption("Note: This is an approximate estimate based on profile and typical industry patterns.")

st.markdown("<hr><center>Built with ❤️ in India using Streamlit</center>", unsafe_allow_html=True)
