#  modifiers
#  A placeholder can also include a modifier to format the value.
#  A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
#  

price =59
txt =f"the price is {price: .2f} dollars"
print(txt)



# You can also format a value directly without keeping it in a variable:

# Display the value 95 with 2 decimals:
txt =f"the price is {95:.2f}dollars"
print(txt)