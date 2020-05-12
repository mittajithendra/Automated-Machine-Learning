class covariance:
    def __init__(self,data):
        self.data=data
    def co_variance(self,data):
        matr=self.data.cov()
        for i in range(len(matr)):
            for j in range(i+1,len(matr)):
                if abs(matr[i][j])>=0.9:
                    print("There is high correlation between "+str(self.data.columns[i])+" "+str(self.data.columns[j]))
                elif abs(matr[i][j])>=0.75:
                    print("There is medium correlation between "+str(self.data.columns[i])+" "+str(self.data.columns[j]))

