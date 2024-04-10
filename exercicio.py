idade = int(input('Digite sua idade\n'))

if idade <16:
    print('voce nao pode votar')
elif idade >18 and idade <65:
    print('voce e obrigado a votar')
else:
    print('eleitor facultativo')