import matplotlib.pyplot as plt
import numpy as np 

hfont = { 'fontname': 'Arial'}

x = np.array(["USA","CAN","NOR","URS","FIN","GER (total)"])
y = np.array([653,625,457,440,434,627])



plt.bar(x, y, width = 0.5,color=['#FEF770', '#FEF770', '#FEF770', '#FEF770', '#FEF770', '#FF4A4A'])
plt.xlabel("Country", **hfont)
plt.ylabel("Number of Medals", **hfont)
plt.title("Germany Medal Total Compared To Top Five Countries", pad=20, **hfont, fontweight="bold")
plt.show()