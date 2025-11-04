def fatorial(num):
    resultado = 1
    while num >= 1:
        resultado *= num
        num -= 1
    return resultado

resp = "sim"

while resp == "sim":
    soma = 0
    i = 1
    while i <= 5:
        valor = int(input(f"Digite o número {i}: "))
        soma += fatorial(valor)
        i += 1

    print(f"O fatorial dos números lidos é {soma}")
    resp = input("Continuar? (sim/não): ")