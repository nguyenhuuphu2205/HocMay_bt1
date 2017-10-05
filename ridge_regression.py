from read_file_excell import ReadFileCSV
from sklearn import linear_model
import numpy
def find_lamda():
    reg = linear_model.RidgeCV(alphas=[0.1,0.2,0.3,0.5,0.8,1.0,1.2,2.0,3.0,10.0])
    readfile_csv = ReadFileCSV("1-prostate-training-data.csv")
    readfile_csv.read_file()
    a = readfile_csv.get_x()
    y = readfile_csv.get_y()
    reg.fit(a, y)
    return  reg.alpha_

def tranning():
    reg = linear_model.Ridge (alpha = find_lamda())
    readfile_csv=ReadFileCSV("1-prostate-training-data.csv")
    readfile_csv.read_file()
    a=readfile_csv.get_x()
    y=readfile_csv.get_y()
    reg.fit(a,y)
    #print(a)
    #print (y)
    A=numpy.array(a)
    y=numpy.array(y)
    I=numpy.identity(9)
    w=[reg.intercept_]
    for i in reg.coef_:
        w.append(i)
    return w
def testing():
    readfile_csv = ReadFileCSV("20143449-test.csv")
    readfile_csv.read_file()
    return readfile_csv.compute_y(tranning())
if __name__=='__main__':
    print(testing())

