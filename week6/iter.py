from ctypes import sizeof
from operator import index, indexOf
from os import lstat, name
import pandas as pd

file  = "./unisex_navne.xls"

dts = pd.read_excel(file, header=None)

dts = dts.squeeze()
list_of_names = dts.tolist()

#name_comprehensive = (name for name in dts.iloc[:,0])

#for n in name_comprehensive:
    #print(n)


def my_names(names):
   num = 0
   while num < len(names):
       yield names[num]
       num += 1

name_list_gen = my_names(list_of_names)


#sizeof(dts)
print(next(name_list_gen))
print(next(name_list_gen))