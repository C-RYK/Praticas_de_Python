from math import pi

print("")
num = float(input("Dígite o valor do raio do circulo: ").strip())
print("")

while True:

    print("Os valores dígitados estão em:")
    print("")

    print("[1] - Metros", "\n[2] - Centímetros", "\n[3] - Milímetros")
    print("")

    esc = int(input(": ").strip())
    print("")

    if esc == 1:
        cal = pow(num, 2) * pi

        print(f"A área do circulo é {cal:.1f} M²\n")
        break

    elif esc == 2:
        cal = pow(num, 2) * pi

        print(f"A área do circulo é {cal:.1f} Cm²\n")
        break

    elif esc == 3:
        cal = pow(num, 2) * pi

        print(f"A área do circulo é {cal:.1f} MM²\n")
        break

    else:
        print("Escolha invalida. Escolha uma das opções de 1 a 3.\n")
