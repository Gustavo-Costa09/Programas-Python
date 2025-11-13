def ehprimo(n):
    if n < 1: 
        return None
    if n == 1:
        return False
    i = 2
    while i <= int(n**0.5):
        if n % i == 0:
            return False
        i += 1
    return True

r = "s"
while r == "s":
    
    num = int(input("Número: "))
    resultado = ehprimo(num)
    if resultado is None:
        print("Número inválido")
    elif resultado:
        print("É primo")
    else:
        print("Não é primo")
    
    r = input("Deseja continuar? s/n: ")