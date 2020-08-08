#   High order function -> Excepts another function inside


#   Decorators Pattern


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('****')
        func(*args, **kwargs)
        print('******')

    return wrap_func

@my_decorator
def hello(greeting, emoji = ':('):
    print(greeting, emoji)

#   @my_decorator does = a = my_decorator(hello)


hello("hi")