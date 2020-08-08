#   Generators are subsets of iterables


def generator_function(num):
    for i in range(num):
        yield i + 1  # this is the difference with a standar for loop to make list yield pauses function


g = generator_function(100)
next(g) # 0 * 2
next(g) # 1 * 2             next throws error if we reach end of the index StopIteration
print(next(g))  # 2 * 2     yield pauses next continues the function
