import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Python Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Python Calculator")
st.write("Perform basic arithmetic operations using Streamlit.")

# Input Numbers
num1 = st.number_input("Enter First Number", value=0.0)
num2 = st.number_input("Enter Second Number", value=0.0)

# Select Operation
operation = st.selectbox(
    "Select Operation",
    (
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Modulus",
        "Power"
    )
)

# Calculate Button
if st.button("Calculate"):

    if operation == "Addition":
        result = num1 + num2

    elif operation == "Subtraction":
        result = num1 - num2

    elif operation == "Multiplication":
        result = num1 * num2

    elif operation == "Division":
        if num2 == 0:
            st.error("Division by zero is not allowed!")
        else:
            result = num1 / num2

    elif operation == "Modulus":
        if num2 == 0:
            st.error("Cannot perform modulus with zero!")
        else:
            result = num1 % num2

    elif operation == "Power":
        result = num1 ** num2

    if (
        operation in ["Addition", "Subtraction", "Multiplication", "Power"]
        or (operation == "Division" and num2 != 0)
        or (operation == "Modulus" and num2 != 0)
    ):
        st.success(f"Result: {result}")

st.markdown("---")
st.caption("Developed using Python & Streamlit")