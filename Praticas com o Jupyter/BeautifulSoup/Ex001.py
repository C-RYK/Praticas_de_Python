from bs4 import BeautifulSoup
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0"}
link = requests.get('https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar', headers=headers)

pagina = BeautifulSoup(link.text, "html.parser")

#print(link.status_code)
#print(pagina.prettify())

print(pagina.title)
titulo = pagina.find('title')
print(titulo)

inp = pagina.findAll('input')

print(f"{inp[2]['aria-label']}:")

dolar = pagina.find_all('input')

print('Dolar:', end=' ')
print(dolar[2]['value'])

valor = pagina.find('span', class_="DFlfde SwHCTb")

num = valor['data-value']

num_float = float(num)

print('Real', end=' ')
print(f'{num_float:.2f}')
