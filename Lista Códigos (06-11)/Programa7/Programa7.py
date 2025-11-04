r = "s"        
while r == "s":
    seq1 = input("Digite a 1ª Sequencia: ")
    
    tam1 = len(seq1)
    tam2 = 0
    
    while tam2 < tam1:
        seq2 = input("Digite a 2ª Sequencia: ")
        tam2 = len(seq2)
        if tam2 < tam1:
            print("A sequencia 2 nao pode ser menor que a sequencia 1")
    
    i = 0
    vezes = 0
    
    while i <= tam2 - tam1:
        if seq2[i : i + tam1] == seq1:
            vezes += 1
        i += 1
            
    print(f"A sequencia 1 se repetiu {vezes} vez(es) na sequencia 2")
    r = input("Continuar? s/n: ")