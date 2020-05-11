import sys
import os
import pandas as pd
from pathlib import Path
from MissingValues import missing_values
from Outliers import outliers
from AssignDataTypes import assigndatatypes
from sklearn.model_selection import train_test_split
from Modeling import models
from Features import FeatureEngineering
from ImbalancedData import imbalanced_data
from Modeling import classification_models
from Visualizations import visualization
from Features import feature_importance
import warnings
from MakingReport import makingreport

if __name__=='__main__':


    warnings.filterwarnings('ignore')
    
    #      -------------path-----------------
    print("Enter the path of your dataset")
    
    p=Path(input()).resolve()
    flag=1
    while(flag):
        if not os.path.isfile(p):
            print("Please enter valid path")
            flag=0
        elif not (str(p).endswith('.csv') or str(p).endswith('.xlsx')):
            print("File should only endswith csv or xlsx")
            flag=0
        if flag==0:
            p=Path(input()).resolve()
            flag=1
        else:
            break
    data=pd.read_csv(p)





    #      -----------Target-----------------
    print("Type 'YES' If your dataset has a target else type 'No'. ")
    Target_check=input().lower()
    while(Target_check != 'yes' and Target_check!='no'):
        print("Please enter either 'yes' or 'no'. ")
        Target_check=input().lower()
    if Target_check=='yes':
        print("The columns in your dataset are :")
        for i in data.columns:
            print(i)
        print("Please enter the exact name of target variable")
        
        while(1):
            target=input()
            if target in data.columns:
                break
            else:
                print("Entered target variable is not in your dataset please give valid one")
    elif Target_check=='no':
        unsupervised=True
        print("Still we are doing only for supervised-regression and classification ")
        print("Sorry!!!!")
        sys.exit()
        
    if Target_check == 'yes':
        t=pd.DataFrame(data[target].value_counts())
        unique=t.shape[0]
        if unique<20:
            classification='True'
        else:
            classification='False'
    else:
        classification='False'
        





    #       ----------------useless----------

    
    print("Is your dataset has useless data type 'YES' ???")
    #print("Useless data is unique, discrete data with no potential relationship with the outcome variable.
    #A useless feature has high cardinality.
    #An example would be bank account numbers that were generated randomly.")
    Useless_check=input().lower()
    if Useless_check=='yes':
        print("Please enter the exact names of all useless variables separating spaces")
        
        useless=list(map(str,input().split()))
        gh=len(useless)
        i=0
        while(i<gh):
            if useless[i] in data.columns:
                i+=1
                pass
            else:
                print(str(useless[i])+" column is not in dataset")
                print("Enter Correct column name")
                new=input()

    else:
        pass





    #     ----------------Time------------------


    print("How this automated machine learning model data as ??")
    print(" 1. As Begginer  \n 2. Medium \n 3. Expert ")
    time_check=int(input())
    

    
    # -------------- assign data types  -------------

    
    print(data.dtypes)
    c=assigndatatypes.datatypes(data)
    data=c.apply_data_types()
    print(data.dtypes)



    #    ------------Dealing missing values-----------

    
    m=missing_values.MissingValues(data)
    perc_value=m.missing_percentage()
    if perc_value<=1:
        data=m.per_lessthan_one()
    else:
        data=m.per_greaterthan_one(data)
        print(data.isna().sum())



    #    ----------Data Cleaning -----------
    #removing duplicates

    #      -------------outliers--------------

    
    print("Doing Outlier Analysis")
    n1=data.shape[0]
    out=outliers.Outliers(data)
    data=out.numerical_outliers()
    print(str(n1-data.shape[0])+" rows are removed")


    #     ----------------  Imbalanced data   -------------------

    
    if classification == 'True':
        im=imbalanced_data.imbalanced_data(data)
        data=im.upsample_data(target)
        print(data[target].value_counts())


    #   ------------  Feature engineering -------------

    
    print(data.columns)
    fe=FeatureEngineering.FeatureEngineering(data)
    data=fe.date_time_features()
    print(data.columns)
    data=fe.LabelEncoder()


    #-------------- Visualization --------------
    vi=visualization.Visualization(data,target)
    vi.start_visuals()


    # ----------- Feature Importance ---------

    fi=feature_importance.feature_importance(data,classification)
    fi.find_important_features(target)
    
    #   --------------modeling--------------

    
    selected_columns=[]
    for i in data.columns:
        if i != target and i!='pickup_datetime':
            selected_columns.append(i)
    X_train,X_test,Y_train,Y_test=train_test_split(data[selected_columns],data[target],test_size=0.2)

    if classification == 'False':
        mod=models.Modeling(X_train,Y_train)
        mod.LinReggr()
        mod.LasoReg()
        mod.RidgReg()
        mod.RandForest()
        mod.KNNReg()
        mod.SupVecReg()
        mod.AdaBoost()
        mod.DTR()
    else:
        mod=classification_models.classification_models(X_train,Y_train)
        mod.Logistic_regression()
        mod.DTC()
        mod.RFC()
        mod.SV()
        mod.ABC()
        mod.KNNC()

    makingreport.report()





    
