from sklearn import svm
import pandas as pd
import numpy as np
import random

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

def read_form_exel():
    return pd.read_excel("D:\Files\Work\Prog\eatit\\USDA.xls")
	
s = read_form_exel()

x = s.values[:, 2]
Y = s.values[:, 1]

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

test = SelectKBest(score_func=chi2, k=100)
fit = test.fit(X, np.array(Y, dtype=int))


clf = svm.SVC()
print("LEARNING START")
clf.fit(fit.transform(X), np.array(Y, dtype=int))
print("LEARNING END")

a = np.zeros(len(ingrs_list), dtype=int)
for i, _ in enumerate(a):
    if random.randint(0, 100) < 30:
        a[i] = 1
print(clf.predict(fit.transform(a)))
