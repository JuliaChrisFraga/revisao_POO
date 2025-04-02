class Produto():
    def __init__(self, __nome, __preco, __estoque):
        self.__nome = __nome
        self.__preco = __preco
        self.__estoque = __estoque
    
    def __validar_preco(self):
        if (self.__preco > 0):
            return True
        else:
            return False
    
    def alterar_preco(self, novo_preco):
        try:
            novo_preco = float(novo_preco)
            if (novo_preco > 0):
                self.__preco = novo_preco
                print("Preço alterado com sucesso.")
            else:
                print("Valor inválido. Tente novamente.")
        except ValueError:
            print("Por favor, digite apenas números.")

    def vender(self, qtd):
        try:
            qtd = float(qtd)
            if (qtd > 0) and (qtd % 1 == 0): #para ver se é inteiro (não foi o gepeto que escreveu isso, foi eu mesmo)
                self.__estoque = self.__estoque - qtd
                print("Vendido com sucesso.")
            else:
                print("Valor inválido. O valor deve ser maior que zero e inteiro.")
        except ValueError:
            print("Por favor, digite apenas números.")
    
    def reabastecer(self, qtd):
        try:
            qtd = float(qtd)
            if (qtd > 0) and (qtd % 1 == 0):
                self.__estoque = self.__estoque + qtd
                print("Reabastecido com sucesso.")
            else:
                print("Valor inválido. O valor deve ser maior que zero e um número inteiro.")
        except ValueError:
            print("Por favor, digite apenas números.")
    
    def exibir_detalhes(self):
        return f"Produto: {self.__nome}; \nPreço: {self.__preco}; \nEstoque: {int(self.__estoque)}."
    
    def __str__(self):
        return f"O produto {self.__nome} custa R${self.__preco} reais e atualmente há {int(self.__estoque)} dele no estoque da loja."
    
p1 = Produto("banana", 12.00, 122)

p1.alterar_preco(-5)
p1.alterar_preco("ABC")
p1.alterar_preco(5)
print("\n")
p1.vender(3.5)
p1.vender("abc")
p1.vender(5)
print("\n")
p1.reabastecer(-5)
p1.reabastecer("abc")
p1.reabastecer(200)
print("\n")
print(p1.exibir_detalhes())