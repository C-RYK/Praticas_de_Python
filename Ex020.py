n1 = float(input("Dígite o primero número: ").strip().replace(",", "."))

if n1 < 0:
    print(f"O valor dígitados é negativo, sendo ele {n1}")

elif n1 == 0:
    print(f"O valor dígitados foi 0, sendo ele considerado um número neutro")

else:
    print(f"O valor dígitados é positivo, sendo ele {n1}")
    