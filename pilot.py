import time
import requests
from bs4 import BeautifulSoup
import smtplib

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

URL = 'https://en-ae.namshi.com/buy-adidas-originals-nmdr1-casual-mens-sneakers-shoes-w714476a.html'  #URL of item

def notify_me():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('Kartikeyarai7@gmail.com', 'obilqvicamaliiyh')
    subject = 'Prices changed'
    body = 'Check Namshi  link https://en-ae.namshi.com/buy-adidas-originals-nmdr1-casual-mens-sneakers-shoes-w714476a.html . Reminding you to forget buying those slick adidas shoes causeyou still can not afford them!'

    msg = f"Subject = {subject}\n\n{body}"
    server.sendmail(
        'Kartikeyarai7@gmail.com',
        'f20170170@dubai.bits-pilani.ac.in',
        msg 
    )

    server.quit()


def checking():      
    shoes = requests.get(URL)
    # print(points_talley.text)
    
    soup = BeautifulSoup(shoes.text,'html.parser')
    # print(soup.prettify)
    
    price = soup.select("p span")[0]
    # print(price.text)
    check_price = float(price.text[0:4])
    print(check_price)
    if (check_price > 500):    
      notify_me()

while(True):
    checking()  #Check prices
    time.sleep(3600)      # Check again after 1 hour
