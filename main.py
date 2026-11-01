import sys 

def parse_tamanho(tamanho_str): 
    tamanho_str = tamanho_str.upper()
    if tamanho_str.endswith("KB"):
        return int(tamanho_str.replace("KB", "")) * 1024
    elif tamanho_str.endswith("B"):
        return int(tamanho_str.replace("B",""))
    return int(tamanho_str) #caso não tenha nenhum sufixo escrito

def iniciar_cli():
    em_andamento = "Em andamento..."

    print("===== CLI - Sistema de Arquivos =====")
    print("Comandos disponíveis: mkdir, create, fs_status, exit\n")

    while True:
        try:
            entrada = input("> ").strip()
            if not entrada:
                continue
            partes = entrada.split()
            comando = partes[0].lower()

            # Comando 1 - exit
            if comando == 'exit' or comando == 'quit':
                print("Encerrando simulador...")
                sys.exit(0)
            
            # Comando 2 - mkdir
            elif comando == 'mkdir':
                if len(partes) < 2:
                    print("Uso correto: >mkdir <caminho> (ex.: mkdir downloads)")
                    continue
                caminho = partes[1]
                # TODO: criar funcao mkdir
                print(em_andamento)
                
            # Comando 3 - create
            elif comando == 'create':
                if len(partes) < 4 or partes[2] != '--size':
                    print("Uso correto: >create <caminho> --size <tamanho> (ex.: create downloads/texto.txt --size 120B)")
                    continue
                
                caminho = partes[1]
                tamanho_bytes = parse_tamanho(partes[3])
                
                # TODO: implementar funcao de criar arquivo (precisa de um caminho antes)
                print(em_andamento)

            # Comando 4 - fs_status
            elif comando == 'fs_status':
                detalhes = True if '--detalhes' in partes else False

                # TODO: implementar mapa do disco e a arvore
                print(em_andamento)

            else:
                print(f"Comando desconhecido ou invalido: {comando}")
                
        except Exception as e:
            # O print precisa estar indentado dentro do except
            print(f"Erro ao processar comando: {e}")

if __name__ == "__main__":
    iniciar_cli()
