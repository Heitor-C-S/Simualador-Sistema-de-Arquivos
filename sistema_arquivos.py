# sistema_arquivos.py
import math
from relatorios import gerar_arvore, calcular_totais

#Constantes
TAMANHO_BLOCO = 4096
TOTAL_BLOCOS = 16

class Node:
    def __init__(self, nome, tipo='dir'):
        self.nome = nome
        self.tipo = tipo  # dir para pasta, arq para arquivo.
        self.filhos = {} # apenas serve para dir, sera o dicionario de filhos.
        self.tamanho = 0 
        self.blocos = []

class FileSystem:
    def __init__(self):
        self.raiz = Node("/", tipo='dir')  #a raiz do sistema sempre existe ("/")
        self.disco = [None] * TOTAL_BLOCOS

    # --- FUNCAO 1: MKDIR --- #
    def mkdir(self, caminho):
        partes = [p for p in caminho.split('/')if p] # basicamente transforma: "sistema/logs" em ['sistema', 'logs']. facilita demais a vida.
        if not partes:
            return "Erro: Caminho invalido.\n"
        
        atual = self.raiz

        for parte in partes[:-1]:
            if parte in atual.filhos and atual.filhos[parte].tipo == 'dir':
                atual = atual.filhos[parte]
            else:
                return f"Erro: O diretorio pai para {parte} nao existe.\n"

        novo_dir = partes[-1]

        if novo_dir in atual.filhos:
            return f"Erro: '{novo_dir}' ja existe.\n"
        
        atual.filhos[novo_dir] = Node(novo_dir, tipo='dir')
        return f"Diretorio '{caminho}' criado com sucesso.\n"


    # --- FUNCAO 2: CREATE --- #
    def create(self, caminho, tamanho_bytes):
        partes = [p for p in caminho.split('/') if p]
        if not partes:
            return "Erro: Caminho invalido.\n"

        atual = self.raiz
        # Navega ate o diretório pai (igual no mkdir)
        for parte in partes[:-1]:
            if parte in atual.filhos and atual.filhos[parte].tipo == 'dir':
                atual = atual.filhos[parte]
            else:
                return f"Erro: O diretorio pai para '{parte}' nao existe.\n"

        nome_arquivo = partes[-1]
        if nome_arquivo in atual.filhos:
            return f"Erro: '{nome_arquivo}' ja existe. \n"

        #parte 1 da logica: quantos blocos serao necessarios (arredondando para CIMA)
        blocos_necessarios = math.ceil(tamanho_bytes / TAMANHO_BLOCO)


        if blocos_necessarios == 0: 
            blocos_necessarios = 1
        
        #parte 2: verificar onde tem espaco livre no array do disco
        blocos_livres = [i for i, b in enumerate(self.disco) if b is None]

        if len(blocos_livres) < blocos_necessarios:
            return f"Erro: Espaco em disco insuficiente. Necessario: {blocos_necessarios}, Livres: {len(blocos_livres)} .\n"

        #parte 3: pega exatamente a qtd de blocos necessarios
        blocos_alocados= blocos_livres[:blocos_necessarios]
        
        #parte 4: alocar no disco
        for i in blocos_alocados:
            self.disco[i] = caminho

        #parte 5: Cria o node do arquivo na arvore de diretorios
        novo_arquivo = Node(nome_arquivo, tipo='arq')
        novo_arquivo.tamanho = tamanho_bytes
        novo_arquivo.blocos = blocos_alocados

        atual.filhos[nome_arquivo] = novo_arquivo

        return f" Arquivo '{nome_arquivo}' criado com sucesso. Esta ocupando {blocos_necessarios} bloco(s)."

    # --- FUNCAO 3: FS_STATUS --- #
    def fs_status(self, detalhes=False):
        saida = ["\n[ÁRVORE DO SISTEMA DE ARQUIVOS]"]
        
        # Usa a função externa passando a raiz
        saida.extend(gerar_arvore(self.raiz))
        
        saida.append(f"\nTamanho do Bloco de Disco: {TAMANHO_BLOCO} B | Total de Blocos: {TOTAL_BLOCOS} ({TOTAL_BLOCOS * TAMANHO_BLOCO} B)")
        
        if detalhes:
            saida.append("\n[MAPA DE ALOCAÇÃO DO DISCO (Indexado)]")
            for i, b in enumerate(self.disco):
                if b is None:
                    saida.append(f"Bloco {i:02d} : [LIVRE]")
                else:
                    saida.append(f"Bloco {i:02d} : [OCUPADO] -> '{b}'")
                    
            saida.append("\n--- RELATÓRIO DE FRAGMENTAÇÃO ---")
            
            # Usa a função externa passando a raiz e a constante do tamanho do bloco
            tamanho_real, tamanho_alocado = calcular_totais(self.raiz, TAMANHO_BLOCO)
            frag_interna = tamanho_alocado - tamanho_real
            
            saida.append(f"Tamanho Real dos Arquivos : {tamanho_real} bytes")
            saida.append(f"Espaço Alocado no Disco   : {tamanho_alocado} bytes")
            saida.append(f"Fragmentação Interna      : {frag_interna} bytes (Desperdício dentro dos blocos)")
            saida.append("Fragmentação Externa      : 0 bytes")
            saida.append("Necessidade de Compactação: NÃO (Blocos são mapeados livremente pelo i-node/índice)")
            
        return "\n".join(saida) + "\n"
