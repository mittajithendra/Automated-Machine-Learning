from sklearn.linear_model import LogisticRegression
import numpy as np

class feature_importance:
    def __init__(self,data,classification):
        self.exec_data=data
        self.classification=classification
    def find_important_features(self,target):
        if self.classification == 'True':
            m=LogisticRegression()
            selected_columns=[]
            for i in self.exec_data.columns:
                if i != target and i!='pickup_datetime':
                    selected_columns.append(i)
            m.fit(self.exec_data[selected_columns],self.exec_data[target])
            print(m.coef_)
            
        
