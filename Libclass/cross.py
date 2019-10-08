import numpy as np

class Cross():
    def __init__(self, x1,x2):
        self.x1=x1
        self.x2=x2
        self.idx=[]

    def cal_cross(self):
        minus=np.array(self.x1)- np.array(self.x2)
        sign=np.sign(minus)
        diff = np.diff(sign)
        idx= np.argwhere(diff).flatten()
        self.idx = idx
        

    #for extracting increasing points
    def up_points(self):
        self.cal_cross()
        up=[]
        if (len(self.idx)!=0):
            try:
                for i in self.idx:
                    if (self.x1[i-1] - self.x1[i+1] > 0):
                        up.append(i)
                return up
            except:
                raise Exception('Some Error Occured!')
        elif(len(self.idx)==0):
            return up
    
    #for extracting descending points
    def down_points(self):
        self.cal_cross()
        down=[]
        if (len(self.idx)!=0):
            try:
                for i in self.idx:
                    if (self.x1[i-1] - self.x1[i+1] < 0):
                        down.append(i)
                return down
            except:
                raise Exception('Some Error Occured!')
        elif(len(self.idx)==0):
            return down        