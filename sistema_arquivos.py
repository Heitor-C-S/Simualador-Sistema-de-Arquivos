# sistema_arquivos.py

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
            return f"Erro: '{novo_dir} ja existe."
        
        atual.filhos[novo_dir] = Node(novo_dir, tipo='dir')
        return f"Diretorio '{caminho}' criado com sucesso."


