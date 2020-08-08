#   *args **kwargs

def super_func(name, *args, i='hi', **kwargs):  # rule
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1,2,3,4,5, num1=5, num2=10))

# args ---> tuples

# kwargs ----> dictionary (keyword-args)

# rule: params, *args, default params, **kwargs