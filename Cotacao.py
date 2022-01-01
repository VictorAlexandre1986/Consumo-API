import requests

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
requisicao=requisicao.json()
for chave,valor in requisicao.items():
    print(f'{chave}: ')
    for moeda,conteudo in valor.items():
        print(f'\t{moeda} = {conteudo}')


print(f"Cotação do dolar : {requisicao['USDBRL']['bid']}")