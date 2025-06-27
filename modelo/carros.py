class Carros:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f"{self.modelo} - {self.cor} - {self.ano}"

    @classmethod
    def listar_carros(cls, carros):
        for carro in carros:
            print(f"{carro.modelo} - {carro.cor} - {carro.ano}")


# Instantiate some Carros objects
carro1 = Carros("Fusca", "azul", 1970)
carro2 = Carros("Civic", "preto", 2020)
carro3 = Carros("Fusca", "azul", 1970)

# List the cars using the class method
Carros.listar_carros([carro1, carro2, carro3])
