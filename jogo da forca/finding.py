from bs4 import BeautifulSoup
import requests
import random

request =  requests.get('https://www.dicio.com.br/palavras-mais-buscadas/')

texto = request.text

bs = BeautifulSoup(texto, 'html.parser')

lista = bs.find('ul', class_='list')
lista = lista.find_all('li')

escolha = random.choice(lista)
palavra = escolha.text
palavra = str(palavra).strip()
text_palavra = str(palavra).strip()

tamanho_pegar = len(text_palavra)#tamanho para pegar após o href


escolha = str(escolha)
valor_corte = 14+tamanho_pegar
palavra_url= escolha[14:int(valor_corte)]

#print(palavra_url)
if __name__==__main__:
  print(palavra)

#////////////////////////////////////////segunda request\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

pagina_dica = requests.get(f'https://www.dicio.com.br/{palavra_url}/')
pagina_dica = pagina_dica.text

sopa = BeautifulSoup(pagina_dica, 'html.parser')

spans = sopa.find('p', class_='significado textonovo')
lista_de_dicas = spans.find_all('span')

dica1 = lista_de_dicas[1].text






