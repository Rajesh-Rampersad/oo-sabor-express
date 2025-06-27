class Pessoa:
    def __init__(self, nome, idade,profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Profissão: {self.profissao}"
    
    #metodo de instancia chamado aniversario, que aumente a idade da pessoa em 1 ano
    def aniversario(self):
        self.idade += 1
        print(f"{self.nome} agora tem {self.idade} anos.")
        
    # propiedade chamada saudacao
    @property
    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e sou {self.profissao}."

# Exemplo de uso

# Criando 3 instâncias da classe Pessoa
pessoa1 = Pessoa("João", 30, "Engenheiro")
pessoa2 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa3 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa4 = Pessoa(nome='Jaque', idade=22, profissao='Designer')

#printando as informações de cada pessoa
print("Informações das pessoas:")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print(pessoa4)

pessoa1.aniversario()  # Aumenta a idade de pessoa1 em 1 ano
pessoa2.aniversario()  # Aumenta a idade de pessoa2 em 1 ano
pessoa3.aniversario()  # Aumenta a idade de pessoa3 em 1 ano
pessoa4.aniversario()  # Aumenta a idade de pessoa4 em 1 ano

# Exibindo a saudação de cada pessoa
print("\nSaudações:")
print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)
print(pessoa4.saudacao) 