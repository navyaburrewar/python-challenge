# Problem 15 — Notification System

# Create classes:

# EmailNotification
# SMSNotification
# PushNotification

# All should have method:

# send_message()

# Use polymorphism to call same method for all objects.


class EmailNotification:
    def send_message(self):
        print("you can send msg using email")
class SMSNotification:
    def send_message(self):       
        print("you can send msg using SMS")
class pushNotification:
    def send_message(self):       
        print("you can send msg using push")

e1=EmailNotification()
s1=SMSNotification()
p1=pushNotification()

e1.send_message()
s1.send_message()
p1.send_message()

