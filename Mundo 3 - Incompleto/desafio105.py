'''Faça um programa
que tenha uma Função
notas() que pode
receber várias notas
de alunos e vai
retornar um dicionário
com as seguintes
informaçoes:
- Quantidada da notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adiciona também as
docstrings da função.
https://prnt.sc/56euLh_eOknX
'''


def notas(* nota, sit = False):
    """
    -> Função para analisar uma ou mais notas e situações de varios alunos
    :param nota: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indica se deve ou não mostrar a situação.
    :return: dicionario com varias informações sobre a situação da turma.
    """
    tudo = dict()
    tudo['total'] = len(nota)
    tudo['maior'] = max(nota)
    tudo['menor'] = min(nota)
    tudo['media'] = sum(nota) / len(nota)
    if sit:
        if tudo['media'] < 7.0 and tudo['media'] >= 5.0:
            tudo['sit'] = 'RAZOAVEL'
        elif tudo['media'] < 5.0:
            tudo['sit'] = 'CRITICA'
        else:
            tudo['sit'] = 'BOA'
    return tudo


resp = notas(5.5, 9.5, 10, 6.5, sit = True)
print(resp)
