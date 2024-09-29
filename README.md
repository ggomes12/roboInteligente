<h1 style="text-align: center;"> robo-inteligente-limpeza </h1>

- O objetivo deste projeto é simular o comportamento de um robô inteligente que utiliza algoritmos de busca em profundidade (DFS) para limpar uma área,
evitando obstáculos e garantindo que todas as células disponíveis sejam limpas.

## Descrição do Projeto

- Este projeto simula o comportamento de um robô que se move por uma matriz 2D, limpando as células disponíveis e evitando obstáculos.
O robô segue uma sequência lógica de limpeza utilizando busca em profundidade (DFS) para garantir que todas as áreas acessíveis sejam
limpas sem passar por obstáculos.

## Estrutura do Projeto
A estrutura do projeto está organizada da seguinte forma:

- Arquivo roboInteligente.py

O arquivo principal do projeto contém a lógica da simulação incluindo a:

    - geração da matriz, 

    - movimentação do robô,

    - visualização do progresso da limpeza. 

Abaixo estão os principais métodos:

**gerar_tabela(linhas, colunas, obstaculos)**

    Este método gera uma matriz 2D representando o ambiente de limpeza do robô. Os valores da matriz indicam:

    0: Obstáculos (áreas inacessíveis)
    1: Células disponíveis para limpeza
    2: Ponto de início do robô

    Parâmetros:

    linhas: Número de linhas da matriz.
    colunas: Número de colunas da matriz.
    obstaculos: Número de células que serão obstáculos.

**gerar_figura(matriz, titulo="", figura=None, eixos=None)**

    Este método utiliza a biblioteca matplotlib para gerar uma visualização gráfica da matriz em tempo real, 
    com diferentes cores para células limpas, disponíveis e obstáculos. O progresso do robô é exibido 
    conforme ele limpa as células.

**movimentar_robo(matriz, inicio)**

    Este método realiza a movimentação do robô utilizando o algoritmo de busca em profundidade (DFS). 
    O robô começa a partir do ponto inicial (valor 2 na matriz) e se move em sequência, limpando uma 
    célula de cada vez. Se encontrar um obstáculo ou o fim de uma linha, ele continua a busca em outras direções.

    A movimentação é restrita a quatro direções: frente, trás, esquerda e direita. O robô limpa uma 
    célula por vez e usa as células já limpas para continuar a busca por áreas disponíveis.

**encontrar_inicio(matriz)**

    Este método encontra a posição inicial do robô, ou seja, a célula que contém o valor 2. 
    Ele retorna as coordenadas (x, y) dessa posição na matriz.
    
**Como Executar**

## Para executar o projeto, siga os passos abaixo:

- Clone o repositório:

```
$ git clone https://github.com/ggomes12 roboInteligente.git
```


## Instale as dependências: 
- Este projeto utiliza a biblioteca matplotlib para visualização gráfica e random para gerar os obstáculos.
  Instale o matplotlib com o comando:

```
$ pip install matplotlib
```

## Execute o projeto:

```
$ python roboInteligente.py
```

## Interaja com o programa: 
Ao iniciar o programa, você será solicitado a inserir o:

- número de linhas,
- colunas e a
- quantidade de obstáculos na matriz.
  
O robô então iniciará a simulação, limpando as células disponíveis e exibindo o progresso em tempo real.

## Exemplo de Uso

- Ao rodar o programa, insira os seguintes valores de exemplo:

    Quantidade de linhas: 10

    Quantidade de colunas: 10

    Quantidade de obstáculos: 20

- O robô começará a simulação a partir de uma célula aleatória e limpará toda a matriz, evitando os obstáculos.
