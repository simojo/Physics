# running domain through eq to get a range http://stackoverflow.com/questions/14000595/ddg#14000631
import numpy as np
import matplotlib.pyplot as plt

## Objects ##
class Function:
    def __init__(self, function):
        self.function = function
        self.title = function.__name__.replace("_", " ")

class Plot:
    def __init__(self, functions, domain, title, xLabel, yLabel, path):
        self.functions = functions
        self.domain = domain
        self.title = title
        self.xLabel = xLabel
        self.yLabel = yLabel
        self.path = path
    def graphEverything(self):
        x = np.array(self.domain)
        for func in self.functions:
            y = func.function(x)
            plt.plot(x, y, label=func.title)
            # NOTE: to switch bounds -> plt.xlim(max(x), min(x))
        plt.title(self.title)
        plt.legend()
        plt.grid(True)
        plt.savefig(self.path)
        plt.clf()
        plt.cla()
        plt.close()

## Functions ##
def Hyperbola(x):
    return x ** 2

def Rational(x):
    return 1/x

def Linear(x):
    return x

## Execution ##
myPlot = Plot(
    functions = [
        Function(
            function = Hyperbola,
        ),
        Function(
            function = Rational,
        ),
        Function(
            function = Linear,
        )
    ],
    domain = np.linspace(-10, 10, 100),
    title = "Graph",
    xLabel = "x",
    yLabel = "y",
    path = "plot.png")

myPlot.graphEverything()
