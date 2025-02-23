import requests

api_key = 'RGAPI-347ef6af-82f9-4370-ac0d-29f0d83ac54e'  # Substitua com sua chave de API
url = 'https://na1.api.riotgames.com/lol/status/v4/platform-data'  # Endpoint de status
headers = {
    'X-Riot-Token': api_key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print('Conexão bem-sucedida! Dados de status:')
    print(response.json())  # Exibe os dados de status
else:
    print(f'Erro na conexão. Código de status: {response.status_code}')
    print('Mensagem de erro:', response.text)
