altura = float(input("Dígite sua altura e veja seu peso ideal: ").strip().replace(",", "."))

print("Qual é seu sexo ?")

print("[1] - Masculino")

print("[2] - Feminino")

sexo = str(input(": ").strip().upper())

if sexo == "1" or sexo == "MASCULINO":
    
    cal = (72.7 * altura) - 58

    print(f"Seu peso ideal levando em conta sua altura é de {cal:.2f} Kg")

elif sexo == "2" or sexo == "FEMININO":

    cal = (62.1 * altura) - 44.7    

    print(f"Seu peso ideal levando em conta sua altura é de {cal:.2f} Kg")
    