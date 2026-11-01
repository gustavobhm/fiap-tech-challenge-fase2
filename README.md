# 🚑 Tech Challenge \- Fase 2: Otimização de Rotas Médicas (VRP)

**Pós-Graduação em Inteligência Artificial \- FIAP** *Autor: Gustavo Luis dos Santos*

Este repositório contém a entrega do Projeto 2 (Fase 2\) do Tech Challenge. O objetivo é otimizar rotas de entrega de suprimentos médicos e hospitalares na cidade de São José dos Campos (SP), utilizando Inteligência Artificial, Algoritmos Genéticos e IA Generativa (Google Gemini).

---

## 🎯 1\. O Desafio e a Evolução do Código Base (FIAP TSP para VRP)

Este projeto utilizou como ponto de partida o repositório base de Algoritmos Genéticos para o Caixeiro Viajante (TSP) fornecido pela FIAP. Para adequar o modelo ao contexto realista de logística hospitalar — caracterizado como um **Vehicle Routing Problem (VRP)** —, efetuámos as seguintes evoluções arquiteturais:

* **Classe `City` (Nós Logísticos):** Expandida para suportar atributos de `demanda_caixas` (volume) e `prioridade` (SLA de atendimento).  
* **Classe `Fitness` (Função Objetivo):** Completamente reescrita para incorporar **Hard Constraints**. A função original, que avaliava apenas a distância, aplica agora multas matemáticas severas caso a rota exceda o limite físico do porta-malas dos veículos (20 caixas) ou ultrapasse a autonomia (25 km).

## 🏛️ 2\. Arquitetura da Solução

O ecossistema do projeto foi desenhado de forma linear no Google Colab, dividindo a responsabilidade entre os seguintes componentes:

1. **Modelagem de Dados:** Definição da malha logística de São José dos Campos.  
2. **Motor de Otimização (Algoritmo Genético):** Implementação de Seleção por Torneio, Crossover (OX1) e Mutação para convergência de rotas.  
3. **Validação e Testes:** Execução de suíte `pytest` para validação matemática das restrições.  
4. **Visualização Geoespacial (Folium \+ OSRM):** Geração de mapas interativos baseados na malha viária real e clustering de entregas.  
5. **Automação Operacional (LLM):** Integração com o modelo **Google Gemini 3.8-Flash** para traduzir a saída matemática num Memorando Logístico natural destinado aos motoristas.

## ⚖️ 3\. Comparativo de Desempenho

Para comprovar a eficiência técnica do Algoritmo Genético, implementámos um script comparativo utilizando a heurística tradicional do **Vizinho Mais Próximo (*Nearest Neighbor*)**.

* **Conclusão:** Embora a heurística gulosa seja computacionalmente mais rápida, falha em prever o esgotamento prematuro do porta-malas e frequentemente viola as restrições de autonomia (25 km), resultando em multas pesadas. O Algoritmo Genético conseguiu explorar múltiplos caminhos em simultâneo, garantindo o respeito estrito às *Hard Constraints* e assegurando uma distribuição globalmente otimizada da frota.

## 🧪 4\. Testes Automatizados

O projeto inclui um módulo de testes unitários para garantir a estabilidade das funcionalidades críticas. Os testes foram implementados utilizando a biblioteca `pytest`, validando especificamente:

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

> ⚠️ **Nota de Segurança e Nuvem:** O projeto foi originalmente desenvolvido no Google Colab. Se executar através da nuvem, não é necessário configurar o `venv`. Certifique-se de configurar a sua chave de API do Google Gemini utilizando a funcionalidade **Secrets** do Colab, não expondo as credenciais (`API_KEY`) diretamente no código ou no GitHub.