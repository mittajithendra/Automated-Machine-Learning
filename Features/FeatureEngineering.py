import pandas as pd

class FeatureEngineering:
    def __init__(self,exec_data):
        self.exec_data=exec_data
    def date_time_features(self):
        for i in self.exec_data.columns:
            if str(self.exec_data[i].dtype) == 'datetime64[ns, UTC]':
                self.exec_data['year']=self.exec_data[i].dt.year
                self.exec_data['month']=self.exec_data[i].dt.month
                self.exec_data['day']=self.exec_data[i].dt.day
                self.exec_data['dayofweek']=self.exec_data[i].dt.dayofweek
                self.exec_data['Hour']=self.exec_data[i].dt.hour
                self.exec_data=self.exec_data.drop(i,axis=1)
        return self.exec_data
    def LabelEncoder(self):
        for i in self.exec_data.columns:
            if self.exec_data[i].dtype=='object':
                self.exec_data[i]=pd.Categorical(self.exec_data[i])
                self.exec_data[i]=self.exec_data[i].cat.codes
        return self.exec_data
        
