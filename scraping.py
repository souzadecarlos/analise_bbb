from wikitable import wikitable
from time import sleep
import pandas as pd

pages = range(1, 24)
classificacao_geral = [] #Coluna pos.
participantes = []  #Coluna participante
audiencia = [] #Coluna Data de transimssão
tabelas = {"classificacao_geral": classificacao_geral, "participantes": participantes, "audiencia": audiencia}

for page in pages:
    print(f"Extraindo tabelas da edicão nº {page}")
    sleep(1)
    url = f"https://pt.wikipedia.org/wiki/Big_Brother_Brasil_{page}"
    tables = wikitable(url)
    for table in tables:
        if set(["Participante", "Ocupação"]).issubset(set(table.columns.values)):
            table = table.assign(
                edicao = f"{page}"
            )
            participantes.append(table)
            print("Tabela de participantes - OK!")
        elif set(["Participante", "Pos."]).issubset(set(table.columns.values)):
            table = table.assign(
                edicao = f"{page}"
            )
            classificacao_geral.append(table)
            print("Tabela de classificacao - OK!")
        elif set(["Data de transmissão"]).issubset(set(table.columns.values)):
            table = table.assign(
                edicao = f"{page}"
            )
            print("Tabela de audiencia - OK!")
            audiencia.append(table)

print("Concatenando tabelas")
for i in tabelas:
    try:
        print(f"Preparando tabela {i}")
        concat_table = pd.concat(tabelas[i]).reset_index(drop = True)
        print(f"Salvando tabela {i}")
        concat_table.to_csv(f"data_raw/{i}.csv", sep = ";", encoding="utf-8-sig", index = False)
        print(f"Tabela {i} salva")
    except:
        print(f"Erro em executar tabela {i}")

