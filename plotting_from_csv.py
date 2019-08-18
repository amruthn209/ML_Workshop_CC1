import pandas as pd
from matplotlib import pyplot as plt

dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:, 1]
y = dataset.iloc[:, 2]
plt.scatter(x,y,color='r')
plt.xlabel('age')
plt.ylabel('salary')
plt.show()


import collections
from matplotlib import pyplot as plt

b = dataset.iloc[:, 3].values
yes = 0
no = 0
for i in b:
	if i == "Yes" :
		yes+=1
	else:
		no+=1
		
count = collections.Counter(b)
no = count['No']
yes = count['Yes']


plt.bar(1,yes,width=0.5, label="Yes")
plt.bar(2, no, width=0.5, color = 'r', label = "No")
plt.legend()
plt.show()
