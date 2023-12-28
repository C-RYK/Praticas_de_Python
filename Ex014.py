peso = float(input("Peso da pesca do dia: ").strip().replace(",", "."))

if peso > 50:

    excesso = peso - 50

    multa = excesso * 4

    print(f"O excesso de peso da pesca é de {excesso:.2f} Kg")

    print(f"O valor da multa por conta do peso excedente é de R$ {multa:.2f}")

else:

    print(f"O peso da pesca não excede o limite de peso")
