import matplotlib.pyplot as plt
import numpy as np 

hfont = { 'fontname': 'Arial'}

w = 0.5
x = ["Canada","USA","Germany (total)"]
bronze = [107,167,203]
silver = [203,319,208]
gold = [315,167,226]

b_bronze = list(np.add(gold,silver))

plt.bar(x,bronze,0.5,bottom=b_bronze,label="Bronze",color="#B1560F")
plt.bar(x,silver,0.5,bottom=gold,label="Silver",color="#C0C0C0")
plt.bar(x,gold,0.5,label="Gold",color="#FFD700")

plt.xlabel("Country", **hfont, fontweight="bold")
plt.ylabel("Number of Medals", **hfont, fontweight="bold")
plt.title("Canada, USA & Germany - Medal Categories", pad=20, **hfont, fontweight="bold")
plt.legend(loc=(1,0.5))
plt.tight_layout()


plt.show()