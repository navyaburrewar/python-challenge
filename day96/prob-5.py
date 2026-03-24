
## 2️⃣9️⃣ Demonstrate that finally runs even after sys.exit().



import sys

try:
    print("Inside try block")
    sys.exit()
finally:
    print("Finally block executed")