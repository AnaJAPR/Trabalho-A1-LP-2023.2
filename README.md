# Trabalho-A1-LP-2023.2
Alunos: Ana Júlia Amaro, Guilherme Moreira Castilho, Otávio Bettega e Paulo César
Gomes Rodrigues

# Objetivo
Este trabalho visa realizar uma análise de dados do IGC (Índice Geral de Cursos) do 
ano de 2021, extraindo informações das colunas e desenvolvendo visualizações com os
resultados obtidos.

A base de dados pode ser encontrada em:
IGC indice de universidades: [https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/indicadores-de-qualidade-da-educacao-superior](url)
A mesma está presente no repositório nos formatos xlsx e csv.

# Estrutura do Repositório
Este repositório conta com 4 arquivos de analise (python) utilizados para extrair as
informações e gerar os gráficos e 4 arquivos de texto (md) no qual os membros do
grupo escreveram suas conclusões.

Há ainda módulos com funções uteis para a limpeza e tratamento dos dados. São eles:
* limpa_dados: Com funções focadas em deixar o DataFrame mais fácil de trabalhar
* func_analises: Com funções úteis para análise, facilitando cálculos de medidas resumo, reindexação e filtragem nos DataFrames, etc.

Todos os gráficos podem ser visualizados de maneira prática pelo arquivo 
*index.html*, onde estão listados e exibidos. Eles também estão no repositório em 
formato png na pasta *graphic_folder*.

Todas as funções passaram por unittests e doctests:
* Os arquivos de unittest podem ser encontrados na pasta *tests*, separados em um  por função.
* Os arquivos de doctest foram feitos no formato txt na pasta *doctest_folder* e  devidamente chamados nos respectivos módulos.

Todas as funções estão devidamente documentadas e comentadas. A documentação foi 
gerada utilizando a ferramenta Sphinx. Ela pode ser acessada em:
"docs/_build/html/index.html".