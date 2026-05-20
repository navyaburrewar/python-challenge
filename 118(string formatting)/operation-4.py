#  perform operations in f-strings
# You can perform Python operations inside the placeholders.



# ############33   ex-1 ######################3
#  You can do math operations:

txt =f"the price is {20*40} dollars"
print(txt)



# ################ ex-2 ##########################
# You can perform math operations on variables:

price=30
items=10
txt =f'total price is {price*items}'
print(txt)


##############3 if__else statements ####################

price=100
text=f"it is very {"expensive" if price>50 else "chea"}"
print(text)