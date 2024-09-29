import random
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import time


# Gerar matriz
def gerar_tabela(linhas, colunas, obstaculos):
    total_casas = linhas * colunas
    disponiveis = total_casas - obstaculos - 1
    valores = [0] * obstaculos + [1] * disponiveis + [2]  # 0: obstáculo, 1: disponível, 2: ponto de início

    random.shuffle(valores)

    if obstaculos > total_casas - 1:
        print("Não é possível essa quantidade de obstáculos.")
        exit(1)

    matriz = []
    for i in range(linhas):
        indice_inicial = i * colunas
        indice_final = (i + 1) * colunas
        linha_atual = valores[indice_inicial:indice_final]
        matriz.append(linha_atual)

    return matriz



# Gerar visualização
def gerar_figura(matriz, titulo="", figura=None, eixos=None):
    if figura is None or eixos is None:
        figura, eixos = plt.subplots()

    # prepara a vizualização da figura com cores e linhas
    cmap = mcolors.ListedColormap(['black', 'brown', 'green', 'blue'])  
    eixos.clear()  
    eixos.imshow(matriz, cmap=cmap)
    
    eixos.set_xticks([x - 0.5 for x in range(1, len(matriz[0]) + 1)])
    eixos.set_yticks([y - 0.5 for y in range(1, len(matriz) + 1)])
    eixos.grid(color='white', linestyle='-', linewidth=1)
    
    eixos.set_xticklabels([])
    eixos.set_yticklabels([])

    plt.title(titulo)
    figura.canvas.draw()
    figura.canvas.flush_events()  # Atualiza a figura em tempo real
    
    
    

# Movimentação do robô com DFS (em profundidade)
def movimentar_robo(matriz, inicio):
    linhas = len(matriz)
    colunas = len(matriz[0])
    pilha = [(inicio[0], inicio[1])]  # Pilha para DFS
    visitados = set()  # Conjunto para acompanhar as células visitadas
    matriz[inicio[0]][inicio[1]] = 3  # Marca o ponto de partida como limpo

    plt.ion()  # Habilita modo interativo do Matplotlib
    figura, eixos = plt.subplots()

    gerar_figura(matriz, "Início da limpeza", figura, eixos)
    time.sleep(0.5)  # Pausa para visualizar alimpeza

    while pilha:
        x, y = pilha.pop()  # Pega o último elemento da pilha (busca em profundidade)
        
        if (x, y) not in visitados:  # Verifica se já foi visitado
            visitados.add((x, y))  # Marca como visitado
            matriz[x][y] = 3  # Marca como limpo
            gerar_figura(matriz, f"Limpeza em ({x}, {y})", figura, eixos)
            time.sleep(0.5)  # Simula o tempo de limpeza

            # Movimentação nas quatro direções: direita, baixo, esquerda, cima
            direcoes = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            
            for dx, dy in direcoes:
                novo_x, novo_y = x + dx, y + dy
                # Verifica se está dentro dos limites, não é obstáculo e não foi visitado
                if 0 <= novo_x < linhas and 0 <= novo_y < colunas and matriz[novo_x][novo_y] == 1:
                    pilha.append((novo_x, novo_y))  # Adiciona à pilha para continuar a exploração

    plt.ioff()  # Desabilitar modo interativo
    plt.show()  # Garantir que a última figura permaneça aberta
    
    

# Encontrar a posição inicial do robô (onde está o valor 2)
def encontrar_inicio(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 2:
                return (i, j)
    return None



# Parâmetros
numero_linhas = int(input("Quantidade de linhas: "))
numero_colunas = int(input("Quantidade de colunas: "))
quantidade_obstaculos = int(input("Quantidade de obstáculos: "))



# Gerar matriz e iniciar simulação
matriz = gerar_tabela(numero_linhas, numero_colunas, quantidade_obstaculos)
inicio = encontrar_inicio(matriz)



if inicio:
    movimentar_robo(matriz, inicio)
else:
    print("Erro: Não foi possível encontrar o ponto de início (valor 2)")

