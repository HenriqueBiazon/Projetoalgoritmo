import random

# Jogo de adivinhação

# Tela inicial
print('------------------------------------------------------------------------------------------------------')
print('------------------------------------- Seja bem-vindo ao jogo!!!! -------------------------------------')
print('------------------------------------------------------------------------------------------------------')
print('Você deverá achar o número de 4 dígitos. Para isso terá 10 tentativas (o número está entre 1000 e 9999)')
print('A partir da 5ª tentativa você receberá dicas.')




# Começo do jogo
comecar = int(input('Se você quer começar, digite 1: '))




if comecar == 1:
    print('O jogo começou, se prepare!')
    numero = random.randint(1000, 9999)   # Gerar número aleatório
    contagem_tentativa = 0
    acertou = False

    
    
    
    
    while contagem_tentativa < 10:
        tentativa = int(input(f'Tentativa {contagem_tentativa + 1} - Digite sua tentativa para acertar o número: '))

       
       
       
        # Verificar se a tentativa é válida (tem 4 dígitos)
        if tentativa < 1000 or tentativa > 9999:
            print('Por favor, digite um número entre 1000 e 9999.')
            continue  
        contagem_tentativa += 1

        
        
        
        
        # Separar dígitos do número e da tentativa
        n1 = numero // 1000
        n2 = (numero % 1000) // 100
        n3 = (numero % 100) // 10
        n4 = numero % 10

        t1 = tentativa // 1000
        t2 = (tentativa % 1000) // 100
        t3 = (tentativa % 100) // 10
        t4 = tentativa % 10

       
       
       
        # Mostrar os acertos
        print("Número: ", end = '')
        if t1 == n1:
            print(t1, end = '')
        else:
            print('-', end = '')

        if t2 == n2:
            print(t2, end = '')
        else:
            print('-', end = '')

        if t3 == n3:
            print(t3, end='')
        else:
            print('-', end = '')

        if t4 == n4:
            print(t4)
        else:
            print('-')

       
       
       
        # Verificar se acertou
        if tentativa == numero:
            print(f'Parabéns! Você acertou o número {numero} em {contagem_tentativa} tentativas!')
            acertou = True
            break

       
       
       
        # Dar dica a partir da 5ª tentativa
        while n1 != t1 or n2 != t2 or n3 != t3 or n4 != t4:
         if contagem_tentativa >= 5:
            posicao = random.randint(0, 3)

            if posicao == 0:
                digito = n1
            elif posicao == 1:
                digito = n2
            elif posicao == 2:
                digito = n3
            else:
                digito = n4

            qual_dica = random.randint(0, 1)

            if qual_dica == 0:
                if digito > 5:
                    print(f'Dica: o número na posição {posicao + 1} é maior que 5.')
                else:
                    print(f'Dica: o número na posição {posicao + 1} é menor ou igual a 5.')
            else:
                if digito % 2 == 0:
                    print(f'Dica: o número na posição {posicao + 1} é par.')
                else:
                    print(f'Dica: o número na posição {posicao + 1} é ímpar.')

    
    
    
    if not acertou:
        print(f'Fim de jogo! O número correto era {numero}.')




else:
    print('Você não iniciou o jogo.')