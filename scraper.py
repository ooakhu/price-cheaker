import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = 'https://stayingfresh.ca/collections/all/products/air-jordan-12-retro-reverse-flu-game-2020?variant' \
      '=32460090310743 '

headers = {
    "User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.141 Safari/537.36'}


def price_alert():
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(attrs={'class': 'product_name'}).get_text()
    price = soup.find(attrs={'class': 'money'}).get_text()
    converted_price = float(price[1:4])
    print(title, price, converted_price)

    if converted_price < 200:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('the email you want to use to send the mail', 'the password or app passcode ')

        subject = f'Price of {title} Went Down!'
        body = f'Check the amazon link {url}'
        msg = f'Subject:{subject} \n\n{body}'

        server.sendmail(
            'same as sending email',
            'delivery email',
            msg,

        )
        print('Alert has been sent!')
        server.quit()


while True:
    price_alert()
    time.sleep(43200)  # so this checks the price of the item twice a day
