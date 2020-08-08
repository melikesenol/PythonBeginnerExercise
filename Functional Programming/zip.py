#   map, filter, zip, reduce
my_list = [1, 2, 3]
your_list = [10, 20, 30]
their_list = [5, 4, 3]


def multiply_by2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


def only_even(item):
    return item % 2 == 0


print(list(zip(my_list, your_list, their_list)))    # like a zipper 1,10 becomes tuple 2,20 becomes tuple etc type does not matter
print(my_list)

#   nothing interacts with outside so this is a pure functions
#   pure functions = less bugs
#   impossible to use everywhere
