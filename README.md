# Resolução do Problema da Mochila com Algoritmos Bio-Inspirados

**Equipe:**
- Cristian Prochnow
- Gustavo Dias
- Lucas Willian de Souza Serpa
- Marlon de Souza
- Ryan Gabriel

## Introdução

O problema da mochila é um problema clássico de otimização, onde o objetivo é selecionar um conjunto de itens com pesos e valores conhecidos, para maximizar o valor total sem exceder a capacidade da mochila. Neste projeto, aplicamos **algoritmos bio-inspirados** para resolver esse problema, usando técnicas inspiradas na natureza.

Os algoritmos escolhidos foram:

- **Algoritmo Genético**
- **Colônia de Formigas (Ant Colony Optimization)**
- **Otimização por Enxame de Partículas (Particle Swarm Optimization)**
- **Busca pelo Cúculo (Cuckoo Search)**

Esses algoritmos buscam soluções aproximadas para problemas complexos através de mecanismos estocásticos e iterativos.

---

## Objetivos e Implementação

O objetivo principal é **resolver o problema da mochila** utilizando um dos algoritmos bio-inspirados. O processo inclui:

1. **Modelagem do problema**: Definir uma lista de itens com pesos e valores, e a capacidade da mochila.
2. **Implementação de um algoritmo bio-inspirado**: Escolher um algoritmo (Genético, Colônia de Formigas, PSO ou Cuckoo) e adaptá-lo para o problema.
3. **Avaliação das soluções**: Utilizar uma função de avaliação que penaliza soluções inválidas (caso o peso total ultrapasse a capacidade da mochila).
4. **Testes**: Testar o algoritmo com diferentes conjuntos de itens e capacidades da mochila.

---

## Algoritmos Bio-Inspirados Utilizados

### 1. **Algoritmo Genético (Genetic Algorithm)**

Este algoritmo é inspirado no processo de evolução natural. Ele trabalha com uma **população de soluções**, utilizando operadores como **crossover (cruzamento)**, **mutação** e **seleção natural** para gerar novas soluções em cada iteração.

- **Crossover**: Combina dois indivíduos para gerar uma nova solução.
- **Mutação**: Altera aleatoriamente partes de uma solução para explorar novas áreas do espaço de soluções.
- **Seleção**: Escolhe os melhores indivíduos para reprodução, com base em sua aptidão (qualidade da solução).

### 2. **Colônia de Formigas (Ant Colony Optimization)**

A **colônia de formigas** utiliza um mecanismo de **feromônio** para guiar a busca de soluções. As formigas deixam feromônio ao percorrerem caminhos e, com o tempo, as soluções mais eficazes (com maior feromônio) são mais propensas a serem escolhidas.

- As formigas "exploram" o espaço de soluções em busca da melhor solução.
- As melhores soluções são reforçadas com mais feromônio, o que aumenta a chance de serem replicadas nas próximas gerações.

### 3. **Otimização por Enxame de Partículas (Particle Swarm Optimization)**

Inspirado no comportamento de **enxames de pássaros ou cardumes de peixes**, cada **partícula** representa uma solução no espaço de busca. As partículas ajustam sua posição com base em sua própria experiência e na experiência do melhor indivíduo do grupo.

- As partículas se movem em direção a melhores soluções, ajustando suas "velocidades" a cada iteração.
- Elas também se guiam pelo melhor caminho encontrado até o momento pelo grupo (enxame).

### 4. **Busca pelo Cúculo (Cuckoo Search)**

O algoritmo **Cuckoo Search** é inspirado no comportamento do **cúculo**, um pássaro que deposita seus ovos nos ninhos de outras aves. As "melhores" soluções são trocadas ao longo do tempo, e o algoritmo explora soluções vizinhas para encontrar uma solução ótima.

- A cada iteração, soluções são geradas e avaliadas, com a troca de soluções entre diferentes "ninhos" (indivíduos).
- A busca é guiada por um parâmetro chamado **taxa de troca (PA)**, que determina a frequência com que ocorre a troca de soluções.

---

## Requisitos do Projeto

1. **Modelagem do Problema**:
   - Lista de itens com pesos e valores.
   - Definição da capacidade da mochila.
   - Representação das soluções usando vetores binários (onde 1 indica que o item foi incluído e 0 indica que não foi).

2. **Implementação do Algoritmo**:
   - Funções para gerar soluções, avaliá-las e modificá-las.
   - Aplicação de operadores específicos de cada algoritmo para buscar soluções ótimas.

3. **Avaliação das Soluções**:
   - Penalização de soluções inválidas (onde o peso total ultrapassa a capacidade da mochila).
   - Definição de uma **função de aptidão** clara que atribui um valor à solução, penalizando as soluções inválidas.

4. **Testes e Comparações**:
   - Testar os algoritmos com **conjuntos pequenos de itens** (5 a 10).
   - Testar com **conjuntos grandes de itens** (1.000 e 10.000).
   - Comparar o desempenho dos algoritmos (tempo de execução, qualidade das soluções, etc.).

5. **Comportamento Estocástico**:
   - Devido à natureza estocástica dos algoritmos, **os resultados podem variar** a cada execução. Esse comportamento é esperado e deve ser levado em consideração ao comparar os resultados.

---

## Conclusão

Os algoritmos bio-inspirados proporcionam uma **abordagem robusta e flexível** para resolver o problema da mochila, explorando o espaço de soluções de forma estocástica. Embora os resultados possam variar devido à natureza aleatória dos algoritmos, a adaptação e a avaliação contínua das soluções são fundamentais para obter boas respostas.

Este projeto permite comparar diferentes abordagens para o problema da mochila, com foco no uso de técnicas bio-inspiradas para resolver problemas de otimização complexos.

---

## Testes Realizados

- **Teste com poucos itens (5 a 10)**: Os algoritmos foram testados em cenários pequenos, onde os resultados foram consistentes.
- **Teste com grandes volumes de itens (1.000 e 10.000)**: Os algoritmos foram ajustados para lidar com um maior número de itens, com algumas variações no desempenho.
- **Penalização de soluções inválidas**: As soluções que ultrapassam a capacidade da mochila são penalizadas com uma avaliação de aptidão de 0.

---
