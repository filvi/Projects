import requests
from bs4 import BeautifulSoup
import smtplib


# https://www.msi.com/Content-creation/Prestige-15-A10X/wheretobuy
URL = "https://www.amazon.it/gp/product/B07WX4VG7V"


headers = { "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}

def check_prices():
    page = requests.get(URL, headers=headers)


    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text().strip()
    price = soup.find(id='priceblock_ourprice').get_text().strip()[:-2]
    price = float(price.replace(".","" ).replace(",", "."))

    if price < 999:
        send_mail(title, price, URL)


def send_mail(title, price, URL):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    gpass = "irurqsjbivvmjzeu"
    server.login('fv.filippovicari@gmail.com', gpass )

    subject = f"Il prezzo inferiore alla soglia impostata (999)"
    body = f"Il prodotto che stai tracciando: \n{title}\n\nora costa {price}\n\necco il link: {URL}" 

    msg = f"Subject: {subject}\n\n{body}"


    server.sendmail(
        'fv.filippovicari@gmail.com',
        'fil.vicari@gmail.com',
        msg
    )

    print("Email inviata")
    server.quit()

check_prices()
