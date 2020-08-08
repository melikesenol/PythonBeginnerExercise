# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': False  # changing this will either run or not run the message_friends function.
}

user2 = {
    'name': 'Dick',
    'valid': True
}


def authenticated(fn):
    def wrap(*args, **kwargs):
        print('checking for authorize')
        if args[0]['valid']:
            return fn(*args, *kwargs)
        else:
            print('auth failed')
    return wrap


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user2)
message_friends(user1)