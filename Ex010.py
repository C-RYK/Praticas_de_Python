graus = float(input("Dígite o valor dos graus em Celsius para ser convertido em Fahrenheit: ").strip())

if graus == 0:
    print("O° C convertidos em Fahrenheit é 32° F.")

else:
    cal = (graus * (9/5)) + 32

    print(f"{graus:.1f}° C convertidos em Fahrenheit é {cal:.1f}° F")
