basket = [1, 2, 3, 4, 5]

# adding

new_list = basket.append(100)  # append changes list in place
print(basket)
print(new_list)

new_list = basket
print(basket)
print(new_list)

# insert

basket.insert(4, 100)  # insert with index
new_list = basket
print(new_list)

# extend

new_list = basket.extend([100, 101])
print(basket)
print(new_list)

# remove

basket.pop()
print(basket)
basket.remove(2)
print(basket)

basket2 = [5, 6, 7, 8, 9]

print(basket2.index(5))
print(basket2.index(5, 0, 1))

print('d' in basket2)
print(5 in basket2)

print(basket2.count('d'))
print(basket2.count(5))

print(basket2.sort()) # Prints none

basket2.sort()
print(basket2) # Returns sorted list

print(sorted(basket2)) # Sorted() produces a new list

basket2.reverse() # Reverses the list

basket2.sort()
basket2.reverse() # High to low reverse

range(list(1,100))

sentence = '!'

new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'jojo'])

print(sentence)
print(new_sentence) # hi!my!name!is!jojo

# LİST UNPACKING

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
print(d)








