print("Calculo de Salario/Descontos".center(160))

salarioHora = float(input("Ganho por hora: ").strip().replace(",", "."))

horasTrabalhadas = int(input("Horas trabalhadas no mês: ").strip())

salario = salarioHora * horasTrabalhadas

ir = salario * 0.11

inss = salario * 0.08

sindicato = salario * 0.05

print("")
print(f"Salário bruto: R$ {salario:.2f}")
print("")

print(f"Desconto do IR (Imposto de renda): R$ {ir:.2f}")
print(f"Desconto do INSS: R$ {inss:.2f}")
print(f"Desconto do Sindicato: R$ {sindicato:.2f}")

print("")
print(f"Salário liquido: R$ {salario - (ir + inss + sindicato):.2f}")
print("")
