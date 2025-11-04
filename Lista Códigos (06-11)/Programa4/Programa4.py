def ehprimo(num):
    if num<2:
        return False
        
    else: 
        i=2
        while i<num:
            if num % i == 0:
                return False
            i += 1
        return True

r="s"        
while (r=="s"):
    n = int(input("Digite um número: "))
    
    i=n+1
    while True:
        if ehprimo(i):
            menor_primo = i
            print(f"O menor número primo maior que N é: {menor_primo}")
            break
        i = i+1
    
    i=n-1
    while i>1:
        if ehprimo(i):
            maior_primo = i
            print(f"O maior número primo menor que N é: {maior_primo}")
            break
        i = i-1
    r = input("Continuar? s/n")
