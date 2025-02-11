escolha = 0
cont = 0
vetor = []  #Vetor não precisa declarar tamanho, apenas o conteúdo

def menuzinho():    #Definindo função de imprimir menú, todas as funções/métodos devem ser definidas antes de ser chamadas, e é necessário ter "def"
    print("------- Olá, bem vindo ao primeiro sisteminha em PYTHON -------")
    print("1. adicionar elemento")
    print("2. remover elemento")
    print("3. imprimir todos os elementos")
    print("7. Sair")

while escolha != 7:
    menuzinho()     #chamando função de imprimir menú
    escolha = int(input("digite: "))    #Todo INPUT é retornado um valor STRING, sendo assim para receber números precisam ser manualmente declarados

    match escolha:      #O famoso SWITCH CASE
        case 1:
            adicionado = input("\nDigite o elemento para inserir: ")    # O famoso \n, para quebrar linha
            vetor.append(adicionado)        #Os vetores são semelhantes aos ArrayLists do Java, não precisa declarar tamanho, apenas inserir (append) e remover (pop/remove)
            if adicionado in vetor:     #Um IF ELSE, para verificar se o conteúdo da variável "adicionado" está presente no vetor(ou lista, como chamam no Python)
                print("\n-- Adicionado com sucesso! --\n")
            else:
                print("\n-- Erro ao adicionar elemento. Tente novamente --\n")
    
        case 2:
            print("\n---- ELEMENTOS EXISTENTES ----")
            if len(vetor) > 0:      # IF ELSE para verificar se o tamanho do vetor é maior que 0 (se possui elemento ou se está vazio). len(vetor) é útil para mostrar o tamanho de um vetor
                for i in vetor:         #Um FOR para percorrer o vetor (ou lista)
                    print(str(cont) + ". " + i)     # o "i" será o conteúdo de cada posição do vetor, assim pode imprimir o "i" no PRINT() que irá aparecer o conteúdo do vetor
                    cont +=1    # Contador para mostrar a posição de cada elemento do vetor (também poderia utilizar vetor.index(i), que iria mostrar o número da posição do conteúdo "i" do vetor)
                removido = vetor.pop(int(input("Digite o elemento que deseja remover: ")))      # vetor.pop remove e retorna o elemento removido do vetor, assim é possivel armazenar numa variável o elemento removido, e posteriormente imprimir na tela para informar ao usuário
                print("\n-- Elemento removido: " + removido + " --\n")             #também é possível utilizar vetor.remove(), que irá apenas remover o elemento, sem retornar nenhuma informação do que foi removido.
                cont = 0
            else:
                print("\n-- Não há elementos para remover. --\n")
                cont = 0

        case 3:
            if vetor:       #se o vetor tiver elemento, o IF será true (essa forma é mais eficiente para quem só quer saber se o vetor está vazio ou não)
                for i in vetor:
                    print(i)
            else:
                print("\n-- Não há elementos --\n")
        case 7:
            print("\nVolte sempre :)")
                
