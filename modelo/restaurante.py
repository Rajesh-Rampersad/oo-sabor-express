from modelo.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, endereco, telefone=None):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._endereco = endereco
        self._telefone = telefone
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self._nome} - {self._categoria} - {self._endereco} - {self._telefone} - Avaliações: {self.media_avaliacoes}"

    @property
    def nome(self):
        return self._nome

    @property
    def categoria(self):
        return self._categoria

    @property
    def endereco(self):
        return self._endereco

    @property
    def telefone(self):
        return self._telefone

    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Endereço'.ljust(25)} | {'Telefone'.ljust(25)} | {'Avaliações'.ljust(25)} | {'Status'}")
        for restaurante in cls.restaurantes:
            print(
                f"{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.endereco.ljust(25)} | {str(restaurante.telefone).ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}")

    @property
    def ativo(self):
        return '✗' if self._ativo else '✓'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
        
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
        
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        total = sum(avaliacao.nota for avaliacao in self._avaliacao)
        quantidade_de_nota = len(self._avaliacao)
        media = total / quantidade_de_nota
        return round(media, 1)