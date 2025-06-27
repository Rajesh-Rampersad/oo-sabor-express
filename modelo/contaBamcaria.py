# class ContaBancaria:
#     """
#     Classe que representa uma conta bancária.
#     """
#     def __init__(self, titular, saldo_inicial=0):
#         """
#         Inicializa uma nova conta bancária.
#         """
#         self.titular = titular
#         self.saldo = saldo_inicial
#         self.ativo = False
        
#     def __str__(self):
#         """
#         Retorna uma representação em string da conta bancária.
#         """
#         return f"Conta Bancária de {self.titular} | Saldo: R${self.saldo} "
    
#     def ativar_conta(self):
#         """
#         Ativa a conta bancária.
#         """
#         self.ativo = True
#         print(f"Conta de {self.titular} ativada com sucesso!")

# #exemplo de uso
# if __name__ == "__main__":
#     conta1 = ContaBancaria("João", 1000)
#     conta2 = ContaBancaria("Maria", 500)

#     print(conta1)
#     print(conta2)

#     conta1.ativar_conta()
#     conta2.ativar_conta()


#Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
# A classe já está utilizando uma abordagem pythonica, mas podemos adicionar propriedades para os atributos `titular` e `saldo`.
# Além disso, podemos adicionar métodos para depositar e sacar dinheiro da conta. Aqui está a versão refatorada:

class ContaBancaria:
    """
    Classe que representa uma conta bancária.
    """
    def __init__(self, titular, saldo_inicial=0):
        """
        Inicializa uma nova conta bancária.
        """
        self._titular = titular
        self._saldo = saldo_inicial
        self.ativo = False

    def __str__(self):
        """
        Retorna uma representação em string da conta bancária.
        """
        return f"Conta Bancária de {self._titular} | Saldo: R${self._saldo} | {'Ativa' if self.ativo else 'Inativa'}"

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        self._saldo += valor
        print(f"Depósito de R${valor} realizado com sucesso.")

    def sacar(self, valor):
        if valor > self._saldo:
            print("Saldo insuficiente.")
        else:
            self._saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")

    def extrato(self):
        print(f"Titular: {self._titular}")
        print(f"Saldo: R${self._saldo}")
    def ativar_conta(self):
        """Ativa a conta bancária.
        """
        self.ativo = True
        print(f"Conta de {self._titular} ativada com sucesso!")

    def desativar_conta(self):
        """
        Desativa a conta bancária.
        """
        self.ativo = False
        print(f"Conta de {self._titular} desativada com sucesso!")
# Exemplo de uso
if __name__ == "__main__":
    conta1 = ContaBancaria("João", 1000)
    conta2 = ContaBancaria("Maria", 500)

    print(conta1)
    print(conta2)

    conta1.ativar_conta()
    conta2.ativar_conta()

    conta1.depositar(200)
    conta1.sacar(150)
    conta1.extrato()

    conta2.depositar(300)
    conta2.sacar(600)  # Tentativa de saque com saldo insuficiente
    conta2.extrato()