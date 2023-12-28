n1 = str(input("Dígite os valores F (Feminino) ou  M (Masculino): ").strip().upper())

if n1 == "F":
    print(f"{n1} - Feminino.")

elif n1 == "M":
    print(f"{n1} - Masculino.")

else:
    print(f"Sexo inválido, dígite uma letra das opções.")
