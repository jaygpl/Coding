#Learning to make an adventure simulator for users to interact with
#This was done using variables and strings to retreive user data that is written
print("=== Your Adventure Simulator ===")
print("""You'll be asked a bunch of questions then we'll
make you up an amazing story with YOU as the main character!""")
print()
name = input("Your name: ")
enemy = input("Your worst enemy's name: ")
superPower = input("Your super power: ")
print()
print("Our story begins as our hero name approaches a giant ominous castle...")
print("Suddenly a bolt of lightning striked the ground at the feet of", name)
print(" 'Our final battle begins!' shouts the evil", enemy, "clearly missing the fact that", name, "has the power of", superPower, "which means they'll win easily")

#I will be trying to learn how to add colour to text.
#This line of code "\033[31m" changes the colour of the text to red.
print()
print(" Uh, oh, you've been given a", "\033[31m", "warning", "\033[0m", "for being a bad, bad person.")