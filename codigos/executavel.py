# Aqui, vou colocar todas as funções que utilizarei no para gerar o aplicativo
from time import sleep

def Linhas2(tam = 29):
    print(tam*'=+')

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

##############################################################################################


######################### Qual é a bandeira do cartão ########################################
def VerficaBandeira(msg):
    while True:
        n = str(input(msg)).lower()
        sleep(1)
        if n == 'visa':
            Linhas('A Bandeira escolida é \033[32mVISA\033[m!')
            return n
        elif n == 'mastercard':
            Linhas('A Bandeira escolida é \033[33mMASTERCARD\033[m!')
            return n
        elif n == 'elo':
            Linhas('A Bandeira escolida é \033[34mELO\033[m!')
            return n
        elif n == 'hipercard':
            Linhas('A Bandeira escolida é \033[33mHIPERCARD\033[m!')
            return n
        else:
            print('Bandeira do cartão não cadastrada.')
            continue
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
    # as taxas das bandeiras são baseadas na maquininha ton no plano GigaTon
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
            elif DebitoOuCredito == 6: # Será que tenho que adicionar um 'and parcelas = 1'?
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



# x = TaxaBandeira('elo', 12, 6)
# print(x)

##############################################################################################


############### Calcula o preço que o vendedor pode colocar no produto #######################

# Para definirmos nosso valor ideal do preço do produto temos que saber como a nossa loja funciona e com qual frequência o produto está sendo vendido, se estiver sendo muito vendido, podemos aumenter a nossa margem de lucro, se não, diminuir, se for muito dificil de produzir, podemos aumentar, e assim por diante. Temos vários fatores que acarretam na variação do lucro, mas, digamos que podemos definir uma margem de lucro depedendo do preço do produto, por exemplo, se o produto custa entre 0 < custo < 500 a margem de lucro é de 10% em cima do valor do produto, caso o valor aumente, eu posso diminuir a porcentagem, entretanto o lucro será maior.

# essa função calcula o lucro, desconto máximo e preço ideal para o produto ser vendido 


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
                     soma += i*ValorCompra

                 media = soma/len(listaTaxas)

                 ValorVenda = ValorCompra + 3*media + taxa*ValorCompra
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
###############################################################################################


Linhas("\033[33mLucro Ideal\033[m")
bandeira = VerficaBandeira('\033[33mQual é a Bandeira do Seu Cartão:\033[m ')
Linhas2()
debcred = DebCred('\033[33mVai ser no débito ou no crédito:\033[m ')
Linhas2()
parcelas = QuantidadeParcelas('\033[33mQuantas Parcelas:\033[m ')
taxa = TaxaBandeira(bandeira, parcelas, debcred)
Linhas('\033[33mCalculando a taxa da Bandeira...\033[m')
sleep(1.5)
valComp = VerificaFloat("\033[33mQual é o preço do produto comprado pelo vendedor:\033[m ")
lista = ldp(valComp, bandeira, taxa)
Linhas("\033[33mCalculando o desconto...\033[m")
sleep(1.5)
#print(f'\n O Lucro da venda sem desconto é de R${lista[0]:.2f} \n Sendo a magem de lucro igual a {lista[1]:.2f}% \n Com isso o desconto Máximo que podemos dar é igual a R${lista[3]:.2f}')
tabela = ['Lucro', 'Margem de Lucro', 'Preço Ideal', 'Desconto Máximo']

for i in range(4):
    if i == 1:
        print(f"\033[3{i}m {tabela[i]} : {lista[i]:.2f}%\033[m")
        Linhas2(tam=29)
        sleep(1)
    else:
        print(f"\033[3{i}m {tabela[i]} : R${lista[i]:.2f}\033[m")
        Linhas2(tam=29)
        sleep(1)