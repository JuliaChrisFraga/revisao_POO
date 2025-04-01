class Domino():
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
    
    def mostrar_pontos(self):
        mensagem = f"Lado A: {self.a}; Lado B: {self.b}."
        return mensagem
    
    def valor(self):
        soma = self.a + self.b
        return soma
    
    def  __str__(self):
        return f'({self.a},{self.b})'

d1=Domino(2,6)
d2=Domino(4,3)
print(d1.mostrar_pontos())
print(d2.mostrar_pontos())
print("Total de pontos: ", d1.valor())
print("Total de pontos: ", d2.valor())
print(d1.__str__())