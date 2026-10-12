import streamlit as st
from backend import calculate_bmi

st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚖️",
    layout="centered"
)

st.title("⚖️ BMI Calculator")
st.write("Calculate your Body Mass Index using your height and weight.")

st.divider()

weight = st.number_input(
    "Weight (kg)",
    min_value=1.0,
    max_value=500.0,
    value=65.0,
    step=1.0
)

height_cm = st.number_input(
    "Height (cm)",
    min_value=50.0,
    max_value=250.0,
    value=170.0,
    step=1.0
)

if st.button("Calculate BMI", type="primary", use_container_width=True):
    height_m = height_cm / 100

    result = calculate_bmi(weight, height_m)

    st.subheader("Your BMI Result")

    st.metric("Body Mass Index", result["bmi"])

    category = result["category"]

    if category == "Underweight":
        st.info("Category: Underweight")
    elif category == "Normal weight":
        st.success("Category: Normal weight")
    elif category == "Overweight":
        st.warning("Category: Overweight")
    else:
        st.error("Category: Obese")

    st.write("### BMI Categories")
    st.write("- Below 18.5: Underweight")
    st.write("- 18.5–24.9: Normal weight")
    st.write("- 25–29.9: Overweight")
    st.write("- 30 and above: Obese")

    st.caption(
        "These are general adult BMI categories, "
        "not a medical diagnosis."
    )

if st.button("Reset Calculator", use_container_width=True):
    st.rerun()
