import pandas as pd
import requests # Импорт библиотеки для запросов к серверу
from bs4 import BeautifulSoup # Импорт библиотеки для автоматического парсинга странички


URL='https://store.data-analyst.praktikum-services.ru/'
req = requests.get(URL) # GET-запрос
soup = BeautifulSoup(req.text, 'lxml')


name_products = [] # Список, в котором хранятся названия товаров
for row in soup.find_all('div', attrs = {'class':'t754__title t-name t-name_md js-product-name'}):
    name_products.append(row.text)


price = [] # Cписок, в котором хранятся цены на товар
for row in soup.find_all('div', attrs = {'class':'t754__price-value js-product-price'}):
    price.append(row.text)
    
# Датафрейм с данными о названии и цене товара 
products_data = pd.DataFrame(columns=['name', 'price'])
products_data['name'] = name_products
products_data['price'] = price
print(products_data.head())