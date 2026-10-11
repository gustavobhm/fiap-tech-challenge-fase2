# 🚚 Otimização de Rotas Logísticas (VRP) com IA

> **Projeto 2 - Tech Challenge (Fase 2)** | Pós-Graduação em Inteligência Artificial - FIAP

Este projeto resolve um Problema de Roteamento de Veículos (VRP) complexo para a distribuição de insumos médicos em São José dos Campos (SP), utilizando Computação Evolutiva e Inteligência Artificial Generativa.

## 🎯 O Desafio
Otimizar a logística de entrega a partir de um Hospital Central para 5 destinos distintos (Unidades de Saúde e Residências), respeitando rigorosas *Hard Constraints*:
* **Capacidade da Frota:** Máximo de 20 caixas por veículo.
* **Autonomia:** Limite máximo de 25 km por rota.
* **SLA (Service Level Agreement):** Prioridade absoluta para locais com nível de urgência 'Alta'.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Motor Matemático:** Algoritmo Genético (Seleção por Torneio, Crossover OX1, Mutação Swap).
* **Roteamento em Malha Viária (API):** Open Source Routing Machine (OSRM) via `requests` e `polyline`.
* **Visualização Geográfica:** `Folium` (com *clustering* e ícones personalizados).
* **IA Generativa (LLM):** Google Gemini 3.8-flash (via `google.generativeai`).

## 🚀 Destaques da Arquitetura
1. **Função Fitness Otimizada:** O modelo não busca apenas a menor distância, mas **penaliza matematicamente** rotas que atrasem entregas prioritárias ou que estourem os limites de capacidade e autonomia da frota.
2. **Roteamento Real (OSRM):** O traçado não utiliza aproximações em linha reta (distância euclidiana). A solução consulta a malha viária real de São José dos Campos, respeitando sentidos de via e traçados reais.
3. **Comunicação Automatizada:** Os resultados otimizados são processados pela IA Generativa do Gemini, que elabora automaticamente um Memorando Operacional e de Segurança completo para os motoristas.

## 📁 Estrutura do Repositório
* `/src`: Códigos fonte (Script `.py` e Jupyter Notebook).
* `/docs`: Relatório Técnico exigido pelo edital.
* `/assets`: Mapas HTML interativos e capturas de tela.

## ⚙️ Como Executar
1. Clone este repositório.
2. Instale as dependências: `pip install folium polyline google-generativeai requests`
3. Substitua a variável `API_KEY` pela sua chave válida do Google Gemini no script principal.
4. Execute o script `projeto_2_otimizacao_rotas_v4.py`.
