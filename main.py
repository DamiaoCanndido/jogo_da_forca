import random

cabeca =  ' '#'O'
corpo = ' '#'|'
braco_esq = ' '#'/'
braco_dir = ' '#'\\'
perna_esq = ' '#'/'
perna_dir = ' '#'\\'

forca = f"########\n##     |\n##     {cabeca}\n##    {braco_esq}{corpo}{braco_dir}\n##     {corpo}\n##    {perna_esq} {perna_dir}\n##"

vidas = 6

pecados = ['soberba', 'avareza', 'inveja', 'ira', 'luxuria', 'gula', 'preguica']


def sorteio(lista: list[str]):
    palavra = random.choice(lista)
    return palavra


def jogar():
    global vidas
    palavra = sorteio(pecados)
    print(palavra)
    while vidas != 0:
        letra = input('Insira uma letra: ')
        jogada = letra in palavra
        if not jogada:
            vidas = vidas - 1
            print("ERROU!")
            print(vidas)
        elif jogada:
            print("ACERTOU!")   


print(forca)
jogar()