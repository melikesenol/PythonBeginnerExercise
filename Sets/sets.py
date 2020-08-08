my_set = {1, 2, 3, 4, 5}  # unordered collection of unique objects

print(my_set)

# not contain same values

my_set.add(100)
my_set.add(2)

print(my_set)

my_list = [1, 2, 3, 4, 5, 5]
print(set(my_list))  # removed duplicate 5

print(my_set[0])    # error set object does not support indexing

print(len(my_set))  # only count unique objects

new_set = my_set.copy()  # new copy

my_set.clear()

print(new_set)
print(my_set)


