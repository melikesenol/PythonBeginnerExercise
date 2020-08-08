#   Ternary Operator

is_friend = True

can_message = "message allowed" if is_friend else "not"

print(can_message)

#   Short Circuting

is_magician = False
is_expert = False

#   Check if magician and expert: "you are a master"

#   Check if mag but not expert: "at least you're getting there"

#   If you're not a mag: "You need magic powers"

if is_magician == True and is_expert == True:
    print("You are a master")
elif is_magician == True and is_expert == False:
    print("At least you're getting there")
elif not is_magician:
    print("You need magic powers")

#   == vs is

#   is checks location of memory is the same

# print(True is True)
# print(1 is 1)
# print([] is [])    False
# print(10 is 10)    True


user = {
    'age': 15,
    'name': "anil",
    'sex': "male"
}

for item in user.values():
    print(item)
