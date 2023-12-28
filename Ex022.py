letra = str(input("Dígite uma letra e veja se é uma vogal ou consoante: ").strip().upper())

if letra in ["A", "E", "I", "O", "U"]:
    print(f"A letra dígitada é uma vogal, sendo ela a letra {letra}.")

else:
    print(f"A letra dígitada é uma consoante, sendo ela a letra {letra}.")
