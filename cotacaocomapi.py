#para utilizar API's é necessário importar a biblioteca REQUESTS e JSON (lembrar de instalar o requests)

import requests
import json

#atribuo uma variável para consumir as informações da API
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

#nesse ponto, printar a variável apenas retornará a porta 200 que significa que houve resposta
#print(cotacoes)

#utilizando o JSON é possível obter informações em formato de dicionário
cotacoes = cotacoes.json()
#print(cotacoes)

#para obter a informação, basta escolher o parâmetro desejado
valor_dolar = cotacoes['USDBRL']["bid"]
valor_euro = cotacoes['EURBRL']["bid"]
valor_btc = cotacoes['BTCBRL']["bid"]

print("O valor do Dólar atualmente é de: $", valor_dolar, "reais")
print("O valor do Euro atualmente é de: $", valor_euro, "reais")
print("O valor do Bitcoin atualmente é de: $", valor_btc, "reais")