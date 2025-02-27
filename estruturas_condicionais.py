MAIOR_IDADE = 18

idade = int(input("Informe sua idade: "))

if idade >= 18:
    print("Maior, pode tirar a CNH")
else:
    print("Menor não permitido")
    
resp = "Pode" if idade > 18 else "Não pode" 

print(f"{resp} tirar a carteira")