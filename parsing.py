"""Parsing Tab."""
import os

def padrao_tab(line):
    """Retorna o padrao de tabulacao até o final da linha."""
    # 0/0/000- 01 02 03 04    06    12       18 19 20 21   |
    #^________^__^__^__^__^^^^__^^^^__^^^^^^^__^__^__^__^^^
    """ Cada ^ é uma ocorrencia de tabulacao, e gera uma sequencia das 
        posicoes na string da tabulação."""
    #tab = [0, 9, 12, 15, 18, 21, 22, 23, 24, 27, 28, 29, 30, 33, 34, 35, 36, 37, 38, 39, 42, 45, 48, 51, 52, 53]
    tab = [str(id) for id, chr in enumerate(line) if chr == ' ']
    return tab


print("Inicio Parsing")
with open('.\data\input.txt', 'r', encoding="utf-8") as f:
    data = f.read()


data = data.splitlines()[1:]

total = len(data)

print(f'{total} linhas lidas')
dict_org = {}
for idx in range(total):
    tab = '.'.join(padrao_tab(data[idx]))
    if tab not in dict_org.keys():
        print(f'{tab} identificada')
        dict_org[tab] = []
    print(f'Linha{idx} com padrao {tab}')
    dict_org[tab].append(idx)

print(f'{len(dict_org.keys())} padroes de tabulacao identificados')

with open('.\data\out.txt', 'w') as f:
    for padrao,linhas in dict_org.items():
        for line in linhas:
            print(data[line], file=f)

print('Fim')
