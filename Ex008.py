print("\033[\033[31;1;47mPAINEL DE INFORMAÇÕES SALARIAIS\033[0;0m".center(210))

salario = float(input("Dígite seu salario: R$ ").strip().replace(",", "."))
print("")

horas = int(input("Horas trabalhadas por dia: ").strip())

print("\033[\033[31;1;47mCARGA HORÁRIA:\033[0;0m".center(210))

print("\n[1] - De Seg. a Sex\n[2] - De Seg. a Sábado\n[3] - 12 por 36\n[4] - 48 por 24\n[5] - Seg. a Seg\n[6] - Sábado e domingo intercalado\n")

esc = int(input(": ").strip())

if esc == 1:
    porDia = (salario / 22)
    porHora = porDia / horas
    HorasTrabalhadasPorMes = horas * 22

    print("")
    print(f"Valor ganho por dia: \033[1;42m{porDia:.2f}\033[0;0m\nValor ganho por hora: \033[1;42m{porHora:.2f}\033[0;0m\nHoras Trabalhadas por mês: \033[1;42m{HorasTrabalhadasPorMes}\033[0;0m\n")

elif esc == 2:
    porDia = (salario / 26)
    porHora = porDia / horas
    HorasTrabalhadasPorMes = horas * 26

    print("")
    print(f"Valor ganho por dia: \033[1;42m{porDia:.2f}\033[0;0m\nValor ganho por hora: \033[1;42m{porHora:.2f}\033[0;0m\nHoras Trabalhadas por mês: \033[1;42m{HorasTrabalhadasPorMes}\033[0;0m\n")

elif esc == 3:
    porDia = (salario / 15)
    porHora = porDia / horas
    HorasTrabalhadasPorMes = horas * 15

    print("")
    print(f"Valor ganho por dia: \033[1;42m{porDia:.2f}\033[0;0m\nValor ganho por hora: \033[1;42m{porHora:.2f}\033[0;0m\nHoras Trabalhadas por mês: \033[1;42m{HorasTrabalhadasPorMes}\033[0;0m\n")

elif esc == 4:
    porDia = (salario / 24)
    porHora = porDia / horas
    HorasTrabalhadasPorMes = horas * 24

    print("")
    print(f"Valor ganho por dia: \033[1;42m{porDia:.2f}\033[0;0m\nValor ganho por hora: \033[1;42m{porHora:.2f}\033[0;0m\nHoras Trabalhadas por mês: \033[1;42m{HorasTrabalhadasPorMes}\033[0;0m\n")

elif esc == 5:
    porDia = (salario / 30)
    porHora = porDia / horas
    HorasTrabalhadasPorMes = horas * 30

    print("")
    print(f"Valor ganho por dia: \033[1;42m{porDia:.2f}\033[0;0m\nValor ganho por hora: \033[1;42m{porHora:.2f}\033[0;0m\nHoras Trabalhadas por mês: \033[1;42m{HorasTrabalhadasPorMes}\033[0;0m\n")

elif esc == 6:
    porDia = (salario / 26)
    porHora = porDia / horas
    HorasTrabalhadasPorMes = horas * 26

    print("")
    print(f"Valor ganho por dia: \033[1;42m{porDia:.2f}\033[0;0m\nValor ganho por hora: \033[1;42m{porHora:.2f}\033[0;0m\nHoras Trabalhadas por mês: \033[1;42m{HorasTrabalhadasPorMes}\033[0;0m\n")
