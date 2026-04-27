# Simulate an ATM that keeps asking for a PIN
# The loop stops when the correct PIN is entered

# Correct PIN stored in the system
correct_pin = 1234

# User's first attempt (wrong on purpose)
user_pin = 0

# Counter to track number of attempts
attempts = 0

# Loop runs while the user enters the wrong PIN
while user_pin != correct_pin:
    user_pin = int(input("Please enter your PIN: ")) # Ask for PIN input
    attempts += 1.                                   # Count the attempt

    # If wrong, warn the user
    if user_pin != correct_pin:
        print("Incorrect PIN. Please try again.")

# When the loop ends, the PIN was correct
print("Acess granted! ")
print ("Number of attempts: ", attempts)
