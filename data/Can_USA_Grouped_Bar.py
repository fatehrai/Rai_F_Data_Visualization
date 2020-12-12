import matplotlib.pyplot as plt
import numpy as np 

hfont = { 'fontname': 'Arial'}

w = 0.2
x = ["Canada","USA"]
bronze = [107,167]
silver = [203,319]
gold = [315,167]

bar1 = np.arange(len(x))
bar2 = [i+w for i in bar1]
bar3 = [i+w for i in bar2]

plt.bar(bar1,bronze,0.2,label="Bronze",color="#B1560F",edgecolor="black")
plt.bar(bar2,silver,0.2,label="Silver",color="#C0C0C0",edgecolor="black")
plt.bar(bar3,gold,0.2,label="Gold",color="#FFD700",edgecolor="black")

plt.xlabel("Country")
plt.ylabel("Number of Medals")
plt.title("Canada & USA - Medal Categories", pad=20, **hfont)
plt.xticks(bar1+w,x)
plt.legend()


plt.show()