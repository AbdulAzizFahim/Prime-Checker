import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import pickle

def train():
    iris_X, iris_y = datasets.load_iris(return_X_y=True)
    np.random.seed(0)
    indices = np.random.permutation(len(iris_X))
    iris_X_train = iris_X[indices[:-10]]
    iris_y_train = iris_y[indices[:-10]]
    iris_X_test = iris_X[indices[-10:]]
    iris_y_test = iris_y[indices[-10:]]
    knn = KNeighborsClassifier()
    knn.fit(iris_X_train, iris_y_train)
    filename = 'iris.sav'
    pickle.dump(knn, open(filename, 'wb'))
    return knn

lb = ["Iris Setosa","Iris Versicolour","Iris Virginica"]
kkk = train()
print(lb[kkk.predict([[1,2,1,2]])[0]])    
