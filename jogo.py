import random

# Jogo de adivinhação

# Tela inicial

print('-----------------------------------------------------------------------------------------------------')
print('--------------------------------------seja bem vindo ao jogo!!!--------------------------------------')
print('-----------------------------------------------------------------------------------------------------')
print('Você deverá achar o número de 4 casas. para isso terá 10 tentativas (o número está entre 1000 e 9999)')
print('À partir da 5a. tentativa você recebera dicas')



# Começo do jogo

comecar = int(input('Se você quer começar digite 1: '))
print('O jogo começou, se prepare')

if comecar == 1:
    numero = random.randint(1000,9999)   # Gerar numero aleatorio
    contagem_tentativa = 0   #  Contador de tentativas
    while contagem_tentativa < 10:
        tentativa = int(input(f'tentativa {contagem_tentativa + 1} - Digite sua tentativa para acertar o número: '))
        contagem_tentativa += 1


        #verificar se a tentativa e valida (tem 4 digitos)

        if tentativa < 1000 or tentativa > 9999: 
            print('Por favor, digite um número entre 1000 e 9999')
            continue


    

        # Converter os números em lista de dígitos para facilitar a comparação

        numero_secreto = [int(d) for d in str(numero)]
        tentativa_lista = [int(d) for d in str(tentativa)]




        #Mostra os acertos

        resultado = ''
        for i in range(4):
            if tentativa_lista[i] == numero_secreto[i]:
               resultado += str(tentativa_lista[i])
            else:
               resultado += '-'
            print(f'Numero: {resultado}')
    


    
    
         # Dar dica a partir da 5a. tentativa

        if tentativa >= 5:
           posicao_dica = random.randint(0,4) #para escolher uma posicao aleatroria
           dica = numero_secreto[posicao_dica]
    



        # Escolher qual dica dar

        qual_dica = random.choice(['maior5', 'par_impar'])

        if qual_dica == 'maior5':
            if dica > 5:
               print(f'Dica: o numero na posicao {posicao_dica} e maior que 5')
            else:
                print(f'Dica: o numero na posicao {posicao_dica} e menor ou igual a 5')
    
        else:
            if dica % 2 == 0:
               print(f'Dica: o numero na posicao {posicao_dica} e par')
            else:
               print(f'Dica: o numero na posicao {posicao_dica} e impar')
    
    


        #ver se o jogador acertou a dica

        if tentativa == numero:
           print(f'Voce acertou, o numero e: {numero} em {tentativa} tentativas')
    
        else:
            print(f'Voce nao conseguiu acertar, o numero era: {numero}')


     # Caso nao iniciar o jogo

    else:
       print('Voce nao iniciou o jogo')
