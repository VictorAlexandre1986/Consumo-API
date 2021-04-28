import requests
import json

#Site onde se obtem o token, é preciso criar uma conta : https://advisor.climatempo.com.br
iTOKEN ="de7dc427cd147a4eecb30fcd06f34a7b"

#Consulte o id da sua cidade e depois passe para as funções
def consulta_id():

    iCITY = input('Informe o nome da cidade: ')
    iURL = "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name="+iCITY+"&state=SP&token=" + str(iTOKEN)
    iRESPONSE = requests.get(iURL, params=iCITY)
    iRETORNO_REQ = json.loads(iRESPONSE.text)
    for iCHAVE in iRETORNO_REQ:
        iID = iCHAVE['id']
        iNAME = iCHAVE['name']
        iUF = iCHAVE['state']
        iPAIS = iCHAVE['country']
        print(f'ID: {iID} , cidade: {iNAME} , estado: {iUF} , pais: {iPAIS}')


def registred_city(id):


    iURL = "http://apiadvisor.climatempo.com.br/api-manager/user-token/" + str(iTOKEN) + "/locales"
    payload = 'localeId[]=' + id
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    iRESPONSE = requests.put(iURL, headers=headers, data=payload)
    print(iRESPONSE.text)

def consulta_tempo(id):
    iURL = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/" + id + "/current?token=" + iTOKEN
    iRESPONSE = requests.get(iURL)
    iRETORNO_REQ = json.loads(iRESPONSE.text)
    
    for chave in iRETORNO_REQ:
        print(chave + " : " + str(iRETORNO_REQ[chave]))
    Id = iRETORNO_REQ['id']
    print(f'A id da cidade : {Id}')
    Cidade = iRETORNO_REQ['name']
    print(f'Cidade da leitura : {Cidade}')
    UF = iRETORNO_REQ['state']
    print(f'Estado : {UF}')
    Pais = iRETORNO_REQ['country']
    print(f'O pais da leitura : {Pais}')
    Temperatura = iRETORNO_REQ['data']['temperature']
    print(f'Temperatura atual: {Temperatura}ºC')
    Vel_vento = iRETORNO_REQ['data']['wind_velocity']
    print(f'Velocidade do vento {Vel_vento} km/h')
    Umidade = iRETORNO_REQ['data']['humidity']
    print(f'A umidade do ar atual é : {Umidade} %')
    Condicao = iRETORNO_REQ['data']['condition']
    print(f'A condição do tempo atual é : {Condicao}')
    Pressao = iRETORNO_REQ['data']['pressure']
    print(f'A pressão está : {Pressao} hPa')
    Sensacao = iRETORNO_REQ['data']['sensation']
    print(f'A sensação térmica é de : {Sensacao}ºC')
    Data = iRETORNO_REQ['data']['date']
    print(f'Data da leitura {Data}')

def previsao_15Dias(id):
#Previsão de três meses para a cidade
    iURL = "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/" + id + "/days/15?token=" + str(iTOKEN)
    iRESPONSE = requests.get(iURL)
    iRETORNO_REQ = json.loads(iRESPONSE.text)
    cidade = iRETORNO_REQ['name']
    uf = iRETORNO_REQ['state']
    grafico = iRETORNO_REQ['meteogram']
    print(f'Cidade : {cidade}')
    print(f'Estado : {uf}')
    print(f'O link do gráfico dos próximos 15 dias : {grafico}')
    for dados in iRETORNO_REQ['data']:
        data = dados['date_br']
        probabilidade = dados['rain']['probability']
        max = dados['temperature']['max']
        min = dados['temperature']['min']
        umidadeMinManha = dados['humidity']['morning']['min']
        umidadeMaxManha = dados['humidity']['morning']['max']
        umidadeMinTarde = dados['humidity']['afternoon']['min']
        umidadeMaxTarde = dados['humidity']['afternoon']['max']
        umidadeMinNoite = dados['humidity']['night']['min']
        umidadeMaxNoite = dados['humidity']['night']['max']
        pressao = dados['pressure']['pressure']
        vento = dados['wind']['velocity_avg']
        uv = dados['uv']['max']
        sensaocaoTermicaMin = dados['thermal_sensation']['min']
        sensaocaoTermicaMax = dados['thermal_sensation']['max']


        print(f'No dia {data} terá a temperatura máxima : {max}ºC e a mínima : {min}ºC, a probabilidade de chuva é de : {probabilidade}% , pressão : {pressao} hPA, vento : {vento} km/h, o índice o ultra violeta : {uv}, sensação termica mínima : {sensaocaoTermicaMin}ºC e a sensação máxima : {sensaocaoTermicaMax}ºC')
    print(iRETORNO_REQ['data'])

def previsao_3Dias(regiao):
    #Previsao de 3 dias da região
    #regioes (sul,sudeste,norte,nordeste,centro-oeste)
    iURL = "http://apiadvisor.climatempo.com.br/api/v1/forecast/region/" + regiao + "?token=" + str(iTOKEN)
    iRESPONSE = requests.get(iURL)
    iRETORNO_REQ = json.loads(iRESPONSE.text)
    regiao = iRETORNO_REQ['region']
    dicionario = iRETORNO_REQ['data']

    for dados in iRETORNO_REQ['data']:
        data = dados['date_br']
        grafico = dados['image']
        descricao = dados['text']
        print(f'Na região {regiao },no dia {data} o tempo estara com : {descricao}')


def condicao_ar(id):
    iURL="http://apiadvisor.climatempo.com.br/api/v1/index/respiratory-disease/locale/" +id+ "?token=" + iTOKEN
    iRESPONSE = requests.get(iURL)
    iRETORNO_REQ = json.loads(iRESPONSE.text)


if __name__=='__main__':
    #consulta_id()
    #id = input('Informe o id da cidade desejada: ')
    #registred_city(id)
    #consulta_tempo("3694")
    #proliferacao_mosquito("3694")
    previsao_15Dias("3694")