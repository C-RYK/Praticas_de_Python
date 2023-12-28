lista = []
soma = 0

for n in range(0, 4):
    notas = float(input(f"{n+1}° Nota: ").strip().replace(",", "."))

    lista.append(notas)

for cont in lista:
    soma += cont

print(f"A média desse aluno é {soma/len(lista)}")
