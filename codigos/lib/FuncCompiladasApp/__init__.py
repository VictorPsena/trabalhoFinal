# Aqui, vou colocar todas as funções que utilizarei no para gerar o aplicativo
def DebCred(msg):
    while True:
        n = msg.upper().strip()[0]
      
        if n =='C':
            x = 7
            return x
        elif n =='D':
            x = 6
            return x
        else:
            print('\033[31mOpção inválida\033[m, escolha entre crédito ou débito.')
            continue

def TaxaBandeira(bandeira, parcelas, DebitoOuCredito):

    taxa = 0
    listaCreditoVM = [0.0369, 0.0599, 0.0629, 0.0715, 0.0799, 0.0879, 0.0959, 0.1039,  0.1119, 0.1199, 0.1279, 0.1349]
    listaDebitoVM = 0.0179
    
    listaCreditoEH = [0.0488, 0.0738, 0.0768, 0.0854, 0.0938, 0.1018, 0.1098, 0.1178, 0.1258,  0.1338, 0.1418, 0.1488]
    listaDebitoEH = 0.0298
    while True:
        if bandeira == 'visa' or bandeira == 'mastercard':
            if DebitoOuCredito == 7:
                for i in range(len(listaCreditoVM)):
                    if parcelas - 1 == i:
                        taxa = listaCreditoVM[i]
                        return taxa
                    else:
                        continue
            elif DebitoOuCredito == 6:
                taxa = listaDebitoVM
                return taxa
            else:
                print("opção inválida")
                DebitoOuCredito = DebCred("Escolha entre Débito ou Crédito: ")
                continue
        elif bandeira == 'elo' or bandeira == 'hipercard':
            if DebitoOuCredito == 7:
                for i in range(len(listaCreditoEH)):
                    if parcelas - 1 == i:
                        taxa = listaCreditoEH[i]
                        return taxa
                    else:
                        continue
            elif DebitoOuCredito == 6:
                taxa = listaDebitoEH
                return taxa
            else:
                print("opção inválida")
                DebitoOuCredito = DebCred("Escolha entre Débito ou Crédito: ")
                continue



def ldp(ValorCompra,  bandeira, TaxaCartao):
    Lucro_Liq = 0
    Lucro_marg = 0
    desconMax = 0
    precos = 0

    while True:
        listapreco = [0.0369, 0.0599, 0.0629, 0.0715, 0.0799, 0.0879, 0.0959, 0.1039,  0.1119, 0.1199, 0.1279, 0.1349, 0.0488, 0.0738, 0.0768, 0.0854, 0.0938, 0.1018, 0.1098, 0.1178, 0.1258,  0.1338, 0.1418, 0.1488]
        if bandeira == 'visa' or bandeira == 'mastercard':
            
            if  0 < ValorCompra < 500: 
                 taxa = 0.12 
                 for i in listapreco:
                     precos += i*(ValorCompra*taxa + ValorCompra) + (ValorCompra*taxa + ValorCompra) #

                 mediaprecos = precos/len(listapreco) 
                 Val_Comp = ValorCompra 
                 Val_Vend = mediaprecos + listapreco[23]*ValorCompra 
                 Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp
                 Lucro_marg = Lucro_Liq/Val_Vend
                 desconMax = Val_Vend - (ValorCompra*taxa + ValorCompra) - TaxaCartao*Val_Vend 
                 taxamaquina = Val_Vend*TaxaCartao
                 lucromin = ValorCompra*taxa
                 if Lucro_marg < 0.1:
                    return 1
                 else:
                    return [Lucro_Liq, Lucro_marg*100, Val_Vend, desconMax, lucromin, taxamaquina ]

        
            elif  500 <= ValorCompra < 5000: #grupo 2 
                 taxa = 0.10 # aqui muda
                 for i in listapreco:
                     precos += i*(ValorCompra*taxa + ValorCompra) + (ValorCompra*taxa + ValorCompra)

                 
                 mediaprecos = precos/len(listapreco)
                 Val_Comp = ValorCompra
                 Val_Vend = mediaprecos + listapreco[23]*ValorCompra
                 Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp
                 Lucro_marg = Lucro_Liq/Val_Vend
                 desconMax = Val_Vend - (ValorCompra*taxa + ValorCompra) - TaxaCartao*Val_Vend
                 lucromin = ValorCompra*taxa
                 taxamaquina = Val_Vend*TaxaCartao
                 if Lucro_marg < 0.1:
                    return 1
                 else:
                    return [Lucro_Liq, Lucro_marg*100, Val_Vend, desconMax, lucromin, taxamaquina ]
        
            elif  5000 <= ValorCompra <= 50000: #grupo 3
                 taxa = 0.07 # aqui muda
                 for i in listapreco:
                     precos += i*(ValorCompra*taxa + ValorCompra) + (ValorCompra*taxa + ValorCompra)

                 
                 mediaprecos = precos/len(listapreco)
                 Val_Comp = ValorCompra
                 Val_Vend = mediaprecos + listapreco[23]*ValorCompra
                 Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp
                 Lucro_marg = Lucro_Liq/Val_Vend
                 desconMax = Val_Vend - (ValorCompra*taxa + ValorCompra) - TaxaCartao*Val_Vend
                 lucromin = ValorCompra*taxa
                 taxamaquina = Val_Vend*TaxaCartao

                 if Lucro_marg < 0.08:
                    return 1
                 else:
                    return [Lucro_Liq, Lucro_marg*100, Val_Vend, desconMax, lucromin, taxamaquina ]
                


        # Agora vamos fazer para as bandeira 'elo' e 'hipercard'

        elif bandeira == 'elo' or bandeira == 'hipercard':
            if 0 < ValorCompra < 500:
                    taxa = 0.12
                    for i in listapreco:
                     precos += i*(ValorCompra*taxa + ValorCompra) + (ValorCompra*taxa + ValorCompra)

                 
                    mediaprecos = precos/len(listapreco)
                    Val_Comp = ValorCompra
                    Val_Vend = mediaprecos + listapreco[23]*ValorCompra
                    Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp
                    Lucro_marg = Lucro_Liq/Val_Vend
                    desconMax = Val_Vend - (ValorCompra*taxa + ValorCompra) - TaxaCartao*Val_Vend
                    lucromin = ValorCompra*taxa
                    taxamaquina = Val_Vend*TaxaCartao
                    if Lucro_marg < 0.1:
                        return 1
                    else:
                        return [Lucro_Liq, Lucro_marg*100, Val_Vend, desconMax, lucromin, taxamaquina ]


            elif  500 <= ValorCompra < 5000:
                    taxa = 0.10
                    for i in listapreco:
                     precos += i*(ValorCompra*taxa + ValorCompra) + (ValorCompra*taxa + ValorCompra)

                 
                    mediaprecos = precos/len(listapreco)
                    Val_Comp = ValorCompra
                    Val_Vend = mediaprecos + listapreco[23]*ValorCompra
                    Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp
                    Lucro_marg = Lucro_Liq/Val_Vend
                    desconMax = Val_Vend - (ValorCompra*taxa + ValorCompra) - TaxaCartao*Val_Vend
                    lucromin = ValorCompra*taxa
                    taxamaquina = Val_Vend*TaxaCartao

                    if Lucro_marg < 0.08:
                        return 1
                    
                    else:
                        return [Lucro_Liq, Lucro_marg*100, Val_Vend, desconMax, lucromin, taxamaquina ]

            elif 5000 <= ValorCompra <= 50000:
                    taxa = 0.08
                    for i in listapreco:
                     precos += i*(ValorCompra*taxa + ValorCompra) + (ValorCompra*taxa + ValorCompra)

                 
                    mediaprecos = precos/len(listapreco)
                    Val_Comp = ValorCompra
                    Val_Vend = mediaprecos + listapreco[22]*ValorCompra
                    Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp
                    Lucro_marg = Lucro_Liq/Val_Vend
                    desconMax = Val_Vend - (ValorCompra*taxa + ValorCompra) - TaxaCartao*Val_Vend
                    lucromin = ValorCompra*taxa
                    taxamaquina = Val_Vend*TaxaCartao

                    if Lucro_marg < 0.05:
                        return 1

                    else:
                        return [Lucro_Liq, Lucro_marg*100, Val_Vend, desconMax, lucromin, taxamaquina ]

        else:
           print("\033[33mAlgum valor está errado\033[m")
           ValorCompra = int(input("Digite o valor da compra: "))
           bandeira = str(input("Informe a bandeira: ")).lower()
           continue


####################################################################################