## Write a program to:

# 🎲 Simulate rolling two dice

# 🃏 Pick 5 random cards from a deck

# 🎟 Generate a lottery ticket

# 🔐 Create a random password

# 👥 Randomly divide people into teams



# 🎲 Simulate rolling two dice

import random

dice1=random.randint(1,6)
dice2=random.randint(1,6)
print("dice1 :",dice1)
print("dice2 :",dice2)

## 
# 🃏 Pick 5 random cards from a deck



import random

cards = random.sample(range(1, 53), 5)
print(cards)