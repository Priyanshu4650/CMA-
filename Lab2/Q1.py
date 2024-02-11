from math import inf
from matplotlib import pyplot as plt

class UndirectedGraph :
    def __init__(self, nodes = inf) -> None:
        self.nodes = nodes
        self.edges = 0
        self.adjacenyList = {}
        if(self.nodes != inf) :
            for i in range(1, self.nodes + 1) :
                self.adjacenyList[i] = []

    def addNode(self, node) -> None :
        if(node > self.nodes) :
            raise Exception("Node index cannot exceed number of nodes")
        if(node not in self.adjacenyList) :
            self.adjacenyList[node] = []
    
    def addEdge(self, edge) -> None :
        a = edge[0]
        b = edge[1]

        if a not in self.adjacenyList :
            self.adjacenyList[a] = []
        if b not in self.adjacenyList :
            self.adjacenyList[b] = []
        
        self.adjacenyList[a].append(b)
        self.adjacenyList[b].append(a)
        self.edges += 1
    
    def __add__(self, object):
        if isinstance(object, int):
            self.addNode(object)
        elif isinstance(object, tuple) and len(object) == 2:
            self.addEdge(object)
        else:
            raise Exception("Invalid operation.")

        return self

    def __str__(self) :
        s = f"Graph with {len(self.adjacenyList)} nodes and {self.edges} edges. Neighbours of the nodes are belows :\n"
        for i in self.adjacenyList :
            s += f"Node {i} : {self.adjacenyList[i]}\n"
        return s
    
    def plotDegDist(self):
        plt.title("Node Degree Distribution")
        plt.xlabel("Node degree")
        plt.ylabel("Fraction of nodes")

        # Calculating degree distribution
        degreeDist = {}
        for val in self.graph.values():
            degree = len(val)
            if degree not in degreeDist:
                degreeDist[degree] = 0
            degreeDist[degree] += 1

        x = []
        y = []

        avgDegree = 0  # Average degree of node

        for i in range(self.numNodes):
            x.append(i)
            if i in degreeDist:
                avgDegree += i*degreeDist[i]
                y.append(degreeDist[i] / self.numNodes)
            else:
                y.append(0)

        avgDegree /= self.numNodes

        plt.plot(x, y, 'ob', label="Actual degree distribution", zorder=0)
        plt.axvline(x=avgDegree, color='red', label='Average node degree')
        plt.legend()
        plt.grid(zorder=1)
        plt.show()
        
g = UndirectedGraph()
g = g + 100
g = g + (1, 2)
g = g + (1, 100)
g = g + (100, 3)
g = g + 20
print(g)