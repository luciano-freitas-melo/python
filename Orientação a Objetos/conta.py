class ContaBancaria:
    moeda = "reais"  # colocar a moeda no plural

    def __init__(self, numero, titular, saldo, limite=1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O saldo de {} é de {} {}.".format(self.__titular, self.__saldo, self.moeda))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_total_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_total_disponivel

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("Saldo Insuficiente!")

    def transfere(self, valor, conta_destino):
        if self.__pode_sacar(valor):
            self.saca(valor)
            conta_destino.deposita(valor)
            print("Tranferência de {} {} realizada com êxito!".format(valor, self.moeda))
        else:
            print("Transferência não efetuada: Saldo Insuficiente!")
