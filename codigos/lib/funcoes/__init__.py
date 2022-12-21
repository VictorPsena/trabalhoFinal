from time import sleep

def Linhas2(tam = 42):
    print(tam*'\033[32m=\033[m')

def Linhas(msg):
    print('='*42)
    print(msg.center(42))
    print('='*42)

############################## verfica se o num é int ou float ###############################
def VerificaFloat(msg):
    while True:
        try:
            x = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO\033[m, Digite um valor válido')
            continue
        else:
            return x


def VerificaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('Erro, digite um valor inteiro')
            continue
        else:
            return n
#####################################Taxa de lucro ###########################################




######################### Qual é a bandeira do cartão ########################################
def VerficaBandeira(msg):
    bandeiras = ['visa', 'mastercard', 'elo', 'hipercard']
    n = str(input(msg)).lower()
    for i in bandeiras:
        if n == i:
            sleep(1)
            Linhas(f"A Bandeira Escolida é \033[3{len(i)}m{i.upper()}\033[m")
            sleep(1)
        else:
            continue
    return n
###############################################################################################

######################## Mostra as taxas da bandeira escolida1.0 #############################

# def BandeiraEscolida(msg):
#     taxa = 0
#     parcelando = 0

#     if msg == 'visa':
#         taxa = 2.5
#         parcelando = 1.99
#         print(f'Na bandeira {msg.upper()} a taxa a vista é {taxa}% e parcelado é {parcelando}%')
#         Linhas2()
#         lista = [taxa, parcelando]
#         return lista
#     elif msg == 'mastercard':
#         taxa = 2.5
#         parcelando = 1.58
#         print(f'Na bandeira {msg.upper()} a taxa a vista é {taxa}% e parcelado é {parcelando}%')
#         Linhas2()
#     elif msg == 'elo':
#         taxa = 2.8
#         parcelando = 1.4
#         print(f'Na bandeira {msg.upper()} a taxa a vista é {taxa}% e parcelado é {parcelando}%')
#         Linhas2()
#         lista = [taxa, parcelando]
#     elif msg == 'hipercard':
#         taxa = 2.1
#         parcelando = 1.2
#         print(f'Na bandeira {msg.upper()} a taxa a vista é {taxa}% e parcelado é {parcelando}%')
#         Linhas2()
#         lista = [taxa, parcelando]

##############################################################################################

        
        

############################### Débito ou crédito ###########################################
# 7 siginifica que a compra será efetuada no crédito 
# 6 siginifica que a compra será efetuada no débito
def DebCred(msg):
    while True:
        n = str(input(msg)).upper().strip()[0]
        
        if n =='C':
            x = 7
            return x
        elif n =='D':
            x = 6
            return x
        else:
            print('\033[31mOpção inválida\033[m, escolha entre crédito ou débito.')
            continue

# x = DebCred("Escolha: ")
# print(x)
##############################################################################################



#########################    Quantidade de parcelas ##########################################
def QuantidadeParcelas(msg):
    while True: 
        x = VerificaInt(msg)
        if 1 <= x <= 12:
            return x
        else:
            print("O máximo que conseguimos parcelar é 12 vezes.")
            continue

# x = QuantidadeParcelas("Quantidade de parcelas: ")
# print(x)

##############################################################################################



############ Mostra as taxas da bandeira escolida 2.0 tendo o número de parcelas #############

def TaxaBandeira(bandeira, parcelas, DebitoOuCredito):
    # band = str(bandeira)
    # parc = int(parcelas)
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



# x = TaxaBandeira('elo', 5, 8)
# print(x)

##############################################################################################







#################################### Se for parcelado ########################################

# def Parcelado(msg):
#     juros = 0
#     if msg == 's':
#         juros = 5.19
#         print(f"O valor do juros em cada parcela é de \033[33m{juros}%\033[m")
#     elif msg == 'n':
#         juros = 1.99
#         print(f"O valor do juros em cada parcela é de \033[33m{juros}%\033[m")
#     else:
#         print('Opção inválida')
#     return juros
###############################################################################################

########################### Se for parcelado 2.0 ############################################



# def Parcelado2(msg):
#     n = msg 
#     taxa = 0
#     listaDeTaxas = ['taxa1', 'taxa2', 'taxa3', 'taxa4', 'taxa5', 'taxa6', 'taxa7', 'taxa8','taxa9', 'taxa10', 'taxa11', 'taxa12']
#     for i in len(listaDeTaxas):
#         if n-1 == i:
#             taxa = listaDeTaxas[i]
#     return taxa



###############################################################################################

# def LucroMinimoTotal(quantidade, MaiorTaxa, ValorDoPoduto, LucroMinimo):
#     for i in range(quantidade):
#         lucro = MaiorTaxa*ValorDoPoduto + (LucroMinimo*ValorDoPoduto)/i
    
#     print(lucro)
 

# LucroMinimoTotal(3, 0.2, 1000, 0.5 )
###############################################################################################


#####################################Taxa de lucro ###########################################
# Para calcular o desconto máximo é nescessario estipular um lucro mínimo liquido(%), estipulado o lucro mínimo, a porcentagem de desconto não pode ser menor que o lucro minimo liquido.

def DescontoMax(ValorCompra, ValorVenda, TaxaCartao):
    Lucro_Liq = 0
    Lucro_marg = 0
    taxa = 0
    while True:
     Val_Comp = VerificaFloat(ValorCompra)
     Val_Vend = VerificaFloat(ValorVenda)
     Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp
     Lucro_marg = Lucro_Liq/Val_Vend
     if 0 < Val_Vend < 500:
        if Lucro_marg < 0.1:
            print()
     elif 500 <= Val_Vend < 5000:
        taxa = 0.05
     else:
        print("Valor da Compra não cadastrado")
        continue





###############################################################################################




#################### Atribui a taxa relacionada ao valor da compra ##############################

# def VerificaValorCompra(valor):
#     taxa = 0
#     while True:
#         if 0 < valor < 500:
#             taxa = 0.05
#             return taxa
#         elif 500 <= valor < 5000:
#             taxa = 0.1
#             return taxa
#         elif 5000 <= valor <= 20000:
#             taxa = 0.04
#             return taxa
#         else:
#             print('valor da compra \033[34minválido\033[m')
#             while True:
#                 try:
#                     valor = float(input("Digite o valor da compra: "))
#                 except (ValueError, TypeError):
#                     print('Valor da Compra \033[34minválido\033[m')
#                     continue
#                 else:
#                     break
#             continue
##############################################################################################


