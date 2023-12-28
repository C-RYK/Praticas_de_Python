from math import pi

print("")
num1 = float(input("Dígite o valor da base do quadrado: ").strip())
num2 = float(input("Dígite o valor da altura do quadrado: ").strip())
print("")

while True:

    print("Os valores dígitados estão em:")
    print("")

    print("[1] - Metros", "\n[2] - Centímetros", "\n[3] - Milímetros")
    print("")

    esc = int(input(": ").strip())
    print("")

    if esc == 1:
        cal = (num1 * num2) * 2

        print(f"O dobro do valor da área do quadrado é {cal:.1f} M²\n")
        break

    elif esc == 2:
        cal = (num1 * num2) * 2

        print(f"O dobro do valor da área do quadrado é {cal:.1f} Cm²\n")
        break

    elif esc == 3:
        cal = (num1 * num2) * 2

        print(f"O dobro do valor da área do quadrado é {cal:.1f} MM²\n")
        break

    else:
        print("Escolha invalida. Escolha uma das opções de 1 a 3.\n")
