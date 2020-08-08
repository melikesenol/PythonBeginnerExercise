def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(f'Please enter only numbers {err}')
        print(err)


print(sum(1,0))
print(sum('1', 2))