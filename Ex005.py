esc = " "
cond = 0

while True:

    num = float(input("Dígite o valor em metros: ").strip().replace(",", "."))

    print(f"{num} Metros equivalem a {num * 100} Centimetros")

    print(" ")

    esc = str(input("Quer fazer outra conversão? : ").strip().upper())

    if esc == "NÃO" \
        or esc == "N" \
        or esc == "NAO":

        break

print("Programa encerrado, volte sempre")
