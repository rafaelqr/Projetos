cidade = input('Digite sua cidade: ')

sul = ['Curitiba','Porto Alegre','Blumenau']
sudeste = ['Sao Paulo','Rio de Janeiro','Vitoria']
nordeste = ['Porto de Galinhas','Recife','Salvador']

if cidade in sul:
    print('Você mora no Sul')

elif cidade in sudeste:
    print('Você mora no Sudeste')

else:
    print('Você mora no Nordeste')