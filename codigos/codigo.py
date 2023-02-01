#Aqui será escrito o código para o trabalho final de Modelagem Matemática.
from lib.FuncCompiladas import *
#from lib.FuncTeste import PrecoIdeal
from time import sleep

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
tabela = ['Lucro', 'Margem de Lucro', 'Preço Ideal', 'Desconto Máximo', 'Lucro mínimo', 'Tarifa da maquininha', 'parcelas']
lista.append(lista[2]/parcelas)
if lista == 1:
    print("Tente renegociar com o cliente, prejuizo a vista!")
else:
    for i in range(7):
        if i == 1:
            print(f"\033[3{i}m {tabela[i]} : {lista[i]:.2f}%\033[m")
            Linhas2(tam=29)
            sleep(1)
        else:
            print(f"\033[3{i}m {tabela[i]} : R${lista[i]:.2f}\033[m")
            Linhas2(tam=29)
            sleep(1)


while True:
    desconto = VerificaFloat("Qual o desconto que você deseja dar? ")
    if desconto > lista[3]:
        print(f"Digite uma valor menor ou igual a R${lista[3]:.2f}")
        continue
    else: 
        sleep(1)
        print(f"\no lucro atual é de: R${lista[0]-desconto:.2f} \nMargem de Lucro: {((lista[0]-desconto)/lista[2])*100:.2f}% \nDesconto  máximo: R${lista[3]-desconto:.2f} \nPreço da venda atual: R${lista[2]-desconto:.2f} \nPacelas: R${(lista[2]-desconto)/parcelas:.2f}")
        break

