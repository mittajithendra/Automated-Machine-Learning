import numpy as np
import pandas as pd
class datatypes:
    def __init__(self,exec_data):
        self.exec_data=pd.DataFrame(exec_data)
    def apply_data_types(self):
        k=0
        for i in self.exec_data.columns:
            if self.exec_data[i].dtype == 'object':
                print(self.exec_data[i])
                count=0
                collect_data=[]
                j=0
                while(count<10):
                    try:
                        if str(self.exec_data.iloc[j,k])!= str(np.nan):
                            collect_data.append(self.exec_data.iloc[j,k])
                            count+=1
                            j+=1
                    except:
                        j+=1
                try:
                    print(collect_data)
                    collect_data=pd.to_numeric(collect_data)
                    print(collect_data)
                    self.exec_data[i]=pd.to_numeric(self.exec_data[i],errors='coerce')
                except:
                    try:
                        collect_data=pd.to_datetime(collect_data)
                        self.exec_data[i]=pd.to_datetime(self.exec_data[i],errors='coerce')
                    except:
                        pass
            k+=1
        return self.exec_data

