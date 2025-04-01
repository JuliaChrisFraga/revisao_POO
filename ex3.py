from datetime import date

class Funcionario():
    def __init__(self, id, sobrenome, nome, nascimento, admissao, salario):
        self.id = id
        self.sobrenome = sobrenome
        self.nome = nome
        self.nascimento = nascimento
        self.admissao = admissao
        self.salario = salario
    
    def idade(self):
        dataAtual = date.today()
        idade = dataAtual.year - self.nascimento[2]
        if ((dataAtual.month, dataAtual.day) < (self.nascimento[1], self.nascimento[0])):
            idade = idade - 1
        else:
            idade = idade - 0
        return idade

    def tempo_de_casa(self):
        dataAtual = date.today()
        tempo = dataAtual.year - self.admissao[2]
        if ((dataAtual.month, dataAtual.day) < (self.admissao[1], self.admissao[0])):
            tempo = tempo - 1
        else:
            tempo = tempo - 0
        return tempo
    
    def aumento_de_salario(self):
        tempo = self.tempo_de_casa()
        if (tempo < 5):
            self.salario = self.salario + self.salario*2/100
        elif (tempo < 10):
            self.salario = self.salario + self.salario*5/100
        else:
            self.salario = self.salario + self.salario*10/100
        return self.salario
    
    def mostrarFuncionario(self):
        idade = self.idade()
        tempo = self.tempo_de_casa()
        mensagem = f"ID: {self.id}, \nNome: {self.nome}; \nSobrenome: {self.sobrenome}; \nIdade: {idade} anos; \nAntiguidade: {tempo} anos; \nSalário: {self.salario} euros."
        return mensagem

p1 = Funcionario(1, "maria", "ze", (21,12,2007), (21,12,2007), 2000)

print("Idade: ", p1.idade())
print("Tempo na empresa: ", p1.tempo_de_casa(), " anos.")
print("Salário inicial: ", p1.salario, "\nSalário aumentado: ", p1.aumento_de_salario())
print("Funcionário info: ", p1.mostrarFuncionario())
