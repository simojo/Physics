# trendline http://stackoverflow.com/questions/26447191/ddg#26447505
import numpy as np
import matplotlib.pyplot as plt

file = "data.csv" # FIXME

# must be a csv
# returns a list of lists
def getData():
    global file
    return list(map(lambda x: x.split(","), filter(lambda y: len(y) != 0, open(file).read().split("\n"))))

data = getData()
x = list(map(lambda x: int(x[0]), data))
y = list(map(lambda x: int(x[1]), data))
print(x)
print(y)

# plot points
plt.scatter(x, y)

# calc the trendline
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x))
plt.xlabel("x")
plt.ylabel("y")

plt.title("title") # FIXME
plt.grid(True)
plt.savefig("plot.png") # FIXME
plt.clf()
plt.cla()
plt.close()
