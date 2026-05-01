# #  ##########################.re.ASCII	re.A	Returns only ASCII matches############

# # What does \w mean in regex?

# # 👉 \w = “word characters”

# # It matches:

# # Letters (a–z, A–Z)
# # Digits (0–9)
# # Underscore (_)


# import re

# text = "café"
# pattern = r"\w+"

# print(re.findall(pattern, text))              # default  ['café']
# print(re.findall(pattern, text, re.ASCII))    # ASCII only  ['caf']



# ############# re.DEBUG	Returns debug information  ##################

# import re
# re.compile(r"\d+", re.DEBUG)


# # What is re.DEBUG?
# # re.DEBUG is a flag that prints how your regex is interpreted internally by Python.

# # 👉 It does NOT change matching results
# # 👉 It is used only for:

# # Learning regex
# # Debugging complex patterns

# # Think of it like:

# # “Show me how Python understands my regex step by step”



# # 🔹 Why is it useful?
# # When your regex:
# # is not working
# # is too complex
# # gives unexpected results

# # 👉 re.DEBUG helps you see the internal structure


# import re
# pattern = r"(cat|dog)"
# re.compile(pattern,re.DEBUG)



class employ :
    def  main (self):
        print("look after entire work")

class developer(employ):
    def sub(self):
        print("only developing")        
c1= developer()
c1.main()
c1.sub()