from sklearn import svm
import pandas as pd
import numpy as np

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from flask import *

import requests
from bs4 import BeautifulSoup


def read_html(i):
    url = 'http://allrecipes.com/recipe/' + str(i)
    r = requests.get(url)
    return r.text


# возвращает текстовый файл с html кодом



def add_receipe(text):
    dic = {}
    # создаём словарь

    soup = BeautifulSoup(text)
    receipename = soup.find('div', {'class': 'recipe-container-outer'}).find('section', {
        'class': 'ar_recipe_index full-page'}).find('div', {'class': 'summary-background'}).find('h1', {
        'class': 'recipe-summary__h1'}).text
    for j in range(1, 2):
        lst = 'lst_ingredients_'
        recipe = soup.find('div', {'class': 'recipe-container-outer'}).find('section', {
            'class': 'ar_recipe_index full-page'}).find('section', {'class': 'recipe-ingredients'}).find('ul', {
            'id': lst + str(j)})  # 1st or 2nd list
        items = recipe.find_all('li', {'class': ['checkList__line']})
        spis = []
        for item in items:
            spis.append(item.find('span', {'itemprop': 'ingredients'}).text)
            dic[receipename] = spis
            # добавляем рецепты в словарь
    return dic


def out_name_and_array(k):
    dic = add_receipe(read_html(k))
    name = list(dic.keys())[0]
    arr = []
    for i in dic[name]:
        arr += i.split(" ")

    return name, arr


def read_form_exel():
    return pd.read_excel("D:\Files\Work\Prog\eatit\\USDA.xls")


s = read_form_exel()

x = s.values[:, 2]
Y = s.values[:, 1]

voc = {"[1]": "Это кушают на завтрак",
       "[2]": "Можно и на обед",
       "[3]": "Отужинать бы этим",
       "[4]": "Не главное блюдо трапезы",
       "[5]": "Только этим нельзя наесться"}

ingrs_list = []
for ingrs_str in x:
    if type(ingrs_str) is str:
        ingrs = ingrs_str.split(',')
        for i in ingrs:
            if i not in ingrs_list:
                ingrs_list.append(i)

table = np.zeros((len(x), len(ingrs_list)), dtype=int)

for ind, ingrs_str in enumerate(x):
    if type(ingrs_str) is str:
        ingrs = ingrs_str.split(',')
        for i in ingrs:
            table[ind, ingrs_list.index(i)] = 1

X = table

test = SelectKBest(score_func=chi2, k=50)
fit = test.fit(X, np.array(Y, dtype=int))

clf = svm.SVC()
print("LEARNING START")
clf.fit(fit.transform(X), np.array(Y, dtype=int))
print("LEARNING END")

app = Flask(__name__)


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.form.get('url') is None:
        return render_template('index.tpl', name='', num='')
    else:
        name, ingrs__ = out_name_and_array(request.form.get('url'))
        ingrs = []
        for tyu in ingrs__:
            ingrs += tyu.upper().split(',')
        print(name)
        print(ingrs)
        a = np.zeros(len(ingrs_list), dtype=int)

        for i, ing in enumerate(ingrs):
            if ing in ingrs_list:
                a[ingrs_list.index(ing)] = 1

        return render_template('index.tpl', name=name, num=voc[str(clf.predict(fit.transform(a)))])


if __name__ == "__main__":
    app.run()
