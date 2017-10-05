import csv
class ReadFileCSV:
    __a=[]
    __y=[]
    def __init__(self,filname):
        self.a=[]
        self.y=[]
        self.filename=filname
    def read_file(self):
        with open(self.filename,'r') as csvfile:
            reader=csv.DictReader(csvfile)
            for row in reader:
                temp=[]
                temp.append(float(row['lcavol']))
                temp.append(float(row['lweight']))
                temp.append(float(row['age']))
                temp.append(float(row['lbph']))
                temp.append(float(row['svi']))
                temp.append(float(row['lcp']))
                temp.append(float(row['gleason']))
                temp.append(float(row['pgg45']))
                self.a.append(temp)
                self.y.append(float(row['lpsa']))
    def get_x(self):
        return self.a
    def get_y(self):
        return self.y
    def compute_y(self,w):
        temp=[]

        for i in self.a:
            sum = w[0]
            for j in range(1,len(w)):
                sum+=w[j]*i[j-1]
            temp.append(sum)
        return temp
