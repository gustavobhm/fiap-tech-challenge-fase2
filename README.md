<div>
  <h1>🚑 FIAP Tech Challenge - Fase 2: Otimização de Rotas Hospitalares (VRP)</h1>
  
  <p>
    <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&amp;logo=python&amp;logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/Google_Colab-F9AB00?style=for-the-badge&amp;logo=googlecolab&amp;logoColor=white" alt="Colab">
    <img src="https://img.shields.io/badge/Google_Gemini-8E75B2?style=for-the-badge&amp;logo=googlegemini&amp;logoColor=white" alt="Gemini">
    <img src="https://img.shields.io/badge/Folium_Mapas-77B829?style=for-the-badge&amp;logo=leaflet&amp;logoColor=white" alt="Folium">
    <img src="https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&amp;logo=pytest&amp;logoColor=white" alt="Pytest">
    <img src="https://img.shields.io/badge/Status-Conclu%C3%ADdo-success?style=for-the-badge" alt="Status">
  </p>

  <p><strong>Desenvolvido por:</strong> Gustavo Luis dos Santos | Pós-Graduação em Inteligência Artificial - FIAP</p>
  
  <p>Este repositório contém a solução desenvolvida para a <strong>Fase 2 do Tech Challenge</strong> da Pós-Graduação em Inteligência Artificial da FIAP. O projeto resolve um problema realístico de <strong>Roteamento de Veículos (VRP - Vehicle Routing Problem)</strong> voltado para a logística de distribuição de medicamentos termolábeis e insumos médicos críticos em São José dos Campos (SP), integrando Metaheurísticas Evolutivas (Algoritmos Genéticos), roteamento viário geoespacial (OSRM + Folium), testes automatizados (Pytest) e Inteligência Artificial Generativa (Google Gemini).</p>

  <hr>

  <h2>📑 Índice</h2>
  <ol>
    <li><a href="#1-evolução-do-código-base-fiap-tsp-para-vrp-hospitalar">🧬 Evolução do Código Base (FIAP TSP para VRP Hospitalar)</a></li>
    <li><a href="#2-tecnologias-utilizadas">💻 Tecnologias Utilizadas</a></li>
    <li><a href="#3-arquitetura-do-sistema-11-blocos-modulares">🏗️ Arquitetura do Sistema (11 Blocos Modulares)</a></li>
    <li><a href="#4-restrições-rígidas-hard-constraints-e-função-fitness">🛡️ Restrições Rígidas (Hard Constraints) e Função Fitness</a></li>
    <li><a href="#5-comparativo-de-desempenho-algoritmo-genético-vs-vizinho-mais-próximo">⚖️ Comparativo de Desempenho (Algoritmo Genético vs. Vizinho Mais Próximo)</a></li>
    <li><a href="#6-integração-com-ia-generativa-llm">🤖 Integração com IA Generativa (LLM)</a></li>
    <li><a href="#7-configuração-do-ambiente-e-como-executar">🚀 Configuração do Ambiente e Como Executar</a></li>
    <li><a href="#8-estrutura-do-repositório">📁 Estrutura do Repositório</a></li>
    <li><a href="#9-vídeo-de-demonstração">🎥 Vídeo de Demonstração</a></li>
  </ol>

  <hr>

  <h2 id="1-evolução-do-código-base-fiap-tsp-para-vrp-hospitalar">🧬 1. Evolução do Código Base (FIAP TSP para VRP Hospitalar)</h2>
  <p>O projeto partiu da implementação clássica de Algoritmos Genéticos para o Problema do Caixeiro Viajante (TSP) fornecida pela FIAP e foi integralmente refatorado para suportar múltiplos veículos e regras reais de operação hospitalar (VRP):</p>
  <ul>
    <li><strong>Expansão da Classe City:</strong> Inclusão dos atributos operacionais <code>demanda_caixas</code> (volume ocupado no veículo), <code>prioridade</code> (nível de criticidade / SLA da entrega) e coordenadas geográficas reais de unidades de saúde em São José dos Campos.</li>
    <li><strong>Refatoração da Classe Fitness:</strong> Transição do cálculo de rota única para decomposição automática em múltiplas viagens com retorno obrigatório ao depósito central (Hospital Base) e aplicação do <em>Penalty Method</em> para restrições operacionais severas.</li>
  </ul>

  <hr>

  <h2 id="2-tecnologias-utilizadas">💻 2. Tecnologias Utilizadas</h2>
  <ul>
    <li><strong>Linguagem Base:</strong> Python 3.10+</li>
    <li><strong>Otimização e Manipulação de Dados:</strong> Algoritmos Genéticos (Crossover OX1, Seleção por Torneio, Elitismo), NumPy, Pandas</li>
    <li><strong>Roteamento Geoespacial e Mapas:</strong> Folium, OSRM API (Open Source Routing Machine), Matplotlib</li>
    <li><strong>Inteligência Artificial Generativa:</strong> Google Gemini (<code>google-genai</code> SDK)</li>
    <li><strong>Geração de Relatórios Executivos (PDF):</strong> ReportLab, Selenium, Pillow</li>
    <li><strong>Qualidade de Software (QA):</strong> Pytest</li>
  </ul>

  <hr>

  <h2 id="3-arquitetura-do-sistema-11-blocos-modulares">🏗️ 3. Arquitetura do Sistema (11 Blocos Modulares)</h2>
  <p>O pipeline está organizado em 11 blocos sequenciais e independentes:</p>
  <ul>
    <li><strong>Blocos 1 a 3 (Modelagem POO e Motor Genético):</strong> Definição das classes <code>City</code> e <code>Fitness</code>, geração da população inicial, seleção por torneio, operador de cruzamento <em>Order Crossover</em> (OX1) e mutação controlada.</li>
    <li><strong>Bloco 4 (Testes Automatizados - QA):</strong> Suíte de testes unitários com <code>pytest</code> para validar a integridade matemática das restrições de capacidade, autonomia e penalidades antes da otimização.</li>
    <li><strong>Bloco 5 (Benchmark Heurístico):</strong> Implementação do algoritmo guloso do Vizinho Mais Próximo (<em>Nearest Neighbor</em>) para comparação direta de desempenho e custo.</li>
    <li><strong>Blocos 6 a 8 (Convergência e Mapeamento Viário Real):</strong> Execução evolutiva do Algoritmo Genético, plotagem Euclidiana dos clusters e renderização interativa sobre as ruas e avenidas reais de São José dos Campos via API OSRM e Folium.</li>
    <li><strong>Bloco 9 (Relatórios Inteligentes com Gemini):</strong> Geração automatizada do Memorando Operacional (para motoristas) e do Relatório de Eficiência (para a diretoria) utilizando o modelo <code>gemini-3.8-flash</code> via SDK <code>google-genai</code>, com mecanismo de contingência (<em>fallback</em>) para erros de cota ou indisponibilidade (HTTP 429/503).</li>
    <li><strong>Bloco 10 (Chatbot Logístico de Q&A):</strong> Assistente conversacional alimentado em tempo real pelos dados das rotas otimizadas para responder a dúvidas operacionais e de SLA.</li>
    <li><strong>Bloco 11 (Exportação Automatizada de PDF):</strong> Compilação do documento final (<code>Relatorio_Tecnico_Projeto2_Final.pdf</code>) integrando tabelas, gráficos, mapas OSRM e pareceres da IA via ReportLab e Selenium.</li>
  </ul>

  <hr>

  <h2 id="4-restrições-rígidas-hard-constraints-e-função-fitness">🛡️ 4. Restrições Rígidas (Hard Constraints) e Função Fitness</h2>
  <p>A Função Fitness aplica o <em>Penalty Method</em> com multiplicadores severos para garantir que nenhuma rota selecionada viole os limites operacionais:</p>
  <ol>
    <li><strong>Capacidade de Carga:</strong> Limite máximo estrito de <strong>20 caixas</strong> por veículo.</li>
    <li><strong>Autonomia Operacional:</strong> Distância máxima percorrida limitada a <strong>25 km</strong> por rota/veículo.</li>
    <li><strong>Prioridade de SLA e Cadeia de Frio:</strong> Penalização algorítmica severa caso entregas de <strong>Prioridade Alta</strong> (medicamentos termolábeis e urgências) sejam alocadas no final dos itinerários.</li>
    <li><strong>Dimensionamento de Frota:</strong> Distribuição otimizada em até <strong>3 veículos</strong> dedicados.</li>
  </ol>

  <hr>

  <h2 id="5-comparativo-de-desempenho-algoritmo-genético-vs-vizinho-mais-próximo">⚖️ 5. Comparativo de Desempenho (Algoritmo Genético vs. Vizinho Mais Próximo)</h2>
  <p>O benchmark implementado no Bloco 5 demonstra a superioridade da abordagem evolutiva:</p>
  <ul>
    <li><strong>Vizinho Mais Próximo (Heurística Gulosa):</strong> Toma decisões míopes baseadas apenas na menor distância imediata, ficando preso em ótimos locais e violando sistematicamente a autonomia de 25 km ou atrasando entregas de SLA crítico.</li>
    <li><strong>Algoritmo Genético (VRP):</strong> Avalia o espaço de busca de forma global ao longo das gerações, reduzindo o custo penalizado total e entregando rotas 100% aderentes às <em>Hard Constraints</em> de capacidade, quilometragem e prioridade médica.</li>
  </ul>

  <hr>

  <h2 id="6-integração-com-ia-generativa-llm">🤖 6. Integração com IA Generativa (LLM)</h2>
  <p>A integração com o Google Gemini (<code>google-genai</code>) cumpre dois papéis estratégicos no ecossistema:</p>
  <ul>
    <li><strong>Geração de Documentação Operacional e Executiva:</strong> Traduz os vetores matemáticos do VRP em instruções claras de segurança e cadeia de frio para os motoristas e em recomendações executivas de melhoria contínua para a diretoria hospitalar.</li>
    <li><strong>Assistente de Suporte à Decisão (Q&A):</strong> Permite aos gestores consultar o estado da frota em linguagem natural, contando com arquitetura tolerante a falhas (contingência local em cache).</li>
  </ul>

  <hr>

  <h2 id="7-configuração-do-ambiente-e-como-executar">🚀 7. Configuração do Ambiente e Como Executar</h2>
  
  <h3>Opção 1: Execução no Google Colab (Recomendada)</h3>
  <ol>
    <li>Importe o ficheiro <code>Tech_Challenge_Fase2_VRP.ipynb</code> no Google Colab.</li>
    <li>No menu lateral esquerdo (<em>Secrets</em> - ícone de chave), adicione a chave <code>GEMINI_API_KEY</code> com o seu token do Google AI Studio.</li>
    <li>Execute todas as células sequencialmente (<code>Runtime -&gt; Run all</code>).</li>
  </ol>

  <h3>Opção 2: Execução Local com Ambiente Virtual (venv)</h3>
  <p>Pré-requisito: Python 3.10 ou superior instalado.</p>
  
  <p><strong>Passo 1 — Clonar o repositório e aceder ao diretório:</strong></p>
  <pre><code>git clone https://github.com/gustavobhm/fiap-tech-challenge-fase2.git
cd fiap-tech-challenge-fase2</code></pre>

  <p><strong>Passo 2 — Criar e ativar o ambiente virtual (venv):</strong></p>
  <ul>
    <li><strong>Windows (CMD):</strong><br><code>python -m venv venv</code><br><code>venv\Scripts\activate.bat</code></li>
    <li><strong>Windows (PowerShell):</strong><br><code>python -m venv venv</code><br><code>Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser</code><br><code>.\venv\Scripts\Activate.ps1</code></li>
    <li><strong>Windows (Git Bash):</strong><br><code>python -m venv venv</code><br><code>source venv/Scripts/activate</code></li>
    <li><strong>Linux / macOS:</strong><br><code>python3 -m venv venv</code><br><code>source venv/bin/activate</code></li>
  </ul>

  <p><strong>Passo 3 — Instalar as dependências:</strong></p>
  <pre><code>python -m pip install --upgrade pip
pip install -r requirements.txt</code></pre>

  <p><strong>Passo 4 — Executar o Notebook e a Suíte de Testes (pytest):</strong></p>
  <pre><code>jupyter notebook Tech_Challenge_Fase2_VRP.ipynb
pytest</code></pre>

  <hr>

  <h2 id="8-estrutura-do-repositório">📁 8. Estrutura do Repositório</h2>
  <pre><code>fiap-tech-challenge-fase2/
    ├── src/                                      # Código-fonte e scripts modulares
    │   ├── Projeto_2_Otimizacao_Rotas_V10.ipynb  # Notebook principal contendo os 11 blocos executáveis
    │   ├── projeto_2_otimizacao_rotas_v10.py     # Versão em script Python do notebook principal
    │   └── test_vrp.py                           # Suíte de testes automatizados com pytest (validação de capacidade e autonomia)
    │
    ├── docs/                                     # Documentação de apoio, relatórios e manuais
    │   └── Relatorio_Tecnico_Projeto2_Final.pdf  # Relatório executivo consolidado em PDF do Tech Challenge
    │
    ├── assets/                                   # Recursos visuais, mapas e gráficos
    │   ├── grafico_abstrato.png                  # Gráfico em espaço cartesiano do Algoritmo Genético
    │   ├── mapa_final.png                        # Captura de tela do mapa interativo (Visão Geral SJC)
    │   ├── mapa_final.html                       # Código HTML interativo do mapa principal
    │   ├── mapa_real_final.png                   # Captura de tela do mapa em malha viária real (OSRM)
    │   └── mapa_real_final.html                  # Código HTML interativo do mapa viário OSRM
    │
    ├── requirements.txt                          # Dependências do projeto versionadas (com numpy, pandas, selenium, reportlab, google-genai, pytest, etc.)
    └── README.md                                 # Documentação técnica oficial e guião do repositório
  </code></pre>
  <hr>

  <h2 id="9-vídeo-de-demonstração">🎥 9. Vídeo de Demonstração</h2>
  <p>Assista à apresentação completa da arquitetura, execução ao vivo dos algoritmos, mapas OSRM e integração com o Google Gemini:</p>
  <ul>
    <li><strong>Link do Vídeo no YouTube:</strong>https://www.youtube.com/watch?v=Nl4leWoyAx4</li>
  </ul>
</div>
