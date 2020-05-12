import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

class Outliers:
    def __init__(self,exec_data):
        self.exec_data=exec_data
    def numerical_outliers(self):
        num_columns=[]
        n_rows=self.exec_data.shape[0]
        f=['int32','int','int64','float','float32']
        for i in self.exec_data.columns:
            if self.exec_data[i].dtype in f:
                num_columns.append(i)
        for i in num_columns:
            
            sns.boxplot(self.exec_data[i]).set_title(i)
            pa=os.getcwd()
            pa=pa+'\\'+'FinalReport\\'+'outliers'+str(i)+'.png'
            plt.savefig(pa)
            
            q25=np.percentile(self.exec_data[i],25)
            q75=np.percentile(self.exec_data[i],75)
            iqr=(q75-q25)*1.5
            q75+=iqr
            q25-=iqr
            outliers_count=self.exec_data[self.exec_data[i]>q75].shape[0]
            outliers_count+=self.exec_data[self.exec_data[i]<q25].shape[0]
            outliers_percentage=(outliers_count/n_rows)*100
            if outliers_percentage<20:
                self.exec_data=self.exec_data[self.exec_data[i]<q75]
                self.exec_data=self.exec_data[self.exec_data[i]>q25]
        return self.exec_data
