compra = float(input('Digite o valor total da sua comra\n'))
parcela = int(input('Digite a quantidade de parcelas\n'))

p2 = compra*0.03+compra
p4 = compra*0.07+compra
p6 = compra*0.09+compra
p8 = compra*0.12

if parcela <= 2:
    print('O valor da parcela é:', p2/parcela)
elif parcela <=4:
    print('O valor da parcela é:', p4/parcela)
elif parcela <=6:
    print('O valor da parcela é:', p6/parcela)
elif parcela <=8:
    print('O valor da parcela é:', p8/parcela)