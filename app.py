import streamlit as stream

def largest(num1,num2,num3):
    return max(num1,num2,num3)


stream.title('Find the Largest Number')

num1 = stream.number_input('Enter first number', value=0.0)
num2 = stream.number_input('Enter second number', value=0.0)
num3 = stream.number_input('Enter third number', value=0.0)

if stream.button('Find Largest'):
    largest = largest(num1,num2,num3)
    stream(f'The largest number is: {largest}')

