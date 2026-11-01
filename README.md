# 🚑 Tech Challenge \- Fase 2: Otimização de Rotas Médicas (VRP)

**Pós-Graduação em Inteligência Artificial \- FIAP** *Autor: Gustavo Luis dos Santos*

Este repositório contém a entrega do Projeto 2 (Fase 2\) do Tech Challenge. O objetivo é otimizar rotas de entrega de suprimentos médicos e hospitalares na cidade de São José dos Campos (SP), utilizando Inteligência Artificial, Algoritmos Genéticos e IA Generativa (Google Gemini).

---

## 🎯 1\. O Desafio e a Evolução do Código Base (FIAP TSP para VRP)

Este projeto utilizou como ponto de partida o repositório base de Algoritmos Genéticos para o Caixeiro Viajante (TSP) fornecido pela FIAP. Para adequar o modelo ao contexto realista de logística hospitalar — caracterizado como um **Vehicle Routing Problem (VRP)** —, efetuámos as seguintes evoluções arquiteturais:

* **Classe `City` (Nós Logísticos):** Expandida para suportar atributos de `demanda_caixas` (volume) e `prioridade` (SLA de atendimento).  
* **Classe `Fitness` (Otimização Multiobjetivo):** Completamente reescrita utilizando o *Penalty Method*. A função aplica multas matemáticas exponenciais caso o cromossomo (rota) exceda os limites físicos do porta-malas dos veículos (20 caixas) ou ultrapasse a autonomia (25 km), atuando como **Hard Constraints**.

## 🏗️ 2\. Arquitetura da Solução (10 Blocos)

O ecossistema do projeto foi estruturado no Google Colab, dividindo a responsabilidade em 10 blocos sequenciais:

1. **Modelagem de Dados e POO:** Definição da malha logística de São José dos Campos.  
2. **Função Fitness:** Avaliação de aptidão e aplicação de *Hard Penalties*.  
3. **Motor Genético (Metaheurística):** Seleção por Torneio, Crossover OX1 (Order 1\) e Mutação Dinâmica.  
4. **Validação (Test-Driven Validation):** Execução de suíte `pytest` para validação matemática autônoma das restrições.  
5. **Benchmark Heurístico:** Comparação de performance provando a superioridade do Genético frente à heurística gulosa do Vizinho Mais Próximo (*Nearest Neighbor*).  
6. **Validação Topológica:** Visualização gráfica vetorial (plano cartesiano) comprovando a integridade das sub-rotas.  
7. **Projeção Geoespacial (Folium):** Execução de *Clustering Espacial* não-supervisionado em mapa interativo.  
8. **Roteamento de Malha Viária (OSRM):** Integração com Open Source Routing Machine para navegação baseada no asfalto real, sentidos e avenidas.  
9. **Integração de LLM (Google Gemini):** Uso de *Prompt Engineering* para traduzir matrizes numéricas num Memorando Operacional natural destinado aos motoristas, contando com arquitetura de resiliência (Fallback).  
10. **Compilação Executiva (Data Storytelling):** Geração 100% automatizada do Relatório Técnico Oficial em PDF utilizando `Selenium` e `ReportLab`.

## ⚖️ 3\. Comparativo de Desempenho

O Benchmark provou que a heurística gulosa falha em prever o esgotamento prematuro do porta-malas e frequentemente viola as restrições de autonomia, resultando em rotas impossíveis. O Algoritmo Genético, com sua visão global do grafo, conseguiu explorar múltiplos caminhos em simultâneo, garantindo o respeito estrito às *Hard Constraints* e assegurando uma distribuição otimizada da frota.

## 🧪 4\. Quality Assurance (Testes Automatizados)

A lógica crítica foi blindada através de testes unitários (`pytest`), validando especificamente:

* Cálculo correto das distâncias euclidianas.  
* Aplicação estrita da penalização de capacidade (máx. 20 caixas).  
* Aplicação estrita da penalização de autonomia (máx. 25 km).

## ⚙️ 5\. Configuração do Ambiente e Execução

Para garantir o isolamento das dependências, este projeto utiliza o ambiente virtual padrão do Python (`venv`). Siga os passos abaixo para correr o projeto localmente:

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

*(Nota: Para gerar o PDF e os mapas em imagem localmente, é necessário ter o Google Chrome e ChromeDriver configurados. No Colab, esta etapa foi automatizada no Bloco 10).*

> ⚠️ **Nota de Segurança e Nuvem:** O projeto foi originalmente orquestrado no Google Colab. Se executar através da nuvem, não é necessário configurar o `venv`. Certifique-se de configurar a sua chave de API do Google Gemini utilizando a funcionalidade **Secrets** do Colab (`GEMINI_API_KEY`), nunca expondo as credenciais diretamente no código-fonte.