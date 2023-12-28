fa = float(input("Temperatura em Fahrenheit: ").strip().replace(",", "."))

c = 5 * ((fa - 32) / 9)

print(f"A temperatura de \033[33;1;33m{fa}\033[0;0m graus Fahrenheit convertida para Celsius é \033[33;1;33m{c:.2f}° C\033[0;0m")
