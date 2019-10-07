class Moving_Averages():
    
    def __init__(self, data, n=14):
        self.data=data
        self.n=n


    def moving_average(self):
        mylist=[]
        for i in range(0,self.n):
            mylist.append(0)
        
        for j in self.data:
            mylist.append(j)

        cumsum, moving_aves = [0], []
        for i, x in enumerate(mylist, 1):
            cumsum.append(cumsum[i-1] + x)
            if i>=self.n:
                moving_ave = (cumsum[i] - cumsum[i-self.n])/self.n
                #can do stuff with moving_ave here
                moving_aves.append(moving_ave)
            
        return moving_aves
