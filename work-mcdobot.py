# McDonald's bot
# Author: Tony
# Date: 2/21/2024

# Ask the user if they want a soda with their meal
soda = input("would you like a soda with your meal? please answer yes or no")

# If they answer yes, reply "here's your meal and a soda"
if soda == "yes":
    print("Here's your meal with a soda, enjoy!")

# If they answer no, reply "here's your meal with no soda"
elif soda == "no":
    print("Here's your meal with no fries, enjoy!")

# for any other answers, reply "I didn't understand what you said"
else:
    print("Sorry I don't undrestand what is {soda}.")