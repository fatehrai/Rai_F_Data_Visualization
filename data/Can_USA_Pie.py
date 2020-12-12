import matplotlib.pyplot as plt

values = [625,653]
labels = ["Canada", "USA"]
colors = ["#ff0000", "#002868"]


plt.pie(values, labels=labels, colors=colors, autopct = '%2.1f%%')
plt.title("Canada & USA Total Medal Comparison")
# generate pie chart
plt.show()