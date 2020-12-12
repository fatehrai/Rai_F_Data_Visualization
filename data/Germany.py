import matplotlib.pyplot as plt
import numpy as np 

x = np.array(["USA","CAN","NOR","URS","FIN","GER (total)"])
y = np.array([653,625,457,440,434,627])



plt.bar(x, y, width = 0.5)
plt.xlabel("Country")
plt.ylabel("Number of Medals")
plt.title("Germany Medal Total Compared To Top Five Countries With Highest Medal Totals")
plt.show()