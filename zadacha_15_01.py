class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.sum = 0

        def sum():
            self.sum = self.a + self.b + self.c

        sum()
    
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))


tri = Triangle(a,b,c)

print("Sum of triangle is :",tri.sum)