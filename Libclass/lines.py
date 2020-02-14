class HorizontalLines():
    def __init__(self, data, window):
        self.data=data
        self.window= window

    def find_Resistance_point(self):
        cal = len(self.data) % self.window
        if cal>0:
            added_zeros = self.window-(len(self.data) % self.window)
        else:
            added_zeros = (len(self.data) % self.window)
    
        zeros = [0]*added_zeros
        for k in self.data:
            zeros.append(k)

        max_points=[]
        max_list_dicts=[]
        number_of_window=int(len(zeros)/self.window)
        for i in range(0, number_of_window):
            max_points.append(max(zeros[i*self.window:(i+1)*self.window]))
            max_list_dicts.append({
                'value':max(zeros[i*self.window:(i+1)*self.window]),
                'color':'red',
                'dashStyle': 'shortdash',
            })
        
        return max_points,max_list_dicts


    def find_Support_point(self):
        cal = len(self.data) % self.window
        if cal>0:
            added_zeros = self.window-(len(self.data) % self.window)
        else:
            added_zeros = (len(self.data) % self.window)
    
        zeros = [999999999999]*added_zeros
        for k in self.data:
            zeros.append(k)

        min_points=[]
        min_list_dicts=[]
        number_of_window=int(len(zeros)/self.window)
        for i in range(0, number_of_window):
            min_points.append(min(zeros[i*self.window:(i+1)*self.window]))
            min_list_dicts.append({
                'value':min(zeros[i*self.window:(i+1)*self.window]),
                'color':'green',
                'dashStyle': 'shortdash',
            })
        
        return min_points,min_list_dicts


    