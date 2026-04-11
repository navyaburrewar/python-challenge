### REGEX- here which is nothing but the regular expression
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#  RegEx can be used to check if a string contains the specified search pattern.


## regex module
# Python has a built-in package called re, which can be used to work with Regular Expressions.
## import re module


#  let see simple example to understand this thing first
import re
txt ="It is raining today"
x=re.search("^It.*today$",txt)
if x:
    print("yes! match")
else:
    print("not match")    


    ################# ex-2##################
    ## manually amw riting wrong code here
    ### see in the below code i hev given the first word as the wrong word
    ##in place of he i hav egave the am
    ## hence it was showing like not matched
import re

sen =" he is a boy"
x=re.search("^am.*boy$",sen)
if x:
    print("matched")
else:
    print("not matched")    


    ################# ex-3 #####################3

#3 in this example i gave last word as the wrong word here
import re
sentence="she drinks tea"
x=re.search("^she.*coffe$",sentence)
if x:
    print("matched")
else:
    print("not matched")    


