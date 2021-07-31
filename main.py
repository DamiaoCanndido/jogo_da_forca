import random

cabeca =  ' '#'O'
corpo = ' '#'|'
braco_esq = ' '#'/'
braco_dir = ' '#'\\'
perna_esq = ' '#'/'
perna_dir = ' '#'\\'

corpo_comp = ['O', '|', '/', '\\', '/', '\\']
corpo_inc = [' ', ' ', ' ', ' ', ' ', ' ']

forca = f"########\n##     |\n##     {cabeca}\n##    {braco_esq}{corpo}{braco_dir}\n##     {corpo}\n##    {perna_esq} {perna_dir}\n##"

vidas = 6

pecados = ['soberba', 'avareza', 'inveja', 'ira', 'luxuria', 'gula', 'preguica']


def sorteio(lista: list[str]):
    palavra = random.choice(lista)
    return palavra


def jogar():
    global vidas
    palavra = sorteio(pecados)
    acertos = len(palavra)
    print(palavra)
    while vidas > 0:
        letra = input('Insira uma letra: ')
        jogada = letra in palavra
        if not jogada:
            vidas = vidas - 1
            helper = 5 - vidas
            
            print("ERROU!")
            print(f"Vidas: {vidas}")
            if vidas == 0:
                print("VOCÊ PERDEU!")
            print(forca)
        elif jogada:
            print("ACERTOU!")
            nova = palavra.replace(letra, '')
            palavra = nova
            acertos = len(palavra)
            if acertos == 0:
                vidas = 0
                print("VOCÊ GANHOU!")
            print(f"ACERTOS: {acertos}")
            print(palavra)
            print(forca)

print(forca)
jogar()