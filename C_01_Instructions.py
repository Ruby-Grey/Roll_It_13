print("🎲 Roll it 13 🎲")


# loop for testing purposes

while True:
    want_instructions = input("Would you like to read the instructions? ").lower()

    if want_instructions == "yes" or want_instructions == "y":
        print("You chose to see the instructions")
    elif want_instructions == "no" or want_instructions == "n":
        print("You do not wish to see the instructions")
    else:
        print("Please choose a valid answer :(")