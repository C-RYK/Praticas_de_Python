from math import pow

pr = int(input("Dígite o 1° valor inteiro: ").strip())
se = int(input("Dígite o 2° valor inteiro: ").strip())

real = float(input("Dígite um valor real: ").strip().replace(",", "."))

PrCal = (pr * 2) / se

SeCal = (pr + real) * 3

TerCal = pow(real, 3)


print(f"Produto do dobro do primeiro com metade do segundo: {PrCal:.1f}")

print(f"Soma do triplo do primeiro com o terceiro: {SeCal:.1f}")

print(f"Terceiro elevado ao cubo: {TerCal:.1f}")
