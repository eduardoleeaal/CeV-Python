from datetime import date
nascimento = int(input('Digite o seu ano de nascimento: '))

idade = date.today().year - nascimento

if idade > 18:
    ano = date.today().year - (idade - 18)
    print('O tempo de alistamento já passou! \nEra para você ter se alistado em {}'.format(ano))
elif idade == 18:
    print('É hora de se alistar')
elif idade < 18:
    tempo_restante = 18 - idade
    ano = date.today().year + tempo_restante
    print('Ainda faltam {} Anos para o alistamento \nVocê vai se alistar em {}'.format(tempo_restante, ano))
