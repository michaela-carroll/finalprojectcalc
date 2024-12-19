import streamlit as st

# Set up the app title and description
st.title("Basic Calculator")
st.write("""
    This is a simple calculator that can perform addition, subtraction, multiplication, and division.
    Enter the values and choose the operation you want to perform.
""")

# Input fields for the numbers 
num1 = st.text_input("Enter first number")
num2 = st.text_input("Enter second number")

# Select operation (add, subtract, multiply, or divide)
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])


# Function to perform the calculations
def calculate(num1, num2, operation):
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtract":
        return num1 - num2
    elif operation == "Multiply":
        return num1 * num2
    elif operation == "Divide":
        if num2 == 0:
            return "Error! Division by zero."
        else:
            return num1 / num2

# Validate inputs
valid_num1 = validate_input(num1)
valid_num2 = validate_input(num2)

# Perform calculation when button is clicked
if st.button("Calculate"):
    if valid_num1 is None or valid_num2 is None:
        st.error("Please enter valid numbers.")
    else:
        result = calculate(valid_num1, valid_num2, operation)
        st.write(f"The result of {operation} is: {result}")
        
