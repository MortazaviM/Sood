class Moving_Averages():
    
    def __init__(self, data,date, n=14):
        self.data=data
        self.date=date
        self.n=n


    def moving_average(self):
        mylist=[]
        mydate=[]
        for i in range(0,self.n):
            mylist.append(0)
            mydate.append(0)

        for k,j in enumerate( self.data):
            mylist.append(j)
            mydate.append(self.date[k])

        cumsum, moving_aves = [0], []
        for i, x in enumerate(mylist, 1):
            cumsum.append(cumsum[i-1] + x)
            if i>=self.n*2:
                #cumsum.append(cumsum[i-1] + x)
                moving_ave = round((cumsum[i] - cumsum[i-self.n])/self.n ,2)
                #can do stuff with moving_ave here
                moving_aves.append(
                    {
                        'x':mydate[i-1],
                        'y':moving_ave,
                        })
            
        return moving_aves