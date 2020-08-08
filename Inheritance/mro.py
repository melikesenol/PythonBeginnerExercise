

#   MRO - Method Resolution Order


class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass

#   Test


print(D.num)    # D->B->C->A
print(D.mro())  # Stops at C
