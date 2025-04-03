import random


# Jogo de adivinhação

# Tela inicial
print('-----------------------------------------------------------------------------------------------------')
print('-------------------------------------- Seja bem-vindo ao jogo!!! -------------------------------------')
print('-----------------------------------------------------------------------------------------------------')
print('Você deverá achar o número de 4 casas. Para isso, terá 10 tentativas (o número está entre 1000 e 9999).')
print('A partir da 5ª tentativa, você receberá dicas.')

# Começo do jogo
comecar = int(input('Se você quer começar, digite 1: '))
if comecar == 1:
    print('O jogo começou, se prepare!')
    
    numero = random.randint(1000, 9999)  # Gerar número aleatório
    contagem_tentativa = 0  # Contador de tentativas
    
    while contagem_tentativa < 10:
        tentativa = int(input(f'Tentativa {contagem_tentativa + 1} - Digite um número: '))
        
        # Verificar se a tentativa é válida (tem 4 dígitos)
        if tentativa < 1000 or tentativa > 9999:
            print('Por favor, digite um número entre 1000 e 9999.')
            continue
        
        contagem_tentativa += 1  # Atualiza a contagem de tentativas

        # Converter números em listas de dígitos
        numero_secreto = [int(d) for d in str(numero)]
        tentativa_lista = [int(d) for d in str(tentativa)]

        # Mostrar os acertos
        resultado = ''
        for i in range(4):
            if tentativa_lista[i] == numero_secreto[i]:
                resultado += str(tentativa_lista[i])
            else:
                resultado += '-'
        print(f'Número: {resultado}')
        
        # Verificar se o jogador acertou
        if tentativa == numero:
            print(f'Parabéns! Você acertou! O número era {numero} e você precisou de {contagem_tentativa} tentativas.')
            break

        # Dar dicas a partir da 5ª tentativa
        if contagem_tentativa >= 5:
            posicao_dica = random.randint(0, 3)  # Escolher uma posição aleatória
            dica = numero_secreto[posicao_dica]

            # Escolher qual dica dar
            qual_dica = random.choice(['maior5', 'par_impar'])

            if qual_dica == 'maior5':
                if dica > 5:
                    print(f'Dica: O número na posição {posicao_dica + 1} é maior que 5.')
                else:
                    print(f'Dica: O número na posição {posicao_dica + 1} é menor ou igual a 5.')
            else:
                if dica % 2 == 0:
                    print(f'Dica: O número na posição {posicao_dica + 1} é par.')
                else:
                    print(f'Dica: O número na posição {posicao_dica + 1} é ímpar.')

    else:
        print(f'Você não conseguiu acertar. O número era: {numero}')
else:
    print('Você não iniciou o jogo.')