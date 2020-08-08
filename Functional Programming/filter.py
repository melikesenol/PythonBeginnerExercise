#   map, filter, zip, reduce
my_list = [1, 2, 3]


def multiply_by2(item):
    return item * 2

def only_odd(item):
    return item % 2 != 0

def only_even(item):
    return item % 2 == 0


print(list(filter(only_odd, my_list)))  # filtered the list based on boolean expression on only_odd()
print(list(filter(only_even, my_list))) # prints only 2 based on boolean expr on only_evenn()
print(my_list)


#   nothing interacts with outside so this is a pure functions
#   pure functions = less bugs
#   impossible to use everywhere
