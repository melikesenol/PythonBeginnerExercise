my_list = [5, 4, 3]

print(list(map(lambda item: item**2, my_list)))

a = [(0, 2), (4, 3), (9, 9), (10, -1)]

print(a.sort(key=lambda x: x[1]))   # sorted by second item lowest to highest we adjusted the sorting with power of lamb
print(a)