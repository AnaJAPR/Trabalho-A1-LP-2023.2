# Análises
## Sigla de Estado
### Contexto
Resolveu-se analisar à coluna das siglas de estado, nomeada como "Sigla da UF" no
DataFrame pois esta pode nos dar melhor noção de em que regiões do país há maior
concentração de instituições de ensino e em que regioões elas são mais escassas.

### Resultados
Foram analisadas a quantidade de instituições de ensino tal que houveram alunos para que o IGC fosse computado.

Observou-se que os estados de São Paulo, Minas Gerais, Paraná, Rio de Janeiro e Bahia 
são os que possuem maior número de instituições de ensino.
Isso faz sentido quando levamos em consideração o fato de que estes estados são os 
5 estados brasileiros com maior população, havendo então maior demanda pelas 
instituições de ensino.

Enquanto isso, Roraima, Acre, Amapá, Sergipe e Tocantins são os estados brasileiros 
com menor número de instituições de ensino no IGC. 4 dos 5 estados com menor população
do país.

## Conceito Médio de Mestrado
### Contexto
A análise da coluna "Conceito Médio de Mestrado" pode trazer informações da qualidade 
de ensino das instituições de ensino brasileiras que oferecem cursos de mestrado. A
intenção desta análise é verificar se, de forma geral, o Brasil possui um bom conceito
médio de mestrado.

### Resultados
Através da análise da coluna, foi verificado que:
* Todas as instituições de ensino avaliadas que oferecem cursos de mestrado possuem uma nota entre 4,0 e 5,0.
* A média entre as instituições de ensino é de 4,3088, com desvio padrão de 0,2571.
* A mediana é de 4,2765.

## Alfa, Beta e Gama
### Contexto
As colunas "Alfa (Proporção de Graduação)", "Beta (Proporção de Mestrado - 
Equivalente)" e "Gama (Proporção de Doutorandos – Equivalente)" representam a 
proporção de alunos em cada nível de ensino.

A análise destas colunas pode retornar como os alunos geralmente se distribuem em
cada nível de ensino.

### Resultados
Por ser proporções do total, pressupõe-se que a soma das 3 colunas seja 1. A soma na
maioria dos casos resulta em 1 ou em valores muito próximos. A média da soma das 3 é
de 0,993, com a mediana sendo 1. O fato de haver valores menores que 1 podem indicar 
erros devido à arredondamento e à instituições de ensino sem alunos matriculados.

A média da proporção de Alfa é de 0,993, indicando a forte presença de alunos de
graduação. Em várias instituições de ensino, 100% dos alunos são de graduação. O 
desvio padrão é de 0,125 e sua mediana é 1.

A média da proporção de Beta é de 0,017, muito menor que a de Alfa. Seu desvio 
padrão é de 0,063 e sua mediana é 0. A maior proporção em uma instituição de ensino é 
de 0,690, que ocorre na Faculdade Unida de Vitória.

A média da proporção de Gama é de 0,009, ainda menor que a de Beta. Seu desvio padrão
é de 0,042 e sua mediana é 0. A maior proporção em uma instituição de ensino é de 
0,443, que ocorre na Universidade Estadual de Campinas.

Assim é possível concluir que as instituições de ensino, em geral, possuem um número 
de estudantes de graduação substancialmente maior que os de mestrado e doutorado.