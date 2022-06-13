import requests
import time
from bs4 import BeautifulSoup
import smtplib,getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

filer = open('lista.txt','r')
lista = filer.readlines()
new_list = []
for k in lista:
    new_list.append(k[:-1])
    
new_list = list(dict.fromkeys(new_list))
print(new_list)
for j in new_list:
    pagina = requests.get(j) #pagina que será raspada
    soup_objeto = BeautifulSoup(pagina.text,'html.parser') #Criação de um objeto 
    texts = soup_objeto.find(class_='col-md-8 mw-m-l-0')   
    texts = texts.get_text()
    print("\n\n\n",texts.center(15))
    mail_content = texts
#Senha e email do remetente
    remetente = 'ivangrana1956@gmail.com'
    senha = getpass.getpass("Insira a senha ->")
    destinatario = 'ivan.grana@icen.ufpa.br'
#MIME
    message = MIMEMultipart()
    message['From'] = remetente
    message['To'] = destinatario
    message['Subject'] = 'links raspados'   #Assunto do email

#corpo e anexos
    message.attach(MIMEText(mail_content, 'plain'))
#Criação da sessão SMTP
    s = smtplib.SMTP('smtp.gmail.com', 587) #porta 587 do gmail
    s.starttls() #TLS
    s.login(remetente, senha) #fazendo o login...
    text = message.as_string()
    s.sendmail(remetente, destinatario, text)
    s.quit()
    print('Email enviado')
    time.sleep(10)

