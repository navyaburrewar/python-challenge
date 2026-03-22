# Write a program that takes two numbers and an operator (+, -, *, /) from command line and performs the calculation.

# Example run:
# python calc.py 10 5 *


import sys

a = int(sys.argv[1])
b= int(sys.argv[2])
op =sys.argv[3]
if op =='+':
    print(a+b)
if op == '-':
    print(a-b)
if op == '*':
    print(a*b)
if op == '/':
    print(a/b)    
