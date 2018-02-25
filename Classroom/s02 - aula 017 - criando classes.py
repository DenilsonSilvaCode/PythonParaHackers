class Pessoa: #definindo a classe

    def __init__(self, nome, id): #definindo atributos TODA FUNÇÃO/METODO DEVE SEMPRE INICIAR POR SELF

        self.nome = nome
        self.id = id

    def getNome(self):    #Metodo para retornar o nome
        return self.nome

    def getId(self): #metodo que retorna id
        return self.id


    #Criando instancias da classe / Objetos

    p1 = Pessoa('Marcos' , 1)

    print(p1.getNome())



