"""
Young's Double Slit Experiment

n (number of fringe lines away from optical axis)
a (slit separation)
deltaY (distance along image from optical axis)
s (distance along optical axis from slits to image)

domain = n/a
range = deltaY/s or sin(theta)
"""

# trendline http://stackoverflow.com/questions/26447191/ddg#26447505
import numpy as np
import matplotlib.pyplot as plt

file = "data.csv" # FIXME

# must be a csv
# returns a list of lists
def getData():
    global file
    return list(map(lambda x: x.split(","), filter(lambda y: len(y) != 0, open(file).read().split("\n"))))

# fetch from csv
data = getData()
x = list(map(lambda x: float(x[0]), data))
y = list(map(lambda x: float(x[1]), data))

# map though to get the actual range
x = list(map(lambda x: x/.00025, x))
y = list(map(lambda x: x/.787, y))
print(x)
print(y)

# plot points
plt.scatter(x, y)

# calc the trendline
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x))
plt.xlabel("n/a")
plt.ylabel("Δy/s")

# plt.title(f"Double Slit (wavelength = {wavelength})") # FIXME
plt.grid(True)
plt.savefig("plot.png") # FIXME
plt.clf()
plt.cla()
plt.close()
