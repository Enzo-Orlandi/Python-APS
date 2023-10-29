#(A)const_Gasolina = Litros * 2.27 (kg de CO2)
#(B)const_Etanol = Litros * 1.47 (kg de C02)
#(C)const_Diesel = Litros * 3.15 (kg de CO2)
#(D)const_Gas =  Metros Cubicos * 1.84 (kg de CO2)

escolha = 'a'

while escolha != 'n':

    escolha = input("\nEscolha o combustivél ou ""N"" p/sair: \n (A) Gasolina, (B) Etanol, (C) Diesel ou (D) Gás Natural (GNV) \n")
    escolha = (format(escolha.lower()))
    
    if (escolha == 'a'):
        const = 2.27
    elif (escolha == 'b'): 
        const = 1.47
    elif (escolha == 'c'): 
        const = 3.15
    elif (escolha == 'd'): 
        const = 1.84   
    elif (escolha == 'n'): 
        print("Fim do Programa.") 
        const = 0   
    else:
        print("Código inválido.")
        const = 0   
    
    if const > 0:
        while True:
            try:
                litros = int(input("\nQuantos Km seu veiculo faz com 1 litro de combustivel: "))
                emissaoCarbono =  (const) / float(litros)
                percurso = float(input("\nQuantos Km voce roda por dia? "))

                print(f"\nSeu veiculo libera {emissaoCarbono:.2f}kg de CO² por km")
                print(f"\nSeu percurso libera {(percurso / litros) * (const):.2f}kg de CO² por dia")

                emissaoAnual = ((percurso / litros) * (const)) * 365
                print(f"\nVocê emite aprox. {emissaoAnual:.2f}kg de CO² por ano")
                compensacao = 21.8 
                print(f"\nVocê precisa plantar {emissaoAnual / compensacao:.2f} arvores por ano para compensar")

                break
            except:
                print("Por favor digite um inteiro: ")

input()