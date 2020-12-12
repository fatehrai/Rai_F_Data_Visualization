import matplotlib.pyplot as plt 

hfont = { 'fontname': 'Arial'}

x1 = [1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1994,1998,2002,2006,2010,2014]
y1 = [112,83,110,99,125,118,123,108,139,153,155,159,167,168,201,226,232,258,273,299,296,340]

plt.plot(x1, y1, label="Men", color="#FFC500")

x2 = [1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1994,1998,2002,2006,2010,2014]
y2 = [6,6,6,9,15,18,27,39,46,46,45,51,51,54,63,99,111,189,208,232,233,272]

plt.plot(x2, y2, label="Women", color="#44DAFF")

plt.xlabel('Year', **hfont)
plt.ylabel('Number of Medals', **hfont)
plt.title('Trajectory Of Medals Won By Men And Women: 1924-2014', pad=20, **hfont, fontweight="bold")
plt.legend()
plt.show()