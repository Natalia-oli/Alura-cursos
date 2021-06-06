# REVISÃO: Quando criamos atributos no inicializador, estamos definindo quais serão as características do objeto sendo definido.
class Programa: 
    def __init__(self, nome, ano):
        self._nome = nome.title()  #_Programa__nome
        self.ano = ano
        self._likes =  0

# _atributo, por convenção, mostra que é algo protegido
#melhor usar um _ só, para indicar que é uma variavel privada
# __ apresnta erros na hora de fazer herança, por isso, é ideal usar o _ 

    @property
    def likes(self):
        return self._likes

    def dar_like(self):  
        self._likes += 1

    @property
    def nome(self):
        return self._nome
    
    # permite deixar o atributo livre para ser alterado
    @nome.setter
    def nome(self, novo_nome):
        self.nome = novo_nome.title()

class Filme(Programa):
    # para evitar repetção de código (dos atributos que já estão na classe mae, é so fazer o processo a baixo):
    # deixando apenas o atributo que não é comum as duas classes
    # o 'def __init__(self, nome, ano, duracao)' está sobrescrevendo o init da classe mae, está 'extendendo'
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao 
        

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas 
# antes o código estava repetido nas classes, com o super(), não é mais necessário essa repetição 
        #self._nome = nome.title()
        #self.ano = ano
        #self._likes = 0

# siper(). chama qualquer metodo/atributos da classse mãe(Programa)

vingadores = Filme('Vingadores', 2018, 160)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
print(f'{vingadores.nome} - {vingadores.ano}'
     f'{vingadores.duracao} - {vingadores.likes}')
     
atlanta = Serie('atlanta', 2018, 2)
print(f'{atlanta.nome} - {atlanta.ano} - {atlanta.temporadas}' )




