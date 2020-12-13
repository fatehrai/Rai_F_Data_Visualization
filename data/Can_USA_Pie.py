import matplotlib.pyplot as plt

hfont = { 'fontname': 'Arial'}

values = [625,653]
labels = ["Canada", "USA"]
colors = ["#ff0000", "#5B8CDB"]

explode = [0, 0.1]


plt.pie(values, labels=labels, colors=colors, explode=explode, autopct = '%2.1f%%')
plt.title("Canada & USA Total Medal Comparison", pad=20, **hfont, fontweight="bold")
plt.legend(loc= 'upper left')
# generate pie chart
plt.show()