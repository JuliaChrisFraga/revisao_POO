from abc import ABC, abstractmethod
import math

class figuraGeometrica(ABC):
    def __init__(self, nome):
        self.nome = nome
        @abstractmethod
        def area(self):
            pass
        @abstractmethod
        def perimetro(self):
            pass

class Circulo(figuraGeometrica):
    def __init__(self, r):
        super().__init__(nome="Círculo")
        self.r = r
    
    def area(self):
        area = round(math.pi * math.pow(self.r, 2),2)
        return area
    
    def perimetro(self):
        perimetro = round(2 * math.pi * self.r,2)
        return perimetro

class Retangulo(figuraGeometrica):
    def __init__(self, altura, largura):
        super().__init__(nome="Retângulo")
        self.altura = altura
        self.largura = largura
    
    def area(self):
        area = round(self.altura * self.largura,2)
        return area
    
    def perimetro(self):
        perimetro = round(2*self.altura + 2*self.largura,2)
        return perimetro

class Triangulo(figuraGeometrica):
    def __init__(self, lado1, lado2, lado3):
        super().__init__(nome="Triângulo")
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def area(self):
        semi = (self.lado1 + self.lado2+ self.lado3)/2
        area = math.sqrt(semi * (semi - self.lado1) * (semi - self.lado2) * (semi - self.lado3))
        area = round(area,2)
        return area
    
    def perimetro(self):
        perimetro = self.lado1 + self.lado2 + self.lado3
        perimetro = round(perimetro,2)
        return perimetro

c1 = Circulo(15)
c2 = Circulo(20)
r1 = Retangulo(3,4)
r2 = Retangulo(6,10)
t1 = Triangulo(2,3,4)
t2 = Triangulo(5,6,7)
lista = [c1, c2, r1, r2, t1, t2]

for objeto in lista:
    print("Nome:", objeto.nome, "|| área:", objeto.area(), "|| perímetro:", objeto.perimetro(), ";")
