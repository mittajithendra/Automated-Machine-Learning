from sklearn.utils import resample
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

class imbalanced_data:
    def __init__(self,exec_data):
        self.exec_data=exec_data
    def upsample_data(self,tar):
        t=pd.DataFrame(self.exec_data[tar].value_counts())
        t=t.reset_index()
        sns.distplot(t['class'])
        pa=os.getcwd()
        pa=pa+'\\'+'FinalReport\\'+str('DataBalance')+'.png'
        plt.savefig(pa)

        
        n=t['class'].max()
        for i in range(t['class'].count()):
            if i==0:
                cla=self.exec_data[self.exec_data['class']==t['index'][i]]
                cla=resample(cla,replace=True,n_samples=n,random_state=27)
                final_data=cla
            else:
                cla=self.exec_data[self.exec_data['class']==t['index'][i]]
                cla=resample(cla,replace=True,n_samples=n,random_state=27)
                final_data=pd.concat([final_data,cla])
        self.exec_data=final_data
        return self.exec_data
