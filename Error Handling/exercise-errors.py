#   Error Handling
while True:
    try:
        age = int(input("What is your age? "))
        10/age
    except ValueError:
        print("Please enter a valid number")
        continue
    except ZeroDivisionError:
        print("Please enter a number higher than 0")
        break
    else:
        print("Thank you")
        
    finally:
        print('ok, im finally done')
    print("can you hear me")


#   We only want integers
#   Except blocks runs only once
#   Finally runs at the end regardless
