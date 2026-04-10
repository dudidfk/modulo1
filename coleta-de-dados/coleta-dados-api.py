import requests
# 1. Definir a função para buscar dados da API
def fetch_data(endpoint, filters={}):
    url = f'https://rickandmortyapi.com/api/{endpoint}' # Construindo a URL da API com o endpoint fornecido
    response = requests.get(url, params=filters) # Fazendo a requisição GET para a API, passando os filtros como parâmetros
    # 2. Verificar se a requisição foi bem-sucedida e retornar os dados em formato JSON, ou None em caso de falha
    return response.json() if response.status_code == 200 else None 
# 3. Exemplo de uso da função para buscar informações sobre um personagem específico da série "Rick and Morty"    
character = fetch_data('character', {'name': 'Rick Sanchez'})
if character: # Verificando se os dados foram retornados com sucesso antes de tentar acessar o conteúdo
    print('character')
else:
    print('Failed to fetch data')

print(character)