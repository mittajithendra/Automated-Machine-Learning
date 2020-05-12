import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import os

class Visualization:
    def __init__(self,data,target):
        self.exec_data=data
        self.target=target
    def start_visuals(self):
        for i in self.exec_data.columns:
            if self.exec_data[i].dtype in ['int32','int64','int','float64','int8']:
                sns.distplot(self.exec_data[i],kde=True,rug=True).set_title(i)
                pa=os.getcwd()
                pa=pa+'\\'+'FinalReport\\'+str(i)+'.png'
                plt.savefig(pa)
