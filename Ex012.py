altura = float(input("Dígite sua altura e veja seu peso ideal: ").strip().replace(",", "."))

pesoIdeal = (72.7*altura) - 58 

print(f"Baseado na sua altura, seu peso ideal é de {pesoIdeal:.2f} Kg")
