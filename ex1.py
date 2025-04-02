import math

class Circle:
    def __init__(self, a, b, r):
        self.O = (a, b)
        self.r = r
    
    def area(self):
        area = math.pi * math.pow(self.r, 2)
        return area
    
    def perimetro(self):
        perimetro = 2 * math.pi * self.r
        return perimetro
    
    def test_pertencente(self, x, y):
        A = (x,y)
        distancia = math.sqrt(math.pow(A[0] - self.O[0], 2) + math.pow(A[1]- self.O[1], 2))  # Distância entre (x, y) e O
        if (distancia <= self.r):
            return True
        else:
            return False
    
    def __str__(self):
        return f"P={self.perimetro()}, A={self.area()}"

c1= Circle(2,2,3)
print(c1)
print(c1.test_pertencente(0,0))
print(c1.test_pertencente(0,-1))