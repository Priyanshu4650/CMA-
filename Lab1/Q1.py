from matplotlib import pyplot as plt
import math

def stringling(n) -> None :
    fact = []
    rhs = []
    x_pts = []

    for i in range(1, n) :
        x_pts.append(i)
        if(len(fact) == 0) :
            fact.append(math.log(i))
        else : 
            fact.append(fact[-1] + math.log(i))
        
        rhs.append(1/2 * math.log(2 * math.pi * i) + i * math.log(i/math.e))

    plt.plot(x_pts, fact, color = "b")
    plt.plot(x_pts, rhs, color = "r")
    plt.show()

stringling(10**6)