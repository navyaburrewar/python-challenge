# 1️⃣ sys.exit() — Exit the program safely
# ✅ Purpose:

# Stops the program immediately and exits Python.

# 🧠 When used:
# To end a program early
# To stop execution when an error happens


##  some of major differences that the  interview ask

#diffrences


# 🔹 1️⃣ return vs sys.exit()
# Feature	           return	               sys.exit()
# Scope	              Exits a function only	    Stops the entire program
# Where used	       Inside functions                 	Anywhere
# Program continues?	✅ Yes	                     ❌ No
# Use case	           Send result back	          Terminate program




##  break vs sys.exit()


# | Feature            | `break`         | `sys.exit()`         |
# | ------------------ | --------------- | -------------------- |
# | Scope              | Exits loop only | Exits entire program |
# | Works in           | Loops           | Anywhere             |
# | Program continues? | ✅ Yes           | ❌ No                 |





### continue vs sys.exit

# | Feature | `continue`                  | `sys.exit()`            |
# | ------- | --------------------------- | ----------------------- |
# | Purpose | Skip current loop iteration | Stop program completely |
# | Scope   | Loop only                   | Whole program           |



# ## existing a loop

# for i in range(5):
#     if i == 2:
#         break
#     print(i)

# print("Program continues...")


# ## output

# 0
# 1
# Program continues...




# ### exsiting a program

# import sys

# for i in range(5):
#     if i == 2:
#         sys.exit()
#     print(i)

# print("Program continues...")




# ## output

# 0
# 1