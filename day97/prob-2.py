## sys.path 
# import sys
# print(sys.path)


# import sys
# for p in sys.path:
#     print(p)


    ## To see all the folders where Python looks for modules.




##  2 — Add a new folder to search path
# Code: 
import sys
sys.path.append("C:/MyModules")


   ## If you have your own Python files in another folder, Python won’t find them unless that folder is in sys.path.



import sys
print("C:/MyModules" in sys.path)


            ## To avoid adding the same folder many times.