import pandas as pd
import random as rn
import numpy  as np

lst = ['robot'] * 10
lst += ['human'] * 10
rn.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

data_numpy = data.to_numpy()

OBJs = []
for i in data_numpy:
    if i[0] not in OBJs:
        OBJs.append(i[0])

setFlag = [[0] * len(OBJs) for i in range(len(data))]

for i in range(len(data_numpy)):
    setFlag[i][OBJs.index(data_numpy[i][0])] = 1

print(OBJs)
for i in setFlag:
    print(i)