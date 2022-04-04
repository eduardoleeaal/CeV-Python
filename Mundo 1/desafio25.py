nome = str(input('Digite seu nome: ')).strip()

if(nome.upper().find('SILVA')):           # Da pra usar o operador 'in' 
    print('Seu nome tem Silva')           # Ex: 'Silva' in nome
else:
    print('Seu nome não tem Silva')