r = "s"

while r == 's':

	n1 = int(input ("Digite o número 1"))
	i = 0
	
	while i < n1:
		n2 = 0
		while n2 < i+1:
			print(n2+1, end = " ")
			n2 += 1
		print()
		i += 1
		
	r = input("Deseja continuar (s/n)?: ")
	