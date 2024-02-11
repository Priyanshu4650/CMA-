from random import uniform
from math import pi
from matplotlib import pyplot as plt

def estimatePi(n) -> None :
    fraction4List = []
    pointsGenerated = []
    pointsInCircle = 0

    for i in range(1, n + 1) :        
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        
        if(x*x + y*y  <= 1) :
            pointsInCircle += 1

        fraction4List.append((4*(pointsInCircle))/(i+1))
        pointsGenerated.append(i+1)
    
    plt.plot(pointsGenerated, fraction4List)
    plt.axhline(y = pi)
    plt.show()

estimatePi(2000000)
