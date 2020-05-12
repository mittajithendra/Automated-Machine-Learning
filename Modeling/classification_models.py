from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler


class classification_models:
    def __init__(self,exec_X,exec_Y):
        self.exec_X=exec_X
        self.exec_Y=exec_Y
    def Logistic_regression(self):
        log_reg=LogisticRegression()
        parameters={'penalty':('l2','l1'),'C':[0.5,1,1.5,0.3],'max_iter':[200]}
        clf=GridSearchCV(log_reg,parameters)
        clf=clf.fit(self.exec_X,self.exec_Y)
        print("Score for Loggistic Regression :",end=" ")
        print(clf.score(self.exec_X,self.exec_Y))
    def DTC(self):
        dt=DecisionTreeClassifier()
        parameters={'criterion':('entropy','gini'),'max_depth':[30,50,80,100],'max_features':('auto','sqrt','log2')}
        clf=GridSearchCV(dt,parameters)
        clf=clf.fit(self.exec_X,self.exec_Y)
        print("Score for Decision Tree Classifier :",end=" ")
        print(clf.score(self.exec_X,self.exec_Y))
    def RFC(self):
        rf=RandomForestClassifier()
        parameters={'n_estimators':[70,90,100,120,150],'criterion':('entropy','gini'),'max_features':('auto','sqrt','log2')}
        clf=GridSearchCV(rf,parameters)
        clf=clf.fit(self.exec_X,self.exec_Y)
        print("Score for Random Forest Classifier :",end=" ")
        print(clf.score(self.exec_X,self.exec_Y))
    def SV(self):
        sv=SVC()
        parameters={'C':[1,2],'kernel':('rbf','linear','sigmoid','poly'),'gamma':('scale','auto')}
        clf=GridSearchCV(sv,parameters)
        clf=clf.fit(self.exec_X,self.exec_Y)
        print("Score for Support Vector Classifier :",end=" ")
        print(clf.score(self.exec_X,self.exec_Y))
    def ABC(self):
        dtc=DecisionTreeClassifier(max_depth=7)
        ab=AdaBoostClassifier(base_estimator=dtc)
        ab.fit(self.exec_X,self.exec_Y)
        print("Score for Ada Boost Classifier :",end=" ")
        print(ab.score(self.exec_X,self.exec_Y))
    def KNNC(self):
        knn=KNeighborsClassifier()
        min_max_scaler=MinMaxScaler()
        parameters={'algorithm':('auto', 'ball_tree', 'kd_tree', 'brute'),'n_neighbors':[2,5,7,10]}
        clf=GridSearchCV(knn,parameters)
        clf=clf.fit(min_max_scaler.fit_transform(self.exec_X),self.exec_Y)
        print("Score for KNN Classifier :",end=" ")
        print(clf.score(min_max_scaler.fit_transform(self.exec_X),self.exec_Y))
        
        
