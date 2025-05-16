
#pesquisar binarias são metodos de pesquisas mais eficiêntes.
#quando comparada as buscas lineares.
#quanto mais itens adicionados na lista, mais rápida ela se torna.


def pesquisa(lista,item):              #definição de onde irei procurar.
    
    #declaração de variáveis.       
    baixo= 0                           #aqui temos o ponto inicial do indice.
    alto= len(lista) -1                #o len vai percorrer a lista .
    tentativas = 0                     #tentativas até acertar.

    while baixo <= alto:               #essa variavel tem como propósito, impedir que as variavéis passem uma pela outra.
        tentativas += 1                #Aqui temos a variável que capturar, quantas tentativas a máquina fez.
        meio = (baixo + alto) //2      #esta variável vai diretamente a metade, fazendo a média entre baixo e alto e dividindo em 2
        chute = lista[meio]            #o chute vai direito ao meio da lista.
    
        if  chute == item:             #mas se o chute for exatamente igual ao item que eu procuro...
        
            return meio,tentativas     #ele vai me retornar o numero acertado, e quantas tentativas a maquina fez.
    
        elif  chute > item:            #e se o chute for maior que o item. 
        
            alto = meio -1             #se eu chutar muito alto ele na proxima tentativa vai excluir tudo que tiver pra frente.
         
        else:                          #Se ele for o muito baixo, ele adiciona mais um, e exclui oque tem para trás. 
    
            baixo = meio +1 

    return None, tentativas            #Se o numero tiver fora, ele mostrará o 'None'.
    

lista = list(range(1, 1001))           # Lista de 1 até 1000 

#não podemos esquecer a lista que vasculharemos.
#abaixo, temos a tentativa chamada try.
#aqui temos um novo laço de repetição, mas aqui, vamos imprimir tudo feito anteriormente.


try:
      
    numero= int(input("Digite o numero de 1 a 1000 : "))          #aqui temos um input para inserir o seu número.
    resultado,tentativas = pesquisa(lista, numero)                #resultado,tentativas,resultam em pesquisa nossa lista e procurar nosso número.

    if resultado is not None:  
                                                                  #is not None, vai ser responsável por garantir que o contéudo não seja None.
                                                                  #O print vai nos mostrar o número, encontrando no indice, mostrando o resultado. 
       print(f"Número{numero} encontrado no índice {resultado} ")
                                                                
       print(f"Foram necessárias {tentativas} tentativas até encontrar.") #Descobriremos aqui o número de tentativas que maquina fez.
    else:
       #printaremos uma spring dentro de duas chaves, para mostrar no terminal.
       print(f"Número {numero} não foi encontrada na lista.")
       
       #printaremos uma spring dentro de duas chaves, para mostrar no terminal.
       
       print(f"A busca fez {tentativas} tentativas até concluir.")
       #printaremos uma spring dentro de duas chaves, para mostrar no terminal.
       
       
#except ValueError vai impedir que você, digite qualquer coisa fora do esperado.
except ValueError:
    
    print("Por favor, digite um número válido.")
#nosso input será mostrado para você não sair dos trilhos.
