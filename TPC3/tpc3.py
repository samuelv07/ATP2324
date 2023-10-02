
modo=int(input("Selecione o modo de jogo. Quer adivinhar o número inteiro que eu escolho (1), ou quer que eu adivinhe o número inteiro em que está a pensar (2)?"))

if modo == 1:
    import random
    n = random.randrange(1,100)
    tentativas=1
    palpite = int(input("Diga a primeira tentativa."))
    while n!= palpite:
        if palpite < n:
            palpite = int(input("Muito baixo. Diga outro número."))
            tentativas += 1
        elif palpite > n:
            palpite = int(input("Muito alto. Diga outro número."))
            tentativas += 1
    print("Adivinhou em "+str(tentativas)+" tentativas.")

else:
    import random
    minimo = 1
    maximo = 100
    print("Pense num número inteiro de 0 e 100")
    numero = random.randrange(1,100)
    print(numero)
    tentativas = 1
    resultado = 0
    while resultado != 3:
        resultado = int(input("o número é superior(1), inferior (2), ou correto (3)?"))
        if resultado == 2:
            if numero > minimo:
                 minimo = numero + 1
            numero = random.randint(minimo,maximo)
            print(numero)
        if resultado == 1:
            if numero < maximo:
                 maximo = numero - 1
            numero = random.randint(minimo,maximo)
            print(numero)
        tentativas += 1
    print("Consegui acertar em "+str(tentativas)+" tentativas.")