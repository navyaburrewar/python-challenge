# Basic Level Questions — sys.argv

# 1. What does sys.argv store?
# → It stores the command-line arguments passed to a Python script.


# 2. What is the data type of sys.argv?
# → It is a list.


# 3. What does sys.argv[0] contain?
# → It contains the script filename (or path).


# 4. How do you access the first user-provided argument?
# → sys.argv[1]


# 5. Are command-line arguments stored as strings or numbers?
# → Strings.


# 6. How do you convert a command-line argument to an integer?
# → int(sys.argv[index])


# 7. What function tells you how many arguments were passed?
# → len(sys.argv)


# 8. What error occurs if you access a missing argument index?
# → IndexError (list index out of range)


# 9. Write a command to run app.py with arguments 10 and 20.
#3 python app.py 10 20


# 10. Why is argument length checking important?
# → To prevent errors when required arguments are missing.


# 11. Which module must be imported to use argv?
# → sys


# 12. What will len(sys.argv) return if no arguments are passed?
# → 1 (only the script name)


# 13. How do you print all command-line arguments?
# → print(sys.argv)


# # 14. How do you safely stop a program if arguments are missing?
# → Use sys.exit()


# 15. What is the index of the second command-line argument?
# → 2


# 16. True or False: sys.argv can store integers directly.
# → False


# 17. How do you multiply two numbers passed via command line?

# a = int(sys.argv[1])
# b = int(sys.argv[2])
# print(a * b)


# 8. What happens if you forget to import sys?
# → NameError occurs (sys is not defined)



# Can we run a Python script without command-line arguments?
# → Yes   ### which is noting  but not  “Without command-line arguments means we don’t give inputs in the same line while running the program


# 20. Is sys.argv mutable (can it be changed)?
# → Yes (it’s a list)


#  20. Is sys.argv mutable (can it be changed)?
# # → Yes (it’s a list)