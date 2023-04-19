import streamlit as st

st.markdown("<h1 style='text-align: center; color: red;'> Application to find the largest of 3 numbers</h1>",unsafe_allow_html=True)

num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")
num3 = st.number_input("Enter the third number")


# Python program to find greatest of three numbers using function

def findLargest(num1, num2, num3):  #user-defined function
    # find largest numbers
    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3
    return largest  #return value

# function call
maximum = findLargest(num1, num2, num3)

# display result

st.markdown("<h4 style='color:blue;'> The largest number is: </h4>", unsafe_allow_html=True)
st.write(maximum)
