#   Exercise

evens = []

def highest_even(li):
    for i in li:
        if i % 2 == 0:
            evens.append(i)
    print(max(evens))

highest_even([1,2,3,4,5,6])

x = int(5)

print(x)