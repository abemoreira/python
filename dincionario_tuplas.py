print("--- Passo 1: Criando o dicionario inicial---")

ponto_de_interesse = {
    "Torre Eiffel":(48.8584, 2.2945),
    "Estatua da Liberdade":(40.6892, -74.0445),
    "Machu Picchu":(-13.1631, -72.5450)
}

print("dincionario 'ponto_de_interesse'.")
print(ponto_de_interesse)
print("-"*30)

print("--- Passo 2: Acessando as coordenadas de um lugar ---")

nome_lugar_para_acessar = "Torre Eiffel"

coordenadas_torre = ponto_de_interesse[nome_lugar_para_acessar]

print(f"As coordenadas de {nome_lugar_para_acessar} são:")
print(coordenadas_torre)
print("-"*30)

print("--- Passo 3: Acessando elementos de dentro da tupla---")

latitude = coordenadas_torre[0]
longitude = coordenadas_torre[1]

print(f"Latitude: {latitude}.")
print(f"Longitude:{longitude}.")
print("-"*30)

print("--- Passo 4: Adcionando um novo lugar ao dicionario---")

nome_novo_lugar = "Cristo Redentor"
coordenadas_novo_ligar = (-22.9519, -43.2105)
ponto_de_interesse[nome_novo_lugar] = coordenadas_novo_ligar

print(f"Dicionario após adcionar {nome_novo_lugar}:.")
print(ponto_de_interesse)
print("-"*30)