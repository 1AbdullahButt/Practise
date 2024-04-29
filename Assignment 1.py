#!/usr/bin/env python
# coding: utf-8

# In[16]:


# Task 1: Variables and Data Types
# a) Create three variables: one for storing your age (integer), one for your name (string), and one to
# check if you are a student (Boolean). Print the variables.


age = 25
name = 'Abdullah'
student = True

print(f'My age is {age}')
print(f'My name is {name}')
print(f'I am student {student}')

print('\n-----------------------------\n')

# b) Perform the following operations and print the results:
# - Add 25 to your age variable.
# - Concatenate your name with the string "Smith"
# - Negate the Boolean variable (if True, make it False, and vice versa).

age += 25
name += ' ' + 'Smith'    # added an extra space
student = not True

print(f'My age is {age}')
print(f'My name is {name}')
print(f'I am student {student}')


# In[17]:


# # Task 2: Expressions and Operators
# # a) A rectangle has a width of 5.5 units and a height of 3.25 units. Store width and height in variables. 
# Create a new variable called area and write an expression to calculate the area. Print the area in the output. 


width = 5.5
height = 3.25
area = width * height  # Area of Rectangle = w * h

print(f'Area of rectangle is = {area}')



print('\n-----------------------------\n')

# # b) Create a temperature variable in Celsius. Convert it to Fahrenheit using the formula:
# F = (C * 9/5) + 32. Store this temperature in a variable called Fahrenheit and print this variable.


C = float(input('Enter the temperature in Celsius = '))
F = (C * 9/5) + 32
print(f'This is the temperature in Fahrenheit then = {F}')



print('\n-----------------------------\n')

# # a) Create a variable called radius and give it a value of 5. 
# Calculate the area of a circle with this radius and store it in a variable called area. 
# Print area at the end of your code. (Use the formula: area = π * radius^2, where π (pi) is approximately 3.14159). 


radius = 5
area = 3.14 * radius**2

print(f'The area of circle with radius {radius} is = {area}')




# In[4]:


# Task 3: Introduction to Data Structures
# a) Create a list called "fruits" containing the following 
# fruits: "apple," "banana," "orange," "grape," and "kiwi." Print the list.


fruits = ['apple','banana','orange','grape','kiwi']
print(f'This is a list of fruits {fruits}')


print('\n-----------------------------\n')


# b) Create a tuple named "months" with the names of the first three months of the year. Print the tuple.

months = ('January','February','March')
print(f'This is a tuple of months {months}')





# In[14]:


# Task 4: List Manipulation
# a) Given the list of numbers below, write a Python program to 
# calculate the sum and average of these numbers. Print both results.
#    numbers = [12, 34, 45, 67, 89, 100, 23, 56]

numbers = [12, 34, 45, 67, 89, 100, 23, 56]

total = sum(numbers)

average = total/len(numbers)


print(f'This is the sum of the above list {total}')
print(f'This is the average of the above list {average}')


print('\n-----------------------------\n')



# b) Remove the first and last elements from the "fruits" list created earlier. Print the updated list.


fruits = ['apple','banana','orange','grape','kiwi']

fruits.pop(0)
fruits.pop(3)

print(f'This is the list named fruits, after we removed its first and last elements {fruits}')

