class ContaBancaria:    #criação da classe
    def __init__(self, titular, saldo):    #__init__ é o CONSTRUTOR, onde "(self" se refere ao atributo do objeto atual, e "titular, saldo)" são as variáveis que serão passados por parâmetro da classe.
        self.titular = titular    #Atributo público, setando o dado no atributo passando por parâmetro "titular", que será definido no momento da criação do objeto
        self.__saldo = saldo  # Atributo privado - sempre que o atributo tiver 2 uniderlines __ significa que é privado

    def depositar(self, valor):  #Criação do método "depositar", da classe ContaBancaria. Assim, ao criar um objeto (exemplo conta1 = ContaBancaria("Andson", 500), poderá usar o método "conta1.depositar(500)" para depositar no saldo.
        self.__saldo += valor    #O self sempre será referido ao atributo do objeto atual. O método faz o atributo saldo receber o valor passado por parâmetro, somando com o saldo atual.

    def sacar(self, valor):    #outro método da classe, para sacar o valor do saldo
        if valor <= self.__saldo:  #if para verificar se possui saldo suficiente para efetuar o saque do valor
            self.__saldo -= valor    #efetuar subtração do atributo saldo, subtraindo com o valor passado por parâmetro
        else:    #else para imprimir mensagem caso nao tiver valor suficiente
            print("Saldo insuficiente!")

    def exibir_saldo(self):    #outro método para imprimir saldo da conta, onde não possui parâmetros, apenas o self para se referir que os dados utilizados são do objeto atual (exemplo no Java: this.saldo)
        print(f"Saldo de {self.titular}: R${self.__saldo:.2f}")    #imprime a variável/atributo "titular" e "saldo" do objeto atual

# Já fora da classe ContaBancaria: 
# Criando uma conta bancária
conta = ContaBancaria("Andson", 1000)    #criando um objeto ContaBancaria
conta.depositar(500)    #chamando o método do objeto para depositar valor no saldo, passando por parâmetro o valor
conta.sacar(200)    #chamando método para sacar, passando por parâmetro o valor para subtrair do saldo
conta.exibir_saldo()  # Saída: Saldo de Andson: R$1300.00
