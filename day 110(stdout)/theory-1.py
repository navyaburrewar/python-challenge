# 🔹 What is sys.stdout?

# In Python, sys.stdout is part of the built-in module sys module.

# 👉 Meaning:
# stdout stands for Standard Output
# It is the default place where Python sends output
# By default, it points to your console/terminal screen





## difference : print() vs sys.stdout.write()

# | Feature                    | print() | sys.stdout.write()   |
# | -------------------------- | ------- | -------------------- |
# | Adds newline automatically | ✅ Yes   | ❌ No                 |
# | Easier to use              | ✅ Yes   | ❌ Slightly low-level |
# | Needs import               | ❌ No    | ✅ Yes                |




# 🔹 Simple rule to remember
# Use print() → easy, normal use
# Use sys.stdout.write() → when you want control or performance




# print() → automatically moves to the next line
# sys.stdout.write() → stays on the same line unless you add \n


# 🔹 But actually what's happening internally:
# print("Hi") → prints "Hi\n" (newline added automatically)
# sys.stdout.write("Hi") → prints just "Hi" (no newline)