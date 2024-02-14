# Checks that users enter an integer
# that is more than 13
while True:

    error = "Please enter an integer that is 13 or more"

    try:
        my_num = int(input("Enter an integer: "))

        # checks that the number is more than / equal to 13
        if my_num < 13:
            print(error)

        else:
            print("Your number is", my_num)

    except ValueError:
        print(error)
