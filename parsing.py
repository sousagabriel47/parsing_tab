"""Parsing Tab."""
import os
import sys

mode = sys.argv


def padrao_tab(line):
    """Retorna o padrao de tabulacao até o final da linha."""
    # 0/0/000- 01 02 03 04    06    12       18 19 20 21   |
    #^________^__^__^__^__^^^^__^^^^__^^^^^^^__^__^__^__^^^
    """ Cada ^ é uma ocorrencia de tabulacao, e gera uma sequencia das 
        posicoes na string da tabulação."""
    #tab = [0, 9, 12, 15, 18, 21, 22, 23, 24, 27, 28, 29, 30, 33, 34, 35, 36, 37, 38, 39, 42, 45, 48, 51, 52, 53]
    tab = [str(id) for id, chr in enumerate(line) if chr == ' ']
    # tab_str = ['X'] * len(line)
    # for ch in tab:
    #     tab_str[int(ch)] = ' '
    tab_str = '.'.join(tab)
    return tab_str

def gera_nome(tab_str):
    """Gera o nome do arquivo."""
    count = 0
    seq = []
    for ch in range(len(tab_str)-1):
        if tab_str[ch] == ' ' and tab_str[ch+1] == ' ':
            if count:
                seq.append(count)
                count = 0
        elif tab_str[ch] == ' ':
            count += 1
    if count:
        seq.append(count)
    return '_'.join([str(s) for s in seq])

if len(sys.argv) > 1:
    mode = sys.argv[1]
else:
    mode = 'onefile'

print("Inicio Parsing")
with open('.\data\in.txt', 'r', encoding="utf-8") as f:
    data = f.read()


data = data.splitlines()[1:]

total = len(data)

print(f'{total} linhas lidas')
dict_org = {}
for idx in range(total):
    tab = padrao_tab(data[idx])
    if tab not in dict_org.keys():
        #print(f'{tab} identificada')
        dict_org[tab] = []
    #print(f'Linha{idx} com padrao {tab}')
    dict_org[tab].append(idx)

print(f'{len(dict_org.keys())} padroes de tabulacao identificados')
tLinhas = 0
nomes = {}

if mode == 'onefile':
    with open(f'.\data\out\\tabulacao.txt', 'w') as f:
        for linhas in dict_org.values():
            for line in linhas:
                print(data[line], file=f)
                tLinhas += 1
elif mode == 'folder':
    for padrao,linhas in dict_org.items():
        nome = data[linhas[0]][1:]
        #print(nome)

        with open(f'.\data\out\{nome}.txt', 'w') as f:
            for line in linhas:
                print(data[line], file=f)
                tLinhas += 1

print(f'Fim: {tLinhas} separadas')

# for nome,padroes in nomes.items():
#     with open(f'.\data\out_p\{len(padroes)}-{nome}.txt', 'a') as f:
#         for line in padroes:
#             print(line, file=f)
