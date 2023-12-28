lista = []

for cont in range(3):
    num = float(input(f"Dígite o {cont+1}° número: ").strip())

    lista.append(num)

print(f"O maior valor dígitado é {max(lista)}")

print(f"O menor valor dígitado é {min(lista)}")
