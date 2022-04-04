cidade = str(input('Digite o nome da sua cidade: ')).strip()
if(cidade[:5].upper() == 'SANTO'):
    print('Sua cidade começa com SANTO')
else:
    print('Sua cidade não começa com SANTO')