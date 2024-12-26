import random

# The user is asked to enter a two-digit account code.
code_pin=input('Entre a 2-digit PIN cod:')

# Create a variable named computer
Computer=random.randint(10,90)

# If the code entered by the user is compatible with the computer, congratulations, you have found the correct number.
if code_pin==Computer:
    print('Congratulations, you have found the right number.')



elif len(code_pin)>2  or  len(code_pin)<2:
    print('Please type 2 digits PIN')

else:
   print(f"""Faliure! PIN code did not match.
   The Computer generated this  PIN :{Computer}""")

