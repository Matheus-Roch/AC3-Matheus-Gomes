#Descreva em portugues o desafio 

# 1 Importad base de daos(import pandas sempre)
import pandas as pd #pandas é uma biblioteca um pacote de dados que trabalham bem com dados
tabela - pd.read_csv("telecom_users.csv")

# 2 visualizar a base de dados 
display(tabela) # gual a print 

# 3 tratamento de dados(corrigir problemas  da base de dados )
# como escluir uma coluna que voce n precisa

#axis = 0 -> linha
#axis = 0 -> coluna

tabela = tabela.drop("Unnamed: 0", axis=0) # tabela = tabela.drop("nome da tabela: 0", axis=0)
#para excluir mais de uma coluna voce us [] >> tabela = tabela.drop(["Unnamed: 0", "IDClinte", "Aposentado "], axis=0)
display(tabela)

display(tabela.info())# voce recebe varias informaçõs da tabela

# 4 para tratar dados
tabela["TotalGasto"] = pd.numeric(tabela["TotalGasto"], erros="ocoerce")#este comando pega uma tabela e trasnforma em nuerico caso esteja com string, erros="coerce" >>tratamento de erro se for uma string ele deixa vazio

# tratar valores caso queria criar uma nova coluna tratata, antes do igual basta colocar onome da coluna que deseja criar
tabela["TotalGastoTratada"] = pd.numeric(tabela["TotalGasto"], erros="ocoerce")

#excluir as colunas vaiza, drop inteligente é "dropna" coluna vazia
tabela = tabela.dropna(how="all" , exis=1)#excluir as colunas vaiza
#"all" todas colunas vaias "eny" que tem pelo menos algun valor faltando na coluna\tabela

#para linha ^^
tabela = tabelana("how=any" , "exis=0")

#como contar os valores entr de m atabela 
print(tabela["Churn"].value_counts())#para saber quantas pesoas cancelaram e quantas pesoas não cancelaram 
#como calcular este vaor em precentual
print(tabela["Churn"].value_counts(notmalize = True))
#como formatar a porcentagem, se colocar 2 ele coloca duas casas decimais 
print(tabela["Churn"].value_counts(notmalize = True).map("{:.1%}".format))

#analise detalhada do clinte
#Sera que os generos masculona são maiores que os femininos,
#procurar pradrões  

import plotly.express as px # para criar graficos > para ver se esta instalado no jupyter !pip install plotly

grafico = px.histogram()(tabela, x="Aposentado", color="Churn")#cria o grafico naprimeira linha, no x="colocar o nome da coluna"
grafico.show()

#para criar istrograma com cores diferente 
grafico = px.histogram()(tabela, x="Aposentado", color="Churn", colcor_discrete_sequence=["blue", "green"])

#como analisar todas oc cancelamentos"Churn" 

for colun in tabela.columns:#paraver as linhas for colun in tabela.rows: 
    #print(colun)

coluna = "MesesComoClinte"
grafico = px.histogram()(tabela, x="Aposentado", color="Churn")#cria o grafico naprimeira linha, no x="colocar o nome da coluna"
grafico.show()

Para analisar basta ver se alguma cor se reslta no grafico 
qual a taxa de cancelamento do primero mes?
 -se tive primeirm mes promocional logic que o clinte vai cancelar depois de 1 mes
 - a primeira expericai do cliente esta sendo ruim
 
 Taxa de cancelamn po servilo de fibra  
 a taxa de cancelamtno por boleto eletronico da netflix é muito alta 


