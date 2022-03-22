import random as rnd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def create_babies(quantity):
    babies = []
   
    for baby in range(quantity):
        age = rnd.randint(0,12)
        if(age >= 3 and age <= 6):
            babies.append((age,rnd.randint(45,60),rnd.randint(2500,7000)))
        elif(age > 6 and age <= 9):
            babies.append((age,rnd.randint(55,70),rnd.randint(5500,10000)))
        elif(age > 9 and age <= 12):
            babies.append((age,rnd.randint(65,90),rnd.randint(8000,13000)))
    return babies

data_3d = create_babies(1000)

Babies = np.array(data_3d)

x, y, z = Babies[:,0], Babies[:,1], Babies[:,2]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, linewidth=0.2)

plt.show()

