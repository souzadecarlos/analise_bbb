import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep


n_edicoes = range(1, 23)

participantes = pd.DataFrame(data = {
    "Participantes": [],
    "Idade": [],
    "Ocupacao": [],
    "Origem": [],
    "Resultado": [],
    "Ref.": [],
    "Edicao": []
})

def get_table(html, edicao):
    print(f"Iniciando coleta da edição nº {edicao}")
    sleep(1)
    re = requests.get(html)
    soup = BeautifulSoup(re.text, "html.parser")
    tables = soup.find_all(class_ = "wikitable")
    for table in tables:
        if table.find_all("th")[0].text.replace("\n", "") == "Participante":
            total_content = []
            content = []
            for num, i in enumerate(table.find_all("td")):   
                if num % 6 == 0 and num not in [0, 1]:
                    content.append(f"BBB {edicao}")
                    total_content.append(content)
                    content = []
                content.append(i.text.replace("\n", ""))
            return total_content

lista_participantes = []
for edicao in n_edicoes:
    url = f"https://pt.wikipedia.org/wiki/Big_Brother_Brasil_{edicao}"
    lista_participantes = get_table(url, edicao)
    for i in lista_participantes:
        participantes.loc[len(participantes)] = i

participantes.to_csv("data_raw/participantes", sep = ";", encoding= "latin-1")