# Simulador de Sistema de Arquivos 

## Comandos basicos:
1. `mkdir <nome_do_diretorio>`
2. `create <caminho+nome_do_arquivo> --size <tamanho_do_arquivo>`
3. `fs_status --detalhes`

Importante para utilização adequada do programa: 

1 - O comando mkdir pode apenas criar um diretorio por vez. Para criar um diretorio dentro de outro diretorio, é necessário citar quem é o pai, em ordem.
Exemplo: 1. `mdkir downloads` ; 2. `mkdir donwloads/jogos`. 
Caso não seja esta a ordem de execução, o argumento não será lido adequadamente e não será criado nenhum dos dois diretórios.

2 - O comando create NECESSÁRIAMENTE precisa do caminho inteiro para o arquivo, junto como o arquivo. A tag --size também é necessária para declarar qual será o tamanho do arquivo.
Exemplo: `create donwloads/jogos/jogo-da-velha.exe --size 30kb`. 
Não é possível receber espaços no nome, portanto, é necessário ter '-' ou '_' em cada lugar que seria espaço vazio.

3. O comando fs_status pode ou não receber a tag `--detalhes`. A tag serve para mostrar mais detalhadamente o contexto dos blocos, fragmentação, necessidade de compactação, etc... Se não, mostrará apenas a árvore do sistema, tamanho do bloco de disco e o total de blocos (com o total de bytes).

--- 
### por Heitor Santana
