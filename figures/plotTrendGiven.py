# trendline http://stackoverflow.com/questions/26447191/ddg#26447505
import numpy as np
import matplotlib.pyplot as plt

file = "data.csv" # FIXME

# must be a csv
# returns a list of lists
def getData():
    global file
    return map(lambda x: x.split(","), open(file).read().split("\n"))

data = getData
x = map(lambda x: x[0], data)
y = map(lambda x: x[1], data)

# plot points
plt.scatter(x, y)

# calc the trendline
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x))

plt.title("title") # FIXME
plt.grid(True)
plt.savefig("plot.png") # FIXME
plt.clf()
plt.cla()
plt.close()
