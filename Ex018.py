n1 = float(input("Dígite o primero número: ").strip().replace(",", "."))

n2 = float(input("Dígite o segundo número: ").strip().replace(",", "."))

if n1 > n2:
    print(f"Os números dígitados foram {n1} e {n2}, {n1} é maior que {n2}")

elif n1 == n2:
    print(f"Os números dígitados foram {n1} e {n2}, ambos são iguais")

else:
    print(f"Os números dígitados foram {n2} e {n1}, {n2} é maior que {n1}")
