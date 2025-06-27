# app.py
from modelo.restaurante import Restaurante

restaurante1 = Restaurante("Pizzaria do João", "Pizzaria", "Rua das Flores, 123", "1234-5678")
# restaurante2 = Restaurante("Churrascaria do Zé", "Churrascaria", "Avenida Brasil, 456", "9876-5432")
# restaurante3 = Restaurante("Sushi do Carlos", "Sushi", "Rua do Peixe, 789", "5555-5555")
# restaurante4 = Restaurante("Café da Manhã", "Cafeteria", "Praça Central, 101", "1111-2222")

restaurante1.alternar_estado()
restaurante1.receber_avaliacao("Maria", 5)
restaurante1.receber_avaliacao("João", 4)
restaurante1.receber_avaliacao("Ana", 3)
# restaurante3.alternar_estado()

def __main__():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    __main__()