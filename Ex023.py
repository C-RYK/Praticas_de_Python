rep = 0
soma = 0

esc = int(input("Quantas notas quer dígitar para o aluno ?: ").strip())

while rep != esc:
   
    nota = float(input(f"Dígite a {rep+1}° nota desse aluno: ").strip())
    print(" ")

    if nota > 10 or nota < 0:
        print("Nota \033[31mINVALIDA\033[m, dígite uma nota entre 0 e 10")
        print(" ")
    
    else:
        rep += 1

        soma = nota + soma

media = soma / esc

print(f"Media: {media:.2f}")
print(" ")

if media >= 7 and media < 10:
    print("Aluno \033[32mAPROVADO\033[m")

elif media < 7:
    print("Aluno \033[31mREPROVADO\033[m")

else:
    print("Aluno \033[32mAPROVADO COM DISTINÇÃO\033[m")
