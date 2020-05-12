from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import GridSearchCV


class Modeling:
    def __init__(self,exec_data_X,exec_data_Y):
        self.exec_data_X=exec_data_X
        self.exec_data_Y=exec_data_Y
    def LinReggr(self):
        lr=LinearRegression()
        lr=lr.fit(self.exec_data_X,self.exec_data_Y)
        print("Score for Linear Regression",end=" ")
        print(lr.score(self.exec_data_X,self.exec_data_Y))

    def LasoReg(self):
        la=Lasso(alpha=1.0)
        la=la.fit(self.exec_data_X,self.exec_data_Y)
        print("Score for Lasso Regression",end=" ")
        print(la.score(self.exec_data_X,self.exec_data_Y))
        
    def RidgReg(self):
        r=Ridge(alpha=1.0, fit_intercept=True, normalize=False, copy_X=True, max_iter=None, tol=0.001, solver='auto', random_state=None)
        r=r.fit(self.exec_data_X,self.exec_data_Y)
        print("Score for Ridge Regression",end=" ")
        print(r.score(self.exec_data_X,self.exec_data_Y))
        
    def RandForest(self):
        RF=RandomForestRegressor()
        parameters={'n_estimators':[80,90,100,120],'min_samples_leaf':[1,3,5,7],'max_features':('auto','sqrt','log2'),'max_depth':[2,4,6,8,12]}
        clf=GridSearchCV(RF,parameters)
        clf=clf.fit(self.exec_data_X,self.exec_data_Y)
        print("Score for Random Forest",end=" ")
        print(clf.score(self.exec_data_X,self.exec_data_Y))
        
    def KNNReg(self):
        knnrg=KNeighborsRegressor()
        min_max_scaler=MinMaxScaler()
        knnrg=knnrg.fit(min_max_scaler.fit_transform(self.exec_data_X),self.exec_data_Y)
        print("Score for KNN",end=" ")
        print(knnrg.score(min_max_scaler.fit_transform(self.exec_data_X),self.exec_data_Y))
        
    def SupVecReg(self):
        su=SVR()
        parameters={'kernel':('linear','rbf'),'C':[1,3,5,7,10]}
        clf=GridSearchCV(su,parameters)
        clf=clf.fit(self.exec_data_X,self.exec_data_Y)
        print("Score for Support Vector Regression",end=" ")
        print(clf.score(self.exec_data_X,self.exec_data_Y))
        
    def AdaBoost(self):
        regr=AdaBoostRegressor()
        parameters={'loss':('linear','square','exponential'),'n_estimators':[30,40,50,60,70],'random-state':[2]}
        clf=GridSearchCV(regr,parameters)
        clf=clf.fit(self.exec_data_X,self.exec_data_Y)
        print("Score for Ada Boost",end=" ")
        print(clf.score(self.exec_data_X,self.exec_data_Y))
        
    def DTR(self):
        dt=DecisionTreeRegressor()
        dt=dt.fit(self.exec_data_X,self.exec_data_Y)
        print("Score for Decision Tree Regressor",end=" ")
        print(dt.score(self.exec_data_X,self.exec_data_Y))
    




        
