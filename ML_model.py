import numpy as np
import pandas as pd


class ML_Selector():

    def __init__(self,dataset):
        self.dataset = pd.read_csv(dataset)
        self.name = []
        self.accuracy = []
        self.final = []

    def run(self):
        self.dataset.replace({'result':{'thumbsup':0,'scissors':1,'paper':2, 'rock':3}}, inplace=True)
        X = self.dataset.iloc[:,:-1].values
        y = self.dataset.iloc[:,-1].values
        y = y.reshape(len(y),1)

        from sklearn.svm import SVC
        self.ksvm = SVC(kernel='rbf',random_state=0)
        self.ksvm.fit(X,y.ravel())

    def find(self,arr):
        return self.ksvm.predict([arr])

def main():
    model = ML_Selector('hands.csv')
    model.run()
    ans = model.find([0,0,1,1,0])
    print(ans)

if __name__ == "__main__":
    main()
