r = "s"

while r == 's':			
			
	lista = list(map(int, input ("Digite os números inteiros separados por espaço: ").split()))
			
	c = int(input("Digite o valor de c: "))
			
	i = 0
			
	while i < len(lista):
		 j = i + 1
		while j < len(lista):
			if lista[i] + lista[j] == c:
				print(f"Resultado: {lista[i]} e {lista[j]}")
				encontrou = True
			    break
			     j += 1
			if encontrou:
			     break
			    i += 1
			    
	if not encontrou:
		print("A combinação de números não existe")
	
	r = input("Deseja continuar (s/n)?: ")
	
		