from sklearn import svm
import pandas as pd
import numpy as np
import random

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from flask import *


def read_form_exel():
    return pd.read_excel("D:\Files\Work\Prog\eatit\\USDA.xls")


s = read_form_exel()

x = s.values[:, 2]
Y = s.values[:, 1]

voc = {"[1]": "завтрак", "[2]": "обед", "[3]": "ужин", "[4]": "закуска", "[5]": "Ошибка!"}

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


@app.route("/", method=['GET', 'POST'])
def hello():
    a = np.zeros(len(ingrs_list), dtype=int)
    for i, _ in enumerate(a):
        if random.randint(0, 100) < 15:
            a[i] = 1
    return render_template('index.tpl', num=voc[str(clf.predict(fit.transform(a)))])


if __name__ == "__main__":
    app.run()
