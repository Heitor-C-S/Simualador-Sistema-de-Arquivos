# relatorios.py

def gerar_arvore(no, prefixo="", is_ultimo=True, is_raiz=True):
    linhas = []
    if is_raiz:
        linhas.append("/")
    else:
        conector = "└── " if is_ultimo else "├── "
        if no.tipo == 'dir':
            linhas.append(f"{prefixo}{conector}{no.nome}/ [DIR]")
        else:
            linhas.append(f"{prefixo}{conector}{no.nome} ({no.tamanho} B) [ARQ]")
            
    if no.tipo == 'dir':
        filhos = list(no.filhos.values())
        total_filhos = len(filhos)
        for i, filho in enumerate(filhos):
            extensao_prefixo = ""
            if not is_raiz:
                extensao_prefixo = "    " if is_ultimo else "│   "
            linhas.extend(gerar_arvore(filho, prefixo + extensao_prefixo, i == total_filhos - 1, False))
    return linhas

def calcular_totais(no, tamanho_bloco):
    real = 0
    alocado = 0
    if no.tipo == 'arq':
        real = no.tamanho
        alocado = len(no.blocos) * tamanho_bloco
        
    for filho in no.filhos.values():
        r, a = calcular_totais(filho, tamanho_bloco)
        real += r
        alocado += a
    return real, alocado
