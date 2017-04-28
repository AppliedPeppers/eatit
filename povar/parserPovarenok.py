import requests
from bs4 import BeautifulSoup
from lxml import html
import tqdm
import json

def read_html(i):
    url='http://www.povarenok.ru/recipes/show/'+str(i)
    r=requests.get(url)
    return r.text

url='http://www.povarenok.ru/recipes/show/'+str(85000)
r=requests.get(url)
text=r.text
soup=BeautifulSoup(text)#преобразовываем html into txt
receipename=soup.find('div', {'id':'print_body'}).find('h1').find('a').text
recipe=soup.find('div', {'class': 'recipe-ing'})
items=recipe.find_all('li', {'class': ['cat']})
spis=[]
for item in items:
    spis.append(item.find('a').find('span').text)

dic={receipename:spis}
#создаём первый рецепт в словаре

def add_receipe(text):
    soup=BeautifulSoup(text)
    receipename=soup.find('div', {'id':'print_body'}).find('h1').find('a').text
    recipe=soup.find('div', {'class': 'recipe-ing'})
    items=recipe.find_all('li', {'class': ['cat']})
    spis=[]
    for item in items:
        spis.append(item.find('a').find('span').text)
    dic[receipename]=spis
#добавляем рецепты в словарь

limit = 5
offset = 10000
bar=tqdm.tqdm(total=limit)        
for i in range(offset,offset+limit):
    try:
        text=read_html(i)#получили текстовый файл данного рецепта, написанного в html
        add_receipe(text)
    except:
        pass
    bar.update(1)
    

bar.close()
with open('outputOLEG.json','w', encoding='utf-16') as output_file:
    output_file.write(json.dumps(dic))
    
