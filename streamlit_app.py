import streamlit as st

st.markdown(':red[**Application to find the largest of 3 numbers**]')

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
st.markdown(':blue[**The largest number is: **]')
st.write(maximum)
