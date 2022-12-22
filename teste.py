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



def DescontoMax(ValorCompra,  bandeira):
    ValorVenda = 0
    listaTaxas =[]
    while True:
        if bandeira == 'visa' or bandeira == 'mastercard':
             if  0 < ValorCompra < 500:
                 listaTaxas = [0.0369, 0.0599, 0.0629, 0.0715, 0.0799, 0.0879, 0.0959, 0.1039,  0.1119, 0.1199, 0.1279, 0.1349]
                 taxa = 0.12 # em cada if a única coisa que muda é a taxa 
                 soma = 0
                 for i in listaTaxas:
                     soma += i*ValorCompra

                 media = soma/len(listaTaxas)
                 print(media, 'sim')
                 ValorVenda = ValorCompra + media + taxa*ValorCompra

                 return ValorVenda
       
             elif  500 <= ValorCompra < 5000:
                 listaTaxas = [0.0369, 0.0599, 0.0629, 0.0715, 0.0799, 0.0879, 0.0959, 0.1039,  0.1119, 0.1199, 0.1279, 0.1349]
                 taxa = 0.11 # aqui muda
                 soma = 0
                 for i in listaTaxas:
                     soma += i*ValorCompra

                 media = soma/len(listaTaxas)
                 print(media, 'não')
                 ValorVenda = ValorCompra + media + taxa*ValorCompra
 
                 return ValorVenda
        
             elif  5000 <= ValorCompra <= 50000:
                 listaTaxas = [0.0369, 0.0599, 0.0629, 0.0715, 0.0799, 0.0879, 0.0959, 0.1039,  0.1119, 0.1199, 0.1279, 0.1349]
                 taxa = 0.07 # aqui muda
                 soma = 0
                 for i in listaTaxas:
                     soma += i*ValorCompra

                 media = soma/len(listaTaxas)
                 print(media, 'oi')
                 ValorVenda = ValorCompra + media + taxa*ValorCompra

                 return ValorVenda


        # Agora vamos fazer para as bandeira 'elo' e 'hipercard'

        elif bandeira == 'elo' or bandeira == 'hipercard':
            if 0 < ValorCompra < 500:
                    listaTaxas = [0.0488, 0.0738, 0.0768, 0.0854, 0.0938, 0.1018, 0.1098, 0.1178, 0.1258,  0.1338, 0.1418, 0.1488]
                    taxa = 0.1
                    soma = 0
                    for i in listaTaxas:
                        soma += i*ValorCompra

                    media = soma/len(listaTaxas)
                    print(media, 'v')
                    ValorVenda = ValorCompra + media + taxa*ValorCompra

                    return ValorVenda


            elif  500 <= ValorCompra < 5000:
                    listaTaxas = [0.0488, 0.0738, 0.0768, 0.0854, 0.0938, 0.1018, 0.1098, 0.1178, 0.1258,  0.1338, 0.1418, 0.1488]
                    taxa = 0.08
                    soma = 0
                    for i in listaTaxas:
                        soma += i*ValorCompra

                    media = soma/len(listaTaxas)
                    print(media, 'i')
                    ValorVenda = ValorCompra + media + taxa*ValorCompra

                    return ValorVenda

            elif 5000 <= ValorCompra <= 50000:
                    listaTaxas = [0.0488, 0.0738, 0.0768, 0.0854, 0.0938, 0.1018, 0.1098, 0.1178, 0.1258,  0.1338, 0.1418, 0.1488]
                    taxa = 0.05
                    soma = 0
                    for i in listaTaxas:
                        soma += i*ValorCompra

                    media = soma/len(listaTaxas)
                    print(media, 'c')
                    ValorVenda = ValorCompra + media + taxa*ValorCompra
            
                    return ValorVenda

        else:
           print("\033[33mAlgum valor está errado\033[m")
           ValorCompra = int(input("Digite o valor da compra: "))
           bandeira = str(input("Informe a bandeira: ")).lower()
           continue

x = DescontoMax(4999, 'elo') # Perceni que 499 rende mais do que 500
print(f'R${x:.2f}')


# def Valor(num, num2):
#     if 0 < num2 < 10:
#         if num == 2 or num == 4:
#             print(num2)
#         else:
#              print('Funcionou')

# Valor(2, 1)