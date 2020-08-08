# Dictionary

user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

print(user.get('age'))  # None - Error handling
print(user.get('basket'))
print(user.get('age', 55))  # If age does not exist then print 55

user2 = dict(name='John')   # Another creating dict method with built-in func
print(user2)

print('basket' in user.keys())
print('hello' in user.keys())
print('hello' in user.values())
print(user.items())

user3 = user.copy()
print(user)
print(user3)

print(user.clear())
user.clear()
print(user)

print(user.pop('age')) # returns popped age key's value
print(user.popitem())  # randomly popps off something

user.update({'age': 55}) # age updated


