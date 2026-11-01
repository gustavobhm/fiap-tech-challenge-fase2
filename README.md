# 🚑 Tech Challenge \- Fase 2: Otimização de Rotas Médicas (VRP)

**Pós-Graduação em Inteligência Artificial \- FIAP** *Autor: Gustavo Luis dos Santos*

Este repositório contém a entrega do Projeto 2 (Fase 2\) do Tech Challenge. O objetivo é otimizar rotas de entrega de suprimentos médicos e hospitalares na cidade de São José dos Campos (SP), utilizando Inteligência Artificial, Algoritmos Genéticos e IA Generativa (Google Gemini).

---

## 🎯 1\. O Desafio e a Evolução do Código Base (FIAP TSP para VRP)

Este projeto utilizou como ponto de partida o repositório base de Algoritmos Genéticos para o Caixeiro Viajante (TSP) fornecido pela FIAP. Para adequar o modelo ao contexto realista de logística hospitalar — caracterizado como um **Vehicle Routing Problem (VRP)** —, efetuámos as seguintes evoluções arquiteturais:

* **Classe `City` (Nós Logísticos):** Expandida para suportar atributos de `demanda_caixas` (volume) e `prioridade` (SLA de atendimento).  
* **Classe `Fitness` (Otimização Multiobjetivo):** Completamente reescrita utilizando o *Penalty Method*. A função atua como **Hard Constraints**, aplicando multas matemáticas caso o cromossomo exceda a capacidade do porta-malas (20 caixas), a autonomia (25 km) ou atrase entregas de Prioridade Alta.

## 🏗️ 2\. Arquitetura da Solução (11 Blocos)

O ecossistema do projeto foi estruturado no Google Colab, dividindo a responsabilidade em 11 blocos sequenciais:

1. **Modelagem de Dados e POO:** Definição da malha logística de São José dos Campos.  
2. **Função Fitness:** Avaliação de aptidão e aplicação de *Hard Penalties* (SLA, Capacidade e Autonomia).  
3. **Motor Genético (Metaheurística):** Seleção por Torneio, Crossover OX1 (Order 1\) e Mutação Dinâmica.  
4. **Validação (Test-Driven Validation):** Execução de suíte `pytest` para validação matemática autônoma.  
5. **Benchmark Heurístico:** Comparação de performance provando a superioridade do Genético frente à heurística do Vizinho Mais Próximo (*Nearest Neighbor*).  
6. **Validação Topológica:** Visualização gráfica vetorial (plano cartesiano) das sub-rotas.  
7. **Projeção Geoespacial (Folium):** Execução de *Clustering Espacial* não-supervisionado em mapa interativo.  
8. **Roteamento de Malha Viária (OSRM):** Navegação baseada no asfalto real, sentidos e avenidas.  
9. **Integração de LLM (Google Gemini):** Uso de *Prompt Engineering* com Fallback/Cache para gerar um Memorando Operacional para motoristas e um Relatório de Eficiência Logística.  
10. **Chatbot Interativo (Q\&A):** Interface de linha de comando em Linguagem Natural para o gestor interagir com a IA sobre as rotas.  
11. **Compilação Executiva (Data Storytelling):** Geração automatizada do Relatório Técnico Oficial em PDF utilizando `Selenium` e `ReportLab`.

## ⚖️ 3\. Comparativo de Desempenho

O Benchmark provou que a heurística gulosa falha em prever o esgotamento prematuro do porta-malas e frequentemente viola as restrições, resultando em rotas impossíveis. O Algoritmo Genético conseguiu explorar múltiplos caminhos em simultâneo, garantindo o respeito estrito às *Hard Constraints* e assegurando uma distribuição otimizada.

## 🧪 4\. Quality Assurance (Testes Automatizados)

A lógica crítica foi blindada através de testes unitários (`pytest`), validando:

* Cálculo correto das distâncias euclidianas.  
* Aplicação da penalização de capacidade (máx. 20 caixas).  
* Aplicação da penalização de autonomia (máx. 25 km).

## ⚙️ 5\. Configuração do Ambiente e Execução

Para garantir o isolamento das dependências, este projeto utiliza o ambiente virtual padrão do Python (`venv`). Siga os passos abaixo:

1. **Clonar o repositório:**

```sh
git clone https://github.com/gustavobhm/fiap-tech-challenge-fase2.git
cd fiap-tech-challenge-fase2
```

2. **Criar e ativar o ambiente virtual:**  
* No Windows:

```sh
python -m venv venv
venv\Scripts\activate
```

* No Linux/macOS:

```sh
python -m venv venv
source venv/bin/activate
```

3. **Instalar as dependências:**

```sh
pip install -r requirements.txt
```

> ⚠️ **Nota de Segurança:** Configure a sua chave de API do Google Gemini utilizando a funcionalidade **Secrets** do Colab (`GEMINI_API_KEY`), nunca expondo as credenciais diretamente no código-fonte.