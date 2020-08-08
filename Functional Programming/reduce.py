#   map, filter, zip, reduce


from functools import reduce

my_list = [1, 2, 3]


def multiply_by2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


def only_even(item):
    return item % 2 == 0


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))  # like a zipper 1,10 becomes tuple 2,20 becomes tuple etc type does not matter
print(my_list)
print(reduce(accumulator, my_list, 10))

#   nothing interacts with outside so this is a pure functions
#   pure functions = less bugs
#   impossible to use everywhere
