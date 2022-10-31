def mainFunc(palavraSecreta,letrasDescobertas,jogador2,dica1,dica2,dica3,jogador1):
    contErro = 0
    contDica = 0
    print('---- JOGO DA FORCA ----')

    for i in range(0, len(palavraSecreta)):
        letrasDescobertas.append('*')
    while True:
        try:
            opcao = int(input('\n[1] JOGAR\n[2] DICA\nOpção: '))
        except:
            print("Valor inválido")

        if opcao == 2:
            contDica = contDica + 1
            if contDica == 1:
                print('Dica 1:',dica1)
            elif contDica == 2:
                print('Dica 2:', dica2)
            elif contDica == 3:
                print('Dica 3:',dica3)
            else:
                print("Não há mais dicas restantes.")
            opcao = 1

        if opcao == 1:
            letra = str(input('\nDigite uma letra: ')).lower().strip()

            for i in range(0,len(palavraSecreta)): #percore as letras da palavra
                if letra == palavraSecreta[i]: #verifica se a letra escolhida está em algúm indice
                    letrasDescobertas[i] = letra #substitui o valor do indice
                print(letrasDescobertas[i], end=' ') #end para que os caracteres estejam na mesma linha

            if letra not in palavraSecreta:
                contErro += 1
                print("\nERRO: Você já errou", contErro,'vez')
            
            if contErro == 5:
                historico = open('historico','a') # a = append (Fim da linha)
                historico.write(f'\nPalavra: {palavraSecreta}, Jogador 1: {jogador1} e jogador 2: {jogador2}')
                historico.close()
                print('\nVocê Perdeu!') 
                break

            if '*' not in letrasDescobertas:
                historico = open('historico','a') # a = append (Fim da linha)
                historico.write(f'\nPalavra: {palavraSecreta}, Jogador 1: {jogador1} e jogador 2: {jogador2}')
                historico.close()
                print('\nParabéns, você venceu!')
                break
    