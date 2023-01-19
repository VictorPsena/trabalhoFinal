# def teste(msg):
#     try:
#         n = str(input(msg))
#     except 



# n = str(input("Digite parte do seu nome: "))
# lista = ['victor', 'sena']

# for i in lista:
#     if n == i:
#         print(f'o nome digitado é {i}')
#     elif n != i:
#         print('Digeite um valor válido')
        
# x = str(input("qual seu nome: "))
# print(x)

# n = 5
# taxa = 0
# listaDeTaxas = ['taxa1', 'taxa2', 'taxa3', 'taxa4', 'taxa5', 'taxa6', 'taxa7', 'taxa8','taxa9', 'taxa10', 'taxa11', 'taxa12']
# for i in range(len(listaDeTaxas)):
#     if n-1 == i:
#         taxa = listaDeTaxas[i]
# print(taxa)

# def Soma( num1, num2):
#     soma = num1 + num2 
#     return soma

# x = Soma(1, 2)
# print(x)



def ldp(ValorCompra,  bandeira, TaxaCartao):
    ValorVenda = 0
    listaTaxas =[]
    Lucro_Liq = 0
    Lucro_marg = 0
    desconMax = 0
    while True:
        if bandeira == 'visa' or bandeira == 'mastercard':
             if  0 < ValorCompra < 500: #grupo 1
                 listaTaxas = [0.0369, 0.0599, 0.0629, 0.0715, 0.0799, 0.0879, 0.0959, 0.1039,  0.1119, 0.1199, 0.1279, 0.1349]
                 taxa = 0.12 # em cada if a única coisa que muda é a taxa 
                 soma = 0
                 for i in listaTaxas:
                     soma += i*(ValorCompra*taxa + ValorCompra)

                 media = soma/len(listaTaxas)

                 ValorVenda = ValorCompra  + media + taxa*ValorCompra # O valor da compra tem que ser alterado, pois como quero lucro mínimo, tenho que ter os 10% dentro do valor antes de add o valor da venda.
                 Val_Comp = ValorCompra 
                 Val_Vend = ValorVenda
                 Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp
                 Lucro_marg = Lucro_Liq/Val_Vend
                 desconMax = Lucro_Liq - Val_Vend*taxa # onde muda
                 if Lucro_marg < 0.1:
                    return 'Compra cancelado, tente renegociar.'
                 else:
                    return [Lucro_Liq, Lucro_marg*100, ValorVenda, desconMax ]

        
             elif  500 <= ValorCompra < 5000: #grupo 2 
                 listaTaxas = [0.0369, 0.0599, 0.0629, 0.0715, 0.0799, 0.0879, 0.0959, 0.1039,  0.1119, 0.1199, 0.1279, 0.1349]
                 taxa = 0.11 # aqui muda
                 soma = 0
                 for i in listaTaxas:
                     soma += i*ValorCompra

                 media = soma/len(listaTaxas)
                
 
                 ValorVenda = ValorCompra + 3*media + taxa*ValorCompra
                 Val_Comp = ValorCompra
                 Val_Vend = ValorVenda
                 Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp
                 Lucro_marg = Lucro_Liq/Val_Vend
                 desconMax = Lucro_Liq - Val_Vend*taxa
                 if Lucro_marg < 0.1:
                    return 'Compra cancelado, tente renegociar.'
                 else:
                    return [Lucro_Liq, Lucro_marg*100, ValorVenda, desconMax ]
        
             elif  5000 <= ValorCompra <= 50000: #grupo 3
                 listaTaxas = [0.0369, 0.0599, 0.0629, 0.0715, 0.0799, 0.0879, 0.0959, 0.1039,  0.1119, 0.1199, 0.1279, 0.1349]
                 taxa = 0.07 # aqui muda
                 soma = 0
                 for i in listaTaxas:
                     soma += i*ValorCompra

                 media = soma/len(listaTaxas)

                 ValorVenda = ValorCompra + 3*media + taxa*ValorCompra
                 Val_Comp = ValorCompra
                 Val_Vend = ValorVenda
                 Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp
                 Lucro_marg = Lucro_Liq/Val_Vend
                 desconMax = Lucro_Liq - Val_Vend*taxa # onde altera
                 if Lucro_marg < 0.1:
                    return 'Compra cancelado, tente renegociar.'
                 else:
                    return [Lucro_Liq, Lucro_marg*100, ValorVenda, desconMax ]
                
             else:
                 print("O Valor do produto excede os valores cadastrados ")
                 ValorCompra = int(input("Digite o valor da compra: "))
                 continue


        # Agora vamos fazer para as bandeira 'elo' e 'hipercard'

        elif bandeira == 'elo' or bandeira == 'hipercard':
            if 0 < ValorCompra < 500:
                    listaTaxas = [0.0488, 0.0738, 0.0768, 0.0854, 0.0938, 0.1018, 0.1098, 0.1178, 0.1258,  0.1338, 0.1418, 0.1488]
                    taxa = 0.1
                    soma = 0
                    for i in listaTaxas:
                        soma += i*ValorCompra

                    media = soma/len(listaTaxas)

                    ValorVenda = ValorCompra + 3*media + taxa*ValorCompra
                    Val_Comp = ValorCompra
                    Val_Vend = ValorVenda
                    Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp
                    Lucro_marg = Lucro_Liq/Val_Vend
                    desconMax = Lucro_Liq - Val_Vend*taxa # onde altera
                    if Lucro_marg < 0.1:
                        return 'Compra cancelado, tente renegociar.'
                    else:
                        return [Lucro_Liq, Lucro_marg*100, ValorVenda, desconMax ]


            elif  500 <= ValorCompra < 5000:
                    listaTaxas = [0.0488, 0.0738, 0.0768, 0.0854, 0.0938, 0.1018, 0.1098, 0.1178, 0.1258,  0.1338, 0.1418, 0.1488]
                    taxa = 0.08
                    soma = 0
                    for i in listaTaxas:
                        soma += i*ValorCompra

                    media = soma/len(listaTaxas)
                    
                    
                    ValorVenda = ValorCompra + 3*media + taxa*ValorCompra
                    Val_Comp = ValorCompra
                    Val_Vend = ValorVenda
                    Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp
                    Lucro_marg = Lucro_Liq/Val_Vend
                    desconMax = Lucro_Liq - Val_Vend*taxa # onde altera
                    if Lucro_marg < 0.1:
                        return 'Compra cancelado, tente renegociar.'
                    else:
                        return [Lucro_Liq, Lucro_marg*100, ValorVenda, desconMax ]

            elif 5000 <= ValorCompra <= 50000:
                    listaTaxas = [0.0488, 0.0738, 0.0768, 0.0854, 0.0938, 0.1018, 0.1098, 0.1178, 0.1258,  0.1338, 0.1418, 0.1488]
                    taxa = 0.05
                    soma = 0
                    for i in listaTaxas:
                        soma += i*ValorCompra

                    media = soma/len(listaTaxas)
                    
                    
                    ValorVenda = ValorCompra + 3*media + taxa*ValorCompra
                    Val_Comp = ValorCompra
                    Val_Vend = ValorVenda
                    Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp
                    Lucro_marg = Lucro_Liq/Val_Vend
                    desconMax = Lucro_Liq - Val_Vend*taxa # onde altera
                    if Lucro_marg < 0.1:
                        return 'Compra cancelado, tente renegociar.'
                    else:
                        return [Lucro_Liq, Lucro_marg*100, ValorVenda, desconMax ]
            else:
                 print("O Valor do produto excede os valores cadastrados ")
                 ValorCompra = int(input("Digite o valor da compra: "))
                 continue

        else:
           print("\033[33mAlgum valor está errado\033[m")
           ValorCompra = int(input("Digite o valor da compra: "))
           bandeira = str(input("Informe a bandeira: ")).lower()
           continue


# opcao = DebCred('Débito ou Crédito: ')
# taxa = TaxaBandeira('elo', 12, opcao )
# print(taxa)
# lista =ldp(50000, 'elo', taxa )
# print(lista)



 #######################################################################################################

# def ldp(ValorCompra,  bandeira, TaxaCartao):
#     ValorVenda = 0
#     listaTaxas =[]
#     Lucro_Liq = 0
#     Lucro_marg = 0
#     desconMax = 0
#     precos = 0
    



#     while True:
#         if bandeira == 'visa' or bandeira == 'mastercard':
#              if  0 < ValorCompra <= 500: #grupo 1
#                  #listaTaxas = [0.0369, 0.0599, 0.0629, 0.0715, 0.0799, 0.0879, 0.0959, 0.1039,  0.1119, 0.1199, 0.1279, 0.1349] # Aqui vamos verificar a taxa vinculada as parcelas
#                  taxa = 0.12 # em cada if a única coisa que muda é a taxa 
#                  listapreco = [0.0369, 0.0599, 0.0629, 0.0715, 0.0799, 0.0879, 0.0959, 0.1039,  0.1119, 0.1199, 0.1279, 0.1349, 0.0488, 0.0738, 0.0768, 0.0854, 0.0938, 0.1018, 0.1098, 0.1178, 0.1258,  0.1338, 0.1418, 0.1488] # Tem as taxas de todos os cartões.
#                  for i in listapreco:
#                      precos += i*(ValorCompra*taxa + ValorCompra) + (ValorCompra*taxa + ValorCompra) # o 'ValorCompra*taxa + valorCompra' é o meu valor mínimo da venda, ou seja, não posso ter um preço menor que esse.
#                      print(precos)

#                  #  soma = 0
#                  #for i in listaTaxas:
#                  #     soma += i*(ValorCompra*taxa + ValorCompra) 

#    #              media = soma/len(listaTaxas)
#                  mediaprecos = precos/len(listapreco)
#                  print(mediaprecos)
#    #              print(soma)
#    #              print(media)

#    #              ValorVenda = ValorCompra  + media + taxa*ValorCompra 
#                  Val_Comp = ValorCompra 
#                  Val_Vend = mediaprecos + listapreco[23]*ValorCompra 
#                  Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp
#                  Lucro_marg = Lucro_Liq/Val_Vend
#                  desconMax = Val_Vend - (ValorCompra*taxa + ValorCompra) # onde muda
#                  if Lucro_marg < 0.1:
#                     return 'Compra cancelado, tente renegociar.'
#                  else:
#                     return [Lucro_Liq, Lucro_marg*100, Val_Vend, desconMax]

# print(ldp(499, 'visa',  0.1488))          


#########################################################################################################################################


def ldp(ValorCompra,  bandeira, TaxaCartao):
    Lucro_Liq = 0
    Lucro_marg = 0
    desconMax = 0
    precos = 0

    while True:
        listapreco = [0.0369, 0.0599, 0.0629, 0.0715, 0.0799, 0.0879, 0.0959, 0.1039,  0.1119, 0.1199, 0.1279, 0.1349, 0.0488, 0.0738, 0.0768, 0.0854, 0.0938, 0.1018, 0.1098, 0.1178, 0.1258,  0.1338, 0.1418, 0.1488]
        if bandeira == 'visa' or bandeira == 'mastercard':
            
            if  0 < ValorCompra < 500: #grupo 1
                 taxa = 0.12 # em cada if a única coisa que muda é a taxa 
                 # Tem as taxas de todos os cartões.
                 for i in listapreco:
                     precos += i*(ValorCompra*taxa + ValorCompra) + (ValorCompra*taxa + ValorCompra) # o 'ValorCompra*taxa + valorCompra' é o meu valor mínimo da venda, ou seja, não posso ter um preço menor que esse.


                 mediaprecos = precos/len(listapreco) # Como eu não sei em qual bandeira o meu cliente vai comprar antes de anunciar o produto, faço uma previsão, pego todas as taxa do cartão e divido pela quantidade de taxas, obtendo assim uma média de preços.
                 Val_Comp = ValorCompra 
                 Val_Vend = mediaprecos + listapreco[23]*ValorCompra # Como obti a média de preços, caso o meu cliente queira comprar com a maior parcela tenho que fazer essa previsão na hora de inserir o preço. Então no caso do nosso programa, estamos sempre prevendo a maior parcela do cartão, que no nosso caso é 0.1488
                 Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp # onde muda
                 print(TaxaCartao*Val_Vend)
                 print(TaxaCartao)
                 Lucro_marg = Lucro_Liq/Val_Vend
                 desconMax = Val_Vend - (ValorCompra*taxa + ValorCompra) - TaxaCartao*Val_Vend # o desconto máximo está deixando apenas os 12% de lucro mínimo para esse tipo de valor.
                 if Lucro_marg < 0.1:
                    return 'Compra cancelado, tente renegociar.'
                 else:
                    return [Lucro_Liq, Lucro_marg*100, Val_Vend, desconMax]
                 

        elif bandeira == 'elo' or bandeira == 'hipercard':
            if 0 < ValorCompra < 500:
                    taxa = 0.12
                    for i in listapreco:
                     precos += i*(ValorCompra*taxa + ValorCompra) + (ValorCompra*taxa + ValorCompra)

                 
                    mediaprecos = precos/len(listapreco)
                    Val_Comp = ValorCompra
                    Val_Vend = mediaprecos + listapreco[23]*ValorCompra
                    Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp
                    print(TaxaCartao*Val_Vend)
                    print(TaxaCartao)
                    Lucro_marg = Lucro_Liq/Val_Vend
                    desconMax = Val_Vend - (ValorCompra*taxa + ValorCompra) - TaxaCartao*Val_Vend
                    if Lucro_marg < 0.1:
                        return 'Compra cancelado, tente renegociar.'
                    else:
                        return [Lucro_Liq, Lucro_marg*100, Val_Vend, desconMax ]


print(ldp(200, 'elo',  0.1488))   
