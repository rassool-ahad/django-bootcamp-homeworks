class A:
    def do_job(self):
        print("its class A")
        print('I am walking ...')


class Z:
    def do_job(self, n):
        print("its class Z")
        print(f'I am counting from 1 to {n}:  {list(range(1, n + 1))}')


class B(A):
    def do_job(self, s, n):
        print("its class b ")
        A.do_job(A.__new__(A))
        print(f'I am printing your string : "{s}"')


class C(A, Z):
    def do_job(self, s, n):
        print("its class c")
        super().do_job(s, n)
        print('I am jumping ...')


class D(B):
    def do_job(self, s, n):
        print("its class D")
        super().do_job(s, n)
        print('I am speaking ...')


class E(D, C):
    def do_job(self, s, n):
        print("its class E")
        super().do_job(s, n)
        print('I am laughing ...')


class F(Z, B):
    def do_job(self, s, n):
        print("its class F")
        Z.do_job( Z.__new__(Z), n)
        print('I am playing ...')

print(E.mro())


obja = A()
obja.do_job()

print()
objz = Z()
objz.do_job(3)

print()
obje = E()
obje.do_job('Python', 5)

print()
objf = F()
objf.do_job('Python', 6)
