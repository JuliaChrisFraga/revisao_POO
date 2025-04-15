
class Categoria():
    def __init__(self, nome):
        self.nome = nome

    def __str__(self): #permite imprimir um objeto categoria
        return self.nome

catEletro = Categoria("Eletrônicos")
catLivro = Categoria("Livros")

class Avaliacoes():
    def __init__(self, cliente, comentario, nota):
        self.cliente = cliente
        self.comentario = comentario
        self.nota = nota
    def __str__(self):
        return f"{self.cliente} diz: '{self.comentario}', e dá nota {self.nota} ao produto."


class Produto():
    def __init__(self, nome, preco, estoque, categoria): #lado n recebe categoria
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque
        self.categoria = categoria
        self.__avaliacoes = []
        
    def _validar_preco(self, preco):
        if (preco > 0):
            return True
        else:
            return False
        
    def alterar_preco(self, novo_preco):
        try:
            if not self._validar_preco(novo_preco):
                raise ValueError("Preço inválido. Deve ser maior que 1 e menor que 5.")
            self.__preco = novo_preco
            return True
        except ValueError as e:
            print("Erro ao alterar o preço: ", e)
            return False
    
    #versão que eu tinha feito, para comparação
    #def alterar_preco(self, novo_preco):
        try:
            novo_preco = float(novo_preco)
            if (novo_preco > 0):
                self.preco = novo_preco
                print("Preço alterado com sucesso.")
            else:
                print("Valor inválido. Tente novamente.")
        except ValueError:
            print("Por favor, digite apenas números.")

    
    def alterar_preco(self, novo_preco):
        try:
            if not self._validar_preco(novo_preco):
                raise ValueError("Preço inválido. Deve ser maior que 1 e menor que 5.")
            self.__preco = novo_preco
            return True
        except ValueError as e:
            print("Erro ao alterar o preço: ", e)
            return False
    
    def vender(self, qtd):
        try:
            qtd = float(qtd)
            if (qtd > 0) and (qtd % 1 == 0):
                self.__estoque = self.__estoque - qtd
                return f"Vendido com sucesso."
            else:
                return f"Valor inválido. O valor deve ser maior que zero e inteiro."
        except ValueError:
            return f"Por favor, digite apenas números."
    
    def reabastecer(self, qtd):
        try:
            qtd = float(qtd)
            if (qtd > 0) and (qtd % 1 == 0):
                self.__estoque = self.__estoque + qtd
                return f"Reabastecido com sucesso."
            else:
                return f"Valor inválido. O valor deve ser maior que zero e um número inteiro."
        except ValueError:
            return f"Por favor, digite apenas números."
    
    
    def adicionar_avaliacao(self, cliente, comentario, nota):
        if nota >= 1 and nota <= 5:
            self.__avaliacoes.append(Avaliacoes(cliente, comentario, nota))
            return f"Avaliado com sucesso!"
        else:
            return f"Nota inválida."
    
    def __str__(self):
        return f"O produto '{self.__nome}', da categoria {self.categoria}, custa R${self.__preco} reais e atualmente há {int(self.__estoque)} dele no estoque da loja."
    
    # imprime o produto com seus atributos e suas avaliações
    def exibir_detalhes(self):
        #print(self) #imprime o str do produto
        print(self.__nome)
        for av in self.__avaliacoes:
            print(" - ", av)

    
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

print("Adicionando produto: ", loja.adicionar_produto(prod1))
print("Adicionando produto: ", loja.adicionar_produto(prod2))

print("\nVendendo produto: ", prod2.vender(2))
print("Reabastecendo produto: ", prod1.reabastecer(30))

print("\nAdicionando avaliação: ", prod1.adicionar_avaliacao("Julia", "A câmera não mostra a lua direitinho como prometeu", 3))
print("Adicionando avaliação: ", prod2.adicionar_avaliacao("Mariana", "Não deu certo >:(", 1))
print("\nExibindo detalhes: ") 
prod1.exibir_detalhes()

print("\n")
loja.listar_estoque()

#se na função o 'return' é com print, não imprimir de novo na saída/nos testes, pois ficará bugado. Basta usar a função na sintaxe objeto.função().
