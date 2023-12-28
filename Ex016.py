print("Calculo para ver quantidade de tinta por M²".center(150))

metragem = float(input("M² da área pintada: ").strip().replace(",", ""))

litros = metragem / 3

if litros > 18:
    print("Você precisara de mais de uma lata de tinta, levando em consideração que cada lata custa R$ 80,00")

else:
    print("Você precisara de uma lata de tinta, levando em consideração que a lata custa R$ 80,00")
