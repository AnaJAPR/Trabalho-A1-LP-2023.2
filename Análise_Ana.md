# Introdução

### A princípio, escolhi as colunas "IGC (Faixa)" e "Organização Acadêmica" para analisar. A ideia era ver qual a faixa de IGC mais comum para cada tipo de instituição educacional e qual a média de IGC para cada um também.

# Análise Contagem

### Meu primeiro plot é um gráfico de linhas mostrando a frequência de ocorrência de cada valor de IGC faixa para cada organização acadêmica.
### Assim, ao analisar o plot, conclui-se que:

- Faculdade apresenta muito mais vezes a faixa 3 de IGC do que as outras, diria até que é um outlier do gráfico, devido ao acento da curva nesse ponto.
- Universidade varia entre as faixas de 2 a 5, sendo mais frequente a 4.
- Centro Universitário geralmente fica no nível 3 de IGC, mas é bem comum os níveis 2 e 4 também
- Centro Federal de Educação Tecnológica não aparece muito no df, mas as poucas vezes em que se faz presente possui faixa 4, apenas.
- Instituto Federal de Educação, Ciência e Tecnologia também é pouco apresentado no df, mas geralmente fica nos níveis 3 e 4 de IGC, sendo ambas as faixas quase que igualmente frequentes.

### Considerando que IGC faixa é um indicador de qualidade do MEC que considera a qualidade dos cursos de graduação e pós-graduação numa escala de 1 a 5.
### Ao observar o gráfico, temos que faculdade geralmente é a organização acadêmica com maior frequência dos maiores IGCs. Isto pode ser porque o nível de qualidade dos seus cursos são melhores, mas também porque esse tipo de instituição é mais comum, tem mais dados.
### Outra observação é que no nível 5 (considerado o melhor IGC faixa) faculdade e universidade tem praticamente o mesmo nível de frequência de ocorrência, isto é, além de ambas serem tipos de instituições mais comuns, elas costumam ser avaliadas como melhores pelo IGC faixa do MEC.

# Análise Média

### Meu segundo plot é um gráfico de barras que mostra a faixa média de IGC para cada organização acadêmica. 
### Assim, ao analisar o plot conclui-se, pricipalmente, que:

- Centro Federal de Educação Tecnológica possui a maior faixa média de IGC.
- Faculdade tem a menor faixa média de IGC.

### Dessa forma, ainda que toda medida tenha suas imperfeições, acredito que a média se encaixe bem aqui. Se compararmos com a análise anterior, por exemplo, faculdade tem a maior frequência de ocorrência das melhores faixas de IGC, no entanto, a faixa média é a menor. Ou seja, a primeira análise pode ter "favorecido" faculdade já que esta aparece em maior quantidade no df, mas agora como a média divide pela quantidade total que cada organização acadêmica aparece, fez-se uma análise mais justa de certa forma.

### Nessa segunda análise, vemos também que Centro Federal de Educação Tecnológica tem a maior faixa média, afinal ele aparece poucas vezes no df e é sempre faixa 4. 
### A segunda maior faixa média é Universidade, mostrando que ela se destaca nas duas análises.

### Portanto, diria que Universidade é a organização acadêmica mais bem avaliada pelo MEC no geral, já que diante de tantas instuições desse tipo presente no df, ela se destaca nas duas análises.
