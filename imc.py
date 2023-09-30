nome = input('Digite seu nome: ')

valid_peso = False
while not valid_peso:
    peso = input('Digite seu peso: ')
    try:
        peso = float(peso)
        if peso < 0:
            print('Peso deve ser maior que 0')
            valid_peso = False
        else:
            valid_peso = True
    except:
        print('Peso inválido. Use apenas números e separe os decimais com ponto')

valid_peso = False

valid_altura = False
while valid_altura == False:
    altura = input('Digite sua altura: ')
    try:
        altura = float(altura)
        if altura < 0:
            print('Altura deve ser maior que 0')
            valid_altura = False

        else:
            valid_altura = True
    except:
        print('Altura inválida. Use apenas números e separe os decimais com ponto')

valid_altura = False

imc = peso / (altura * altura)

print(nome, 'Seu índice de massa corporal é {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')

elif imc <= 25:
    print('Peso normal')

elif imc <= 30:
    print('Pré-obeso')

elif imc <= 35:
    print('Obesidade I')

elif imc <= 40:
    print('Obesidade II')

else:
    print('Obesidade III')

