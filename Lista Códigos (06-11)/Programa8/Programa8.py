def sequencia(num):
    n1= 0
    n2= 1
    
    if num >= 1:
        print(n1)
    if num >= 2:
        print(n2)
    
    i = 3
    while i <= num:
        n3 = n1 + n2
        print(n3)
        
        n1 = n2
        n2 = n3
        i += 1
    
r="s"
while (r=="s"):
    n = int(input("Digite o valor de n: "))
    sequencia(n)
    r = input("Continuar? s/n: ")
