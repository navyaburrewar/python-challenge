# 🟢 Basic Understanding
# 1️⃣ Q: What is sys.exit() and why is it used?

# A:
# sys.exit() is a function from Python’s built-in Python Software Foundation sys module that stops the execution of a program.

# It is used when you want to:

# Terminate the program intentionally
# Stop execution after a fatal error
# Exit early based on a condition



# 2️⃣ Q: What happens internally when sys.exit() is executed?

# A:
# Internally:

# sys.exit() raises a special exception called SystemExit
# If not handled, Python:
# Cleans up resources
# Executes finally blocks
# Terminates the program
# Control returns to the operating system with an exit status



# 3️⃣ Q: What is the default exit status code if no argument is passed?

# A:
# The default exit status code is:

# 0

# Status code 0 means successful termination.




# 4️⃣ Q: What is the difference between:
# sys.exit()
# sys.exit(0)
# sys.exit(1)
# sys.exit("Error")

# A:

# Statement	Meaning
# sys.exit()	Same as sys.exit(0) → Successful exit
# sys.exit(0)	Success (no error)
# sys.exit(1)	Error / abnormal termination
# sys.exit("Error")	Prints "Error" and exits with failure status




# 5️⃣ Q: Why are exit status codes important for the operating system?

# A:
# Exit codes tell the operating system whether the program succeeded or failed.

# They are important because:

# Scripts can detect success/failure
# Automation tools rely on them
# Other programs can react accordingly

# Example:

# 0 → Success
# Non-zero → Error
# 🟡 Concept Clarity (Very Common)



# 6️⃣ Q: Difference between return, break, continue, and sys.exit()?

# A:

# Keyword	What it does
# return	Exits a function and sends a value back
# break	Exits the current loop
# continue	Skips current iteration, continues loop
# sys.exit()	Exits the entire program





# 7️⃣ Q: What is the difference between exiting a loop and exiting a program?

# A:

# Exiting Loop	Exiting Program
# Stops only the loop	Stops entire script
# Program continues	Program fully terminates
# Done using break	Done using sys.exit()




# 8️⃣ Q: Does code written after sys.exit() execute? Why?

# A:
# ❌ No, it does not execute.

# Because:

# sys.exit() raises SystemExit
# # Program stops immediately (unless caught)

# # Example:

# # import sys
# # sys.exit()
# # print("Hello")  # Won’t run




# # 9️⃣ Q: Does the finally block execute if sys.exit() is called?

# # A:
# # ✅ Yes, it executes.

# # Reason:

# # sys.exit() raises an exception
# # finally always runs during exception handling




# # 🔟 Q: Can sys.exit() be caught using try/except? If yes, how?

# # A:
# # ✅ Yes. Since it raises SystemExit, you can catch it.

# # Example:

# # import sys

# # try:
# #     sys.exit()
# # except SystemExit:
# # #     print("Exit prevented")




# # 🟠 Practical Usage
# # 1️⃣1️⃣ Q: When should you use sys.exit(1) instead of sys.exit()?

# # A:
# # Use sys.exit(1) when the program is terminating due to an error or failure.

# # sys.exit() → signals success
# # sys.exit(1) → signals something went wrong

# # Use it when:

# # Invalid input
# # File not found
# # Network failure
# # Any abnormal termination

# # This helps other programs and scripts detect failure correctly.

# # 1️⃣2️⃣ Q: In what kind of applications is exit status especially important?

# # A:
# # Exit status is especially important in:

# # Command-line tools → Other commands check success/failure
# # Shell scripts → Automation depends on exit codes
# # CI/CD pipelines → Build/test steps rely on status
# # System services & daemons → OS monitors health
# # Batch processing systems → Detect job success

# # Basically, anywhere programs interact with other programs.




# 1️⃣3️⃣ Q: Why is sys.exit() preferred over exit() in production code?
# ✅ Short Answer

# Because sys.exit() is the official, reliable way to terminate programs, while exit() is meant only for interactive use.

# 🧠 What’s the Difference?
# sys.exit()	exit()
# Part of Python’s standard sys module	Helper added for interactive shell
# Always available in scripts	May not work in some environments
# Used in real software	Meant for beginners & REPL use
# Raises SystemExit properly	Just a convenience wrapper

# exit() is provided for convenience in the interpreter managed by the Python Software Foundation tools, not for serious production systems.

# 🌍 Real-World Scenario

# Imagine you’re building:

# 🏦 A banking server app that must shut down safely if the database connection fails.

# Using something unofficial like exit() is risky — some runtime environments (embedded Python, services, containers) may not define it.

# You need a guaranteed and standard exit mechanism → sys.exit().

# 💻 Code Example

# ❌ Not recommended:

# # Might fail in some environments
# exit()

# ✅ Production-safe:

# import sys

# if not database_connected:
#     print("Database connection failed")
#     sys.exit(1)
# 1️⃣4️⃣ Q: What happens if an error occurs but you still exit using sys.exit() with no argument?
# ✅ Short Answer

# The program exits with status code 0 (success) — even though it failed.

# ⚠️ Why This Is Dangerous

# Operating systems and automation tools depend on exit codes.

# Exit Code	Meaning
# 0	Success
# Non-zero	Error

# If your program crashes but returns 0, the system thinks everything worked.

# 🌍 Real-World Scenario

# Imagine:

# 🤖 A nightly data backup script runs automatically.

# The script fails to copy files but ends with:

# sys.exit()

# The monitoring system sees exit code 0 and reports:

# ✅ Backup successful

# But actually:

# ❌ Backup failed — data is lost.

# 💻 Code Example

# ❌ Wrong way:

# import sys

# try:
#     process_files()
# except Exception:
#     print("Processing failed")
#     sys.exit()   # ❌ returns success code

# ✅ Correct way:

# import sys

# try:
#     process_files()
# except Exception:
#     print("Processing failed")
#     sys.exit(1)  # ✅ tells OS it failed
# 1️⃣5️⃣ Q: How does sys.exit("message") behave differently from print("message"); sys.exit(1)?

# This is a very common interview question.

# 🧠 Core Difference

# Both exit with failure, but how they display the message differs.

# Feature	sys.exit("message")	print("message"); sys.exit(1)
# How message is shown	As error from exception	As normal printed text
# Output stream	stderr (error stream)	stdout (normal output)
# Style	Short & compact	More readable & flexible
# Control	Less formatting control	Full formatting control
# 🌍 Real-World Scenario

# Imagine a command-line tool:

# $ python upload.py

# If login fails:

# Option A — sys.exit("Login failed")
# Message appears like a system error
# Good for quick fatal errors
# Option B — print("Login failed"); sys.exit(1)
# Cleaner user message
# Better for user-facing tools
# 💻 Code Examples
# 🔹 Method 1 — Message via sys.exit
# import sys

# if not login_success:
#     sys.exit("Login failed")

# Output:

# Login failed
# 🔹 Method 2 — Print then exit
# import sys

# if not login_success:
#     print("❌ Login failed. Please check credentials.")
#     sys.exit(1)

# Output:

# ❌ Login failed. Please check credentials.
