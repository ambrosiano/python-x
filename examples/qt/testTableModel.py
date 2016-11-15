from tables import TableModel
from PyQt4.QtCore import *

data = [["one","two","three"],\
        ["four","five","six"],\
        ["seven","eight","nine"]]

headers = ["A","B","C"]

tmodel = TableModel(data,headers)
v = tmodel.data(tmodel.index(0,1))

print("nrows = "+str(tmodel.rowCount(None)))
print("ncols = "+str(tmodel.columnCount(None)))
print("data at [0][1] = "+ v.toString())
