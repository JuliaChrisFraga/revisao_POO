class ContaBancaria():
    def __init__(self, __saldo, __titular):
        self.__saldo = __saldo
        self.__titular = __titular
    
    def depositar(self, valor):
        self.__saldo = self.__saldo + valor
        return self.__saldo
  
    def sacar(self, valor):
        if (self.__saldo > valor):
            self.__saldo = self.__saldo - valor
            return self.__saldo
        else:
            mensagem = "Saldo insuficiente."
            return mensagem
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @saldo.setter
    def saldo(self, valor):
        try:
            valor = float(valor)
            if (valor >= 0):
                self.__saldo = valor
            else:
                print("Valor inválido. O saldo não pode ser negativo.")
        except ValueError:
            print("Valor inválido. Insira um número válido.")
    
    @titular.setter
    def titular(self, new):
        if not new:
            print("Não é permitido nomes vazios. tente novamente.")
        else:
            self.__titular = new

p1 = ContaBancaria(2000, "zaoba")

print("Exibindo o titular:", p1.titular, "\n") #se não tivesse o property, seria p1.exibirTitular()
print("Exibindo o saldo atual:", p1.saldo) #se não tivesse o property, seria p1.exibirSaldo()
print("Depositando 200:", p1.depositar(200))
print("Sacando 100:", p1.sacar(100))

p1.saldo = "abc" #sem o setter, chamaria-se a função e passaria-se como parâmetro o Valor. Also, o setter tem que ter o mesmo nome do seu respectivo get
p1.saldo = "400"
print("Saldo depois de alterado: ", p1.saldo, "\n")

p1.titular = ""
p1.titular = "amaba"
print("Titular depois de alterado: ", p1.titular)

    