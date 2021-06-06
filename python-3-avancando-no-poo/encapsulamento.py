# REVISÃO: Quando criamos atributos no inicializador, estamos definindo quais serão as características do objeto sendo definido.

class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao 
        self.__likes =  0

# o property permite o retorno do atributo likes que está dentro da função dar_like
# criado ao inves do get_algumacoisa, para evitar quebrar o código que já está usando 
# uma maneira de acessar o atributo. 
# usar property é uma ótima prática. Quando criamos getters e setters todos os lugares que já acessam a classe precisam mudar.
    @property
    def likes(self):
        return self.__likes

    def dar_like(self):  
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome
    
    # permite deixar o atributo livre para ser alterado
    @nome.setter
    def nome(self, novo_nome):
        self.nome = novo_nome.title()

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas 
        self.likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome
    
    @nome.deleter
    def nome(self, novo_nome):
        self.nome = novo_nome.title()



vingadores = Filme('Vingadores', 2018, 160)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
print(f'Nome:{vingadores.nome} - Ano: {vingadores.ano}'
     f'Duração: {vingadores.duracao} - Likes: {vingadores.likes}')
     


atlanta = Serie('atlanta', 2018, 2)
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}')




