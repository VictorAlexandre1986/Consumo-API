import requests

try:

    cep = input('Informe o cep sem os pontos e traço : \n')

    #A resposta já vem em json
    conteudo = requests.get("http://viacep.com.br/ws/" + cep + "/json/")

    #Convertendo o conteudo de json para dicionario
    dados = dict(conteudo.json())

    cep = dados.get('cep')
    logradouro = dados.get('logradouro')
    complemento = dados.get('complemento')
    bairro = dados.get('bairro')
    localidade = dados.get('localidade')
    uf = dados.get('uf')
    ddd = dados.get('ddd')

    #Se for o valor 400 o cep é inválido
    print(f'O status da requisição {conteudo.status_code}  ')

    print('\n Os dados do cep: \n')
    for chave,valor in dados.items():
        print(f'{chave} : {valor}')

except (Exception):
    print('Não foi possível fazer uma requisição na URI especificada.')