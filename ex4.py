class ContaBancaria():
    def __init__(self, __saldo, __titular):
        self.__saldo = __saldo
        self.__titular = __titular
    
    def depositar(self, valor):
        self.saldo = self.saldo + valor
        return self.saldo
  
    def sacar(self, valor):
        if (self.saldo > valor):
            self.saldo = self.saldo + valor
            return self.saldo
        else:
            mensagem = "Saldo insuficiente."
            return mensagem

    def exibirSaldo(self):
        return self.saldo

    