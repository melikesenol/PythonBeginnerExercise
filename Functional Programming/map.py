#   map, filter, zip, reduce
my_list = [1, 2, 3]


def multiply_by2(item):
    return item * 2


print(list(map(multiply_by2, my_list)))   # action did to data on multiply_by2
new_list = list(map(multiply_by2, my_list))
print(new_list) # we created a new list with map func
print(my_list)  # map is pure function so my_list does not changed


#   nothing interacts with outside so this is a pure functions
#   pure functions = less bugs
#   impossible to use everywhere
