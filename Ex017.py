print("Calculo para ver quantidade de tinta por M²".center(150))

metragem = float(input("M² da área pintada: ").strip().replace(",", ""))

litros = metragem / 3

if litros > 18:
    print("Você precisara de mais de uma lata de tinta, levando em consideração que cada lata de 18 L custa R$ 80,00 e as de 3,6 L custa R$ 25,00")

elif litros >= 15 and litros <= 18:
    print("Você precisara de uma lata de tinta de 18 L, levando em consideração que a lata custa R$ 80,00")

elif litros <= 14:
    print("Você precisara de uma ou mais latas de 3,6 L, levando em consideração que cada lata custa R$ 25,00")
