import requests
from bs4 import BeautifulSoup
# 1. Fazer a requisição HTTP para obter o conteúdo da página
requisicao = requests.get('https://books.toscrape.com/')
# 2. Verificar se a requisição foi bem-sucedida
if requisicao.status_code == 200:
    print('Requisição bem-sucedida!')
extracao = BeautifulSoup(requisicao.text, 'html.parser')
# 3. Extrair os dados desejados usando BeautifulSoup
extracao.find_all('article', class_='product-pod')
# 4. Armazenar os dados extraídos em uma estrutura de dados adequada (como uma lista de dicionários)
catalogo = []
contar_livros = 0 # Variável para contar o número de livros encontrados
# 5. Exibir os dados extraídos
for artigo in extracao.find_all('article', class_='product_pod'):
    titulo = artigo.find('h3').find('a')['title'] # Acessando o atributo 'title' da tag 'a' dentro do 'h3' para obter o título do livro
    preco = artigo.find('p', class_='price_color').text # Acessando o texto da tag 'p' com a classe 'price_color' para obter o preço do livro
    # Criando um dicionário para armazenar as informações do livro e adicionando-o à lista de catálogo
    livro = {
        'titulo': titulo,
        'preco': preco
    }
    # Adicionando o dicionário do livro ao catálogo
    catalogo.append(livro)
    # Incrementando a contagem de livros encontrados    
    contar_livros += 1
    

print(f'Foram encontrados {contar_livros} livros.')