# Checks that users enter an integer
# that is more than 13
def int_check():

    while True:

        error = "Please enter an integer that is 13 or more"

        try:
            response = int(input("Enter an integer: "))

            # checks that the number is more than / equal to 13
            if response < 13:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


# main routine
target_score = int_check()
print(target_score)
