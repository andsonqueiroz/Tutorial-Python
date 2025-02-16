class Pessoa:       #O nome da classe
    def __init__(self, nome):   #__init__ é o famoso CONSTRUTOR, "self" refere-se a classe atual, e "nome" é o atributo
        self.nome = nome    #O atributo nome recebe o dado por parâmetro do construtor
        
# Já fora da classe:

def imprimirNome(Pessoa):       #função para imprimir o nome da pessoa, passando por parametro a CLASSE "Pessoa"
    print(f"O seu nome é {Pessoa.nome}.")       #Um print com texto formatado, juntando o texto com a string "Pessoa.nome" da classe Pessoa

def receberNome():      #função para receber o nome do usuário, que retorna a variável "nome"
    nome = input("Digite o seu nome: ")     #O input, com o texto informando o usuário para digitar o nome (Colocando o texto dentro dos parênteses do INPUT se livra de colocar um print com o texto)
    return nome     #a função retorna a variável "nome", que está armazenando o dado que o usuário digitou

nome = receberNome()    #variável armazenando o nome do usuário digitado

pessoa1 = Pessoa(nome)      #criando objeto "pessoa1", passando por parâmetro (preenchendo o atributo NOME da classe) o "nome", que está armazenando o nome inserido pelo usuário

imprimirNome(pessoa1)       #chamando método para imprimir o nome do usuário
