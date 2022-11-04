from bs4 import BeautifulSoup
import requests

urls = [] #Sites que serão minerados

palavras_chaves = [] #palavras_chaves que serão utilizadas para filtrar as noticias

def get_soup(url):
    """Função reponsável por realizar um request GET ao site e criar um objeto bs4"""
    try:
        req = requests.get(url)
        soup  = BeautifulSoup(req.text,'html.parser')
        return soup
    except:
        print("Não foi possivel fazer o request !")
        
def filtragem():
    "Função responsável por filtrar as noticias baseada nas palavras-chaves"
    lista_links = []
    for j in urls:
    #urls que serão mineradas
        soup = get_soup(j)  #criação do objeto beautifulSoup
        for k in palavras_chaves:
            for link in soup.find_all('a'):
              try:
               if '' not in link.get('href'):
                pass
               elif (k in link.get('href')): #inserção das palavras chaves
                lista_links.append('https://www.oliberal.com' + (link.get('href')))
              except:
               pass
    return list(set(lista_links))