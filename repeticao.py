palavra = input("Digite uma palavra: ")
vogais = "aeiou"

for letras in palavra:
    if letras in vogais:
        print(letras)