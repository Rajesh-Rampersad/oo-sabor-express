class Cliente:
    clientes = []

    def __init__(self, nome, idade, email, telefone=None):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        Cliente.clientes.append(self)

    def __str__(self):
        return f"{self.nome} - {self.idade} anos - {self.email} - {self.telefone if self.telefone else 'Sem telefone'}"

    @classmethod
    def listar_clientes(cls):
        for cliente in cls.clientes:
            print(f"{cliente.nome} - {cliente.idade} anos - {cliente.email} - {cliente.telefone if cliente.telefone else 'Sem telefone'}")


# Instantiate some Cliente objects
cliente1 = Cliente("Alice", 30, "exemplo1@test.com", "1234-5678")
cliente2 = Cliente("Bob", 25, "exemplo2@test.com", "9876-5432")
cliente3 = Cliente("Charlie", 35, "exemplo3@test.com", "5555-5555")

Cliente.listar_clientes()
