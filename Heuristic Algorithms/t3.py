# -*- coding: utf-8 -*-


from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn import metrics

data = load_digits()
x = data.data
y = data.target
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0, test_size=0.25,
                                                    stratify=y)
# 采用暴力搜索，所有参数进行组合，然后选择最好的参数
tuned_parameters = [{'penalty': ['l1', 'l2'],
                     'C': [0.01, 0.05, 0.1, 0.5, 1, 5, 10, 50, 100],
                     'solver': ['liblinear'],
                     'multi_class': ['ovr']},
                    {'penalty': ['l2'],
                     'C': [0.01, 0.05, 0.1, 0.5, 1, 5, 10, 50, 100],
                     'solver': ['lbfgs'],
                     'multi_class': ['ovr', 'multinomial']}]

clf = GridSearchCV(LogisticRegression(tol=1e-6), tuned_parameters, cv=10)
clf.fit(x_train, y_train)
print('Best parameters set found:', clf.best_params_)

print(classification_report(y_test, clf.predict(x_test)))
print(metrics.confusion_matrix(y_test, clf.predict(x_test)))

from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import scipy

digits = load_digits()
x = digits.data
y = digits.target

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0, test_size=0.25,
                                                    stratify=y)
# 采用随机搜索，给参数一个范围，然后系统随机选择参数，进行检验，然后选择最好的
tuned_parameters = {'C': scipy.stats.expon(scale=100),
                    'multi_class': ['ovr', 'multinomial']}
clf = RandomizedSearchCV(LogisticRegression(penalty='l2', solver='lbfgs', tol=1e-6),
                         tuned_parameters, cv=10, scoring='accuracy', n_iter=100)

clf.fit(x_train, y_train)
print('best parameters:', clf.best_estimator_)
print(classification_report(y_test, clf.predict(x_test)))
print(metrics.confusion_matrix(y_test, clf.predict(x_test)))
