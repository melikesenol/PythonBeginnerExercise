def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        print("this is temp" + str(temp))
        print("---------")
        a = b
        print("this is a " + str(a))
        print("-----------")
        b = temp + b
        print("this is b " + str(b))


for x in fib(3):
    print(x)

