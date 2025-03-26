import streamlit as st

st.set_page_config(page_title="BMI CALCULATOR", page_icon="🤒", layout="centered")

st.title("Project 9: BMI Calculator in Python")
st.markdown("""
## Apna Body Mass Index (BMI) calculate karain. Neeche apna **weight and height** enter karein.
""")
            
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Weight (kg): ", min_value=1.0, format="%.2f")
with col2:
    height = st.number_input("Height (m): ", min_value=0.5, format="%.2f")  # Corrected format and height limit

if height > 0 and weight > 0:
    bmi = weight / (height ** 2)  # BMI formula
    st.subheader("Aapka BMI hai:")
    st.markdown(f"**{bmi:.2f}**", unsafe_allow_html=True)

    if bmi < 18.5:
        st.error("underweight ❗")
    elif 18.5 <= bmi < 24.9:
        st.success("normal weight ✅")
    elif 25 <= bmi < 29.9:
        st.warning("Overweight ⚠️")
    else:
        st.error("Obesity 🚨")
else:
    st.error("Please enter a valid weight and height.")
