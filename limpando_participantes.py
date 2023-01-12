import pandas as pd

data_raw = pd.read_csv("data_raw/participantes.csv", sep = ";").drop(axis=1, labels=["Unnamed: 0"])

cols = ['Data de nascimento', 'Idade', 'Data de Nascimento']
data = data_raw.assign(
    data_nascimento = lambda x: x['Data de nascimento'].fillna("") +
                                x['Data de Nascimento'].fillna("") +
                                x['Idade'].fillna("")
).drop(cols, axis = 1).drop("Ref.", axis = 1)

data[["municipio", "estado"]] = data['Origem'].str.split(",", expand= True)
data = data.drop("Origem", axis = 1)

profissoes = data.groupby(["Ocupação"]).agg(
    contagem = ("Ocupação", "count")
).sort_values("contagem", ascending= False)

print(profissoes)

# To do:
# Colocar gênero
