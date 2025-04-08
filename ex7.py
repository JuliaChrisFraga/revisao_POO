
class Categoria():
    def __init__(self, nome):
        self.nome = nome

catEletro = Categoria("Eletrônicos")
catLivro = Categoria("Livros")

class Avaliacoes():
    def __init__(self, cliente, comentario, nota):
        self.cliente = cliente
        self.comentario = comentario
        self.nota = nota
    def __str__(self):
        return f"{self.cliente} diz: {self.comentario} e dá nota {self.nota} ao produto."


class Produto():
    def __init__(self, nome, preco, estoque, categoria): #lado n recebe categoria
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.categoria = categoria
        self.avaliacoes = []
        
    def _validar_preco(self):
        if (self.__preco > 0):
            return True
        else:
            return False
    def alterar_preco(self, novo_preco):
        try:
            novo_preco = float(novo_preco)
            if (novo_preco > 0):
                self.preco = novo_preco
                print("Preço alterado com sucesso.")
            else:
                print("Valor inválido. Tente novamente.")
        except ValueError:
            print("Por favor, digite apenas números.")

    def vender(self, qtd):
        try:
            qtd = float(qtd)
            if (qtd > 0) and (qtd % 1 == 0):
                self.estoque = self.estoque - qtd
                print("Vendido com sucesso.")
            else:
                print("Valor inválido. O valor deve ser maior que zero e inteiro.")
        except ValueError:
            print("Por favor, digite apenas números.")
    
    def reabastecer(self, qtd):
        try:
            qtd = float(qtd)
            if (qtd > 0) and (qtd % 1 == 0):
                self.estoque = self.estoque + qtd
                print("Reabastecido com sucesso.")
            else:
                print("Valor inválido. O valor deve ser maior que zero e um número inteiro.")
        except ValueError:
            print("Por favor, digite apenas números.")
    
    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)
        return f"Avaliado com sucesso!"
    
    def exibir_detalhes(self):
        return f"Produto: {self.nome}; \nPreço: {self.preco}; \nEstoque: {int(self.estoque)}."
    
    def __str__(self):
        return f"O produto '{self.nome}'' custa R${self.preco} reais e atualmente há {int(self.estoque)} dele no estoque da loja."

prod1 = Produto("Iphone 15 pro max", 25000, 1, catEletro)
prod2 = Produto("Como conseguir um Iphone 15 pro max", 10, 50, catLivro)


class Loja():
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []
        
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        return f"Produto adicionado com sucesso!"
    
    def listar_estoque(self):
        print("Estoque da loja:")
        for produto in self.produtos:
            print(produto)

loja = Loja("Papaya")

print(loja.adicionar_produto(prod1))
print(loja.adicionar_produto(prod2))

prod2.vender(2)
prod1.reabastecer(3)

av1 = Avaliacoes("Julia", "Queria rosa mas veio magenta", 6)
#prod1.adicionar_avaliacao(av1)
#print(prod1.avaliacoes)

print(loja.listar_estoque())
