import requests
from bs4 import BeautifulSoup

lista_links = open('lista.txt','w')
urls = ['https://dol.com.br/noticias/policia']

palavras_chaves = ['policia']
for j in urls:
 #urls que serão mineradas
    reqs = requests.get(j) #request do link
    soup = BeautifulSoup(reqs.text, 'html.parser')  #criação do objeto beautifulSoup
    for k in palavras_chaves:
     for link in soup.find_all('a'):
       try:
           if 'noticias' not in link.get('href'):
             pass
           elif (k in link.get('href')): #inserção das palavras chaves
            lista_links.write('https://dol.com.br' + link.get('href') + '\n')
       except:
        pass

lista_links.close()
