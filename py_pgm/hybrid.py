class A:
    def m(self):
        print("m of A called")


class B(A):
    def p(self):
        print("m of b called")


class C(A):
    def f(self):
        print("m of C called")


class D(B, C):
    def r(self):
        print("m of d called")
        B.p(self)
        C.f(self)


x = D()
x.r()
x.m()
x.f()
x.p()