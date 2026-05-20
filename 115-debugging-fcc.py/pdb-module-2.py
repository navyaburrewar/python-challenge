# What is pdb in Python?

# pdb stands for:

# Python Debugger

# It is a built-in tool in Python that helps you:

# pause your program
# inspect variables
# check values
# move through code step by step
# find bugs/errors

# Think of it like a pause-and-investigate tool for your Python programs.

# The Code
# import pdb

# def divide(a, b):
#     pdb.set_trace()
#     return a / b

# print(divide(10, 2))
# Step-by-Step Explanation
# 1. import pdb
# import pdb

# This imports Python’s debugger module.

# Without importing it, Python would not know what pdb is.

# 2. Creating the Function
# def divide(a, b):

# This creates a function named divide.

# It takes 2 inputs:

# a
# b

# Example:

# divide(10, 2)

# means:

# a = 10
# b = 2
# 3. pdb.set_trace()
# pdb.set_trace()

# This is the MOST important line.

# It tells Python:

# “Pause the program HERE and open debugging mode.”

# When Python reaches this line:

# execution pauses
# terminal becomes interactive
# you can inspect the program

# This is called a breakpoint.

# What Happens When You Run It?

# When this line runs:

# print(divide(10, 2))

# Python enters the function:

# divide(10, 2)

# So now:

# a = 10
# b = 2

# Then Python reaches:

# pdb.set_trace()

# and pauses.

# Debugger Screen Output

# You may see something like:

# > /Users/fcc/Desktop/debugging.py(5)divide()
# -> return a / b
# (Pdb)

# Now let’s understand EACH PART.

# Understanding This Output
# > /Users/fcc/Desktop/debugging.py

# This shows:

# the file location
# where your Python file exists

# Example:

# /Users/fcc/Desktop/debugging.py

# means your file is named:

# debugging.py

# and stored on Desktop.

# (5)
# (5)

# means:

# Python is currently paused at line 5.

# divide()

# This shows the current function being executed.

# So currently Python is inside:

# divide()
# -> return a / b

# The arrow shows:

# the NEXT line Python will execute.

# Python has paused BEFORE executing:

# return a / b
# (Pdb)

# This is the debugger prompt.

# It means:

# "Now you can type debugging commands."

# Similar to:

# >>>

# in Python shell.

# Using help

# If you type:

# help

# inside the debugger:

# (Pdb) help

# you see a big list of commands.

# These commands help you control the debugger.

# Important Beginner Commands

# You do NOT need to memorize all commands.

# Start with these:

# Command	Meaning
# n	next line
# s	step into function
# c	continue running
# p variable	print variable
# q	quit debugger
# whatis	show type
# l	show code lines
# whatis Command

# Example:

# (Pdb) whatis a

# Output:

# <class 'int'>

# This means:

# variable a is an integer

# Because:

# a = 10

# and 10 is an integer.

# Another Example
# (Pdb) whatis divide

# Output:

# Function divide

# This tells us:

# divide is a function.

# Why is whatis Useful?

# It helps when:

# you're unsure what type a variable is
# debugging large programs
# checking objects/functions

# Example:

# name = "choti"

# then:

# whatis name

# shows:

# <class 'str'>

# because strings use str.

# Continue Execution

# Command:

# (Pdb) continue

# or shorter:

# (Pdb) c

# This tells Python:

# "Resume running normally."

# Then the program finishes:

# 5.0

# because:

# 10 / 2 = 5.0
# Why Result is 5.0 not 5?

# In Python:

# /

# always returns a float (decimal number).

# So:

# 10 / 2

# becomes:

# 5.0
# Full Flow of the Program

# Here is the entire flow:

# Step 1

# Program starts.

# Step 2

# divide(10, 2) is called.

# Step 3

# Inside function:

# a = 10
# b = 2
# Step 4

# Python hits:

# pdb.set_trace()

# Program pauses.

# Step 5

# Debugger opens:

# (Pdb)
# Step 6

# You inspect variables:

# whatis a
# p a

# etc.

# Step 7

# You continue execution:

# c
# Step 8

# Python executes:

# return a / b

# Result:

# 5.0
# Another Useful Command: p

# You can print values directly.

# Example:

# (Pdb) p a

# Output:

# 10

# Another:

# (Pdb) p b

# Output:

# 2
# Very Important Concept

# Debugging helps you answer questions like:

# Why is my variable wrong?
# Why is my loop failing?
# Why is function returning unexpected values?
# Which line causes the error?

# Instead of guessing, debugger lets you SEE the actual program state.

# Real-Life Analogy

# Imagine your program is a movie.

# Normally it runs continuously.

# pdb.set_trace() acts like:

# pressing PAUSE on the movie

# Then you can:

# inspect characters (variables)
# see current scene (line)
# move frame-by-frame (next)
# continue playback (continue)
# Example with Error Debugging
# import pdb

# def divide(a, b):
#     pdb.set_trace()
#     return a / b

# print(divide(10, 0))

# Now division by zero will fail.

# Before error happens, debugger pauses.

# You can inspect:

# p a
# p b

# Output:

# 10
# 0

# Then you quickly understand:

# problem is b = 0

# This is why debugging is powerful.

# Most Useful Beginner Commands Summary
# Command	What it does
# p variable	print variable
# n	go to next line
# s	step into function
# c	continue execution
# q	quit debugger
# l	show nearby code
# whatis variable	show type
# Small Practice Exercise

# Try this:

# import pdb

# def add(x, y):
#     pdb.set_trace()
#     result = x + y
#     return result

# print(add(5, 7))

# Inside debugger try:

# p x
# p y
# p result
# n
# p result
# c

# You’ll start understanding how values change step by step.

# Final Important Point

# pdb is mainly used in:

# debugging bugs
# understanding code flow
# learning Python internally
# inspecting complex programs