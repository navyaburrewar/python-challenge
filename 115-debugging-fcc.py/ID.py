# Beginner-Friendly Explanation of IDE Debugging Tools
# What is an IDE?

# An IDE stands for:

# Integrated Development Environment

# It is a software where you write and run code.

# Examples:

# Visual Studio Code
# PyCharm

# Think of an IDE like a smart coding workspace.

# It helps you:

# write code
# run code
# find errors
# debug programs
# What is Debugging?

# Debugging means:

# finding and fixing mistakes (bugs) in your program.

# Sometimes programs:

# give wrong output
# crash
# behave unexpectedly

# Debugging helps you understand WHY.

# What are IDE Debugging Tools?

# IDE debugging tools help you:

# ✅ pause the program
# ✅ inspect variable values
# ✅ run code step-by-step
# ✅ understand program flow

# Instead of using many print() statements, IDE debugging gives a visual way to inspect code.

# Example Program

# Create a file named:

# main.py

# Add this code:

# def divide(a, b):
#     result = a / b
#     return result

# print(divide(10, 2))
# print(divide(15, 3))
# Understanding the Code First
# Function
# def divide(a, b):

# Creates a function named:

# divide

# It takes 2 values:

# a
# b
# Division Line
# result = a / b

# This divides:

# a ÷ b

# and stores answer in:

# result
# Return Statement
# return result

# This sends answer back.

# Function Calls
# print(divide(10, 2))
# print(divide(15, 3))

# First call:

# 10 / 2 = 5.0

# Second call:

# 15 / 3 = 5.0

# Output:

# 5.0
# 5.0
# Step 1: Set a Breakpoint
# What is a Breakpoint?

# A breakpoint means:

# “Pause the program HERE.”

# It lets you stop program execution at a specific line.

# How to Set Breakpoint in VS Code

# In Visual Studio Code:

# Find this line:

# result = a / b

# Now click LEFT side of line number.

# You will see:

# 🔴 Red Dot

# This red dot means:

# breakpoint is active

# Why Breakpoints are Useful

# Breakpoints help you:

# pause before problem happens
# inspect variables
# understand step-by-step execution
# Step 2: Start Debugging

# Now press:

# F5

# OR

# Go to:

# Run → Start Debugging
# What Happens Now?

# Program starts running.

# When it reaches breakpoint:

# result = a / b

# program PAUSES automatically.

# VERY IMPORTANT

# At this moment:

# result = a / b

# has NOT executed yet.

# Debugger is waiting for your action.

# Step 3: Inspect Variables

# When paused, VS Code shows variable values.

# You can inspect variables in 3 ways.

# Method 1: Hover Mouse

# Move mouse over:

# a

# You may see:

# 10

# Move over:

# b

# You may see:

# 2
# Method 2: Variables Panel

# On LEFT side you see:

# VARIABLES panel

# It may show:

# Variable	Value
# a	10
# b	2

# This helps you see program state.

# Method 3: Debug Console

# At bottom you can type:

# a + b

# Output:

# 12

# This helps test expressions during debugging.

# Step 4: Step Through Code

# Now debugger toolbar appears.

# It contains buttons.

# Continue (F5)
# Meaning

# Continue normal execution.

# Program keeps running until next breakpoint.

# Step Over (F10)
# Meaning

# Execute ONE line and move to next line.

# Example:

# Current line:

# result = a / b

# Press:

# F10

# Now line executes.

# Result becomes:

# 5.0

# Debugger moves to:

# return result
# Step Into (F11)
# Meaning

# Go INSIDE a function.

# Useful when you want to see how function works internally.

# Example

# Suppose current line is:

# divide(10, 2)

# Press:

# F11

# Debugger enters:

# def divide(a, b):
# Step Out (Shift + F11)
# Meaning

# Exit current function.

# Suppose you are inside:

# divide()

# Press:

# Shift + F11

# Debugger leaves function.

# Why IDE Debugging is Better Than print()

# Without debugger people use:

# print(variable)

# everywhere.

# But IDE debugger is easier because:

# print()	IDE Debugger
# Manual	Visual
# Many print statements	Automatic inspection
# Hard in large programs	Easier navigation
# Cannot pause properly	Full control
# Three Common Debugging Methods
# 1. Using print()

# Example:

# print(a)

# Good for:

# quick checks
# tiny programs
# 2. Using pdb

# Example:

# pdb.set_trace()

# Good for:

# terminal debugging
# interactive debugging
# 3. Using IDE Debugger

# Good for:

# visual debugging
# large projects
# beginner learning
# professional coding
# Real-Life Analogy

# Imagine your code is a movie.

# print()

# Like shouting updates during movie:

# “Now hero entered!”

# pdb

# Like pausing movie manually and inspecting details.

# IDE Debugger

# Like having movie controls:

# ▶️ play
# ⏸️ pause
# ⏭️ next frame
# 👀 inspect scene

# Simple Debugging Flow
# Write Code
#     ↓
# Add Breakpoint 🔴
#     ↓
# Press F5
#     ↓
# Program Pauses
#     ↓
# Inspect Variables
#     ↓
# Press F10
#     ↓
# One Line Executes
#     ↓
# Variables Update
#     ↓
# Press F5
#     ↓
# Program Ends
# Final Summary

# IDE debugging tools help you:

# ✅ pause programs
# ✅ inspect variables
# ✅ run code step-by-step
# ✅ understand program flow
# ✅ find bugs easily

# Important Shortcut Keys
# Key	Action
# F5	Continue
# F10	Step Over
# F11	Step Into
# Shift+F11	Step Out
# Most Important Beginner Understanding

# Debugging is NOT just fixing errors.

# It is:

# understanding what your program is doing internally step-by-step.