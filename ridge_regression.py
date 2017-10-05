from read_file_excell import ReadFileCSV
import numpy

readfile_csv=ReadFileCSV("1-prostate-training-data.csv")
readfile_csv.read_file()
a=readfile_csv.get_x()
y=readfile_csv.get_y()
#print(a)
#print (y)
A=numpy.array(a)
y=numpy.array(y)
I=numpy.identity(9)
A_nv=numpy.linalg.inv(A)
print A_nv


