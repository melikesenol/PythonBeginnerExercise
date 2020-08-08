#   Error Handling
while True:
    try:
        age = int(input("What is your age? "))
        10/age
    except ValueError:
        print("Please enter a valid number")
    except ZeroDivisionError:
        print("Please enter a number higher than 0")
    else:
        print("Thank you")
        break


#   We only want integers
#   Except blocks runs only once

