import emoji
cores = {
    'verde':'\033[32m',
    'vermelho':'\033[31m',
    'amarelo':'\033[33m',
    'limpa':'\033[m'
         }
tabela = ('Palmeiras', 'Santos', 'Flamengo', 'Atletico-MG', 'Botafogo', 'Athlético-PR', 'Corinthians', 'Ponte Preta', 'Grêmio', 'São Paulo', 'Chapecoense', 'Cruzeiro', 'Fluminense', 'Sport Recife', 'Coritiba', 'Vitória', 'Internacional', 'Figueirense', 'Santa Cruz', 'América-MG')

print(cores['verde'], end='')
print('-=-' * 15)
print('{:>12}5 Primeiros'.format(''), end=' ')
print(emoji.emojize(':rosto_sorridente_com_óculos_escuros:', language='pt'))
print('-=-' * 15)
print(cores['limpa'], end='')

for pos, prim in enumerate(tabela[:5]):
    print(f'O {pos + 1}º colocado é {prim}')
    
print(cores['vermelho'], end='')
print('-=-' * 15)
print('{:>12}REBAIXADOS'.format(''), end=' ')
print(emoji.emojize(':rosto_neutro:', language='pt'))
print('-=-' * 15)
print(cores['limpa'], end='')

for pos, ult in enumerate(tabela[16:]):
    print(f'O {pos + 17}º colocado é {ult}')
    
print(cores['amarelo'], end='')
print('-=-' * 15)
print('{:>8}Tabela em ordem alfabética'.format(''))
print('-=-' * 15)
print(cores['limpa'], end='')

tabela_org = sorted(tabela)
for cont in tabela_org:
    print(cont)

print(cores['verde'], end='')
print('-=-' * 15)
print('{:>12}Chapecoense: '.format(''))
print('-=-' * 15)
print(cores['limpa'], end='')
print(f'O Chapecoense está na posição: {tabela.index("Chapecoense") + 1}º\n\n')

