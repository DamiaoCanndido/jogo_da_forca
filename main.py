import random

quadro = ''

corpo_comp = ['O', '|', '/', '\\', '/', '\\']
corpo_inc = [' ', ' ', ' ', ' ', ' ', ' ']

forca = f"########\n##     |\n##     {corpo_inc[0]}\n##    {corpo_inc[2]}{corpo_inc[1]}{corpo_inc[3]}\n##     {corpo_inc[1]}\n##    {corpo_inc[4]} {corpo_inc[5]}\n##"

vidas = 6

pecados = ['soberba', 'avareza', 'inveja', 'ira', 'luxuria', 'gula', 'preguica']


def sorteio(lista: list[str]):
    palavra = random.choice(lista)
    return palavra


def criaQuadro(palavra_original: str):
    global quadro
    for i in palavra_original:
        quadro = quadro + '_'
    

def colocarLetras(palavra_original: str, letra: str):
    global quadro
    res = [i for i in range(len(palavra_original)) if palavra_original.startswith(letra, i)]
    for i in res:
        quadro = quadro[:i] + letra + quadro[i+1:]
        


def jogar():
    global vidas
    global forca
    palavra = sorteio(pecados)
    palavra_original = palavra
    criaQuadro(palavra_original)
    print(f"{quadro} - letras: {len(palavra_original)}")
    acertos = len(palavra)
    while vidas > 0:
        letra = input('Insira uma letra: ')
        jogada = letra in palavra
        if not jogada:
            vidas = vidas - 1
            helper = 5 - vidas
            corpo_inc[helper] = corpo_comp[helper]
            forca = f"########\n##     |\n##     {corpo_inc[0]}\n##    {corpo_inc[2]}{corpo_inc[1]}{corpo_inc[3]}\n##     {corpo_inc[1]}\n##    {corpo_inc[4]} {corpo_inc[5]}\n##"
            print("ERROU!")
            print(f"{quadro} - letras: {len(palavra_original)}")
            print(f"Vidas: {vidas}")
            if vidas == 0:
                print("VOCÊ PERDEU!")
            print(forca)
        elif jogada:
            print("ACERTOU!")
            colocarLetras(palavra_original, letra)
            nova = palavra.replace(letra, '')
            palavra = nova
            acertos = len(palavra)
            if acertos == 0:
                vidas = 0
                print("VOCÊ GANHOU!")
            print("===================================================================")
            print(f"{quadro} - letras: {len(palavra_original)}")
            print("===================================================================")
            print(forca)

print(forca)
jogar()