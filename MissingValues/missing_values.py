import pandas as pd
import numpy as np
import random
import math

class MissingValues:
    def __init__(self,data):
        self.data=data

    def missing_percentage(self):
        return self.data.isna().sum().sum()/self.data.shape[0]

    def per_lessthan_one(self):
        self.data=self.data.dropna()
        return self.data
    def per_greaterthan_one(self,data):
        #sample
        sample=self.data.dropna()
        k=int(math.floor(sample.shape[0]*0.5))#k=sample percentage
        
        #Systematic sampling
        groups=int(k*0.2)
        split_size=int(k/groups)
        pick=[]
        c=0
        i=0
        j=split_size
        while(c<groups):
          pick.append(int(random.randint(i,j)))
          i+=split_size
          j+=split_size
          c+=1
        sample=sample.iloc[pick,:]

        # finding missing column names
        col=pd.DataFrame(data.isna().sum())
        col=col.reset_index()

        columns_list=[]
        h=col.shape[0]
        for i in range(h):
          if col.iloc[i,1]!=0:
            columns_list.append(col.iloc[i,0])


        dicti={}
        for i in range(len(sample.columns)):
          dicti[sample.columns[i]]=i
        k=sample.shape[0]*0.1
        split_size=int(sample.shape[0]/k)
        point=0
        point_len=len(columns_list)
        c=0
        i=0
        j=split_size
        rows=[]
        columns=[]
        values=[]
        while(c<k-2):
            r=int(random.randint(i,j))
            rows.append(r)
            columns.append(dicti[columns_list[point]])
            try:
                values.append(sample.iloc[r,dicti[columns_list[point]]])
            except:
                print(r,point)
            sample.iloc[r,dicti[columns_list[point]]]=np.nan
            point=(point+1)%point_len
            j+=split_size
            i+=split_size
            c+=1
        def mean(on_data,columns_list,rows,columns):
            mean_values=[]
            for i in columns_list:
                on_data[i]=on_data[i].fillna(pd.to_numeric(on_data[i],errors='coerce').mean())
            for i in range(len(rows)):
                mean_values.append(on_data.iloc[rows[i],columns[i]])
            return mean_values

        def median(on_data,columns_list,rows,columns):
            median_values=[]
            for i in columns_list:
                on_data[i]=on_data[i].fillna(pd.to_numeric(on_data[i],errors='coerce').median())
            for i in range(len(rows)):
                median_values.append(on_data.iloc[rows[i],columns[i]])
            return median_values
        
        mean_values=mean(sample.copy(),columns_list,rows,columns)
        median_values=median(sample.copy(),columns_list,rows,columns)
        mean_difference=0
        for i in range(len(values)):
            mean_difference+=abs(float(mean_values[i])-float(values[i]))

        median_difference=0
        for i in range(len(values)):
            median_difference+=abs(float(median_values[i])-float(values[i]))
        print(str(mean_difference)+" is the error of mean difference")
        print(str(median_difference)+" is the error of median difference")
        if mean_difference<median_difference:
            for i in columns_list:
                data[i]=data[i].fillna(pd.to_numeric(data[i],errors='coerce').mean())
        else:
            for i in columns_list:
                data[i]=data[i].fillna(pd.to_numeric(data[i],errors='coerce').median())
        return data
