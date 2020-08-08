#   lambda func

#   lambda func are anonymous one time useable functions    -> lambda item: item*2, my_list


from functools import reduce


my_list = [1, 2, 3]


# def multiply_by2(item):     # if you want to only use once and im done with it
# return item * 2


print(list(map(lambda item: item * 2, my_list)))    # we commented out def but with lambda we can use it only once
print(my_list)
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda acc, item: acc + item, my_list))

#   nothing interacts with outside so this is a pure functions
#   pure functions = less bugs
#   impossible to use everywhere
