# Вывод названия сайта по ссылке

import requests
from bs4 import BeautifulSoup

request = requests.get('https://www.svetrsk26.ru/')
page = request.text
doc = BeautifulSoup(page, 'html.parser')
title = doc.title.string
print(title)

from PIL import Image

filename = "GBPOY_SRSK.png"

with Image.open(filename) as img:
    img.load()

# Поворот изображения на 45 градусов
rotated_img = img.rotate(45)
rotated_img.show()

# Перевод изображения в градации серого
gray_img = img.convert("L")
gray_img.show()

import numpy as np

a3 = np.array([[[1, 2, 3], [4, 5, 6]],
               [[7, 8, 9], [10, 11, 12]]])

# Операция сложения
print(a3 + 10)

# Вычисление косинуса
print(np.cos(a3))


