import matplotlib.pyplot as plt

hfont = { 'fontname': 'Arial'}

values = [3944,1986]
labels = ["Men", "Women"]
colors = ["#FFC500", "#44DAFF"]

explode = [0, 0.1]


plt.pie(values, labels=labels, colors=colors, explode=explode, autopct = '%2.1f%%')
plt.title("Portions of Total Medals Won by Men & Women", pad=20, **hfont, fontweight="bold")
plt.legend(loc='upper right')
# generate pie chart
plt.show()