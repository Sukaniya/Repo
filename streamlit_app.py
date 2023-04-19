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

# take inputs
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
num3 = float(input('Enter third number: '))

# function call
maximum = findLargest(num1, num2, num3)

# display result
print('The largest number = ',maximum)