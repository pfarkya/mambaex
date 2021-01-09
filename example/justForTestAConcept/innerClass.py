class A:
    def __init__(self,a):
        self.a = a
    class B:
        def __init__(self,b):
            self.b = b

def test_main():
    a1 = A(2)
    a2 = A(3)
    if a1.B == a2.B:
        print("is equal")
    else:
        pring("not equal")
if __name__ == '__main__':
    test_main()
