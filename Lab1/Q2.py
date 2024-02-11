from os import WIFCONTINUED, name
import random
from cv2 import exp
import matplotlib.pyplot as plt

class Dice : 
    def __init__(self, sides) -> None:
        if(type(sides) is int and sides >= 4) :
            self.sides = sides
            self.probability = [1/self.sides for i in range(self.sides)]
        else :
            raise Exception("Invalid input as the number of faces of the dice")
    
    def __str__(self) -> str:
        return f"Dice with {self.sides} faces and probability distribution {self.probability}\n"

    def setProb(self, probability) -> None :
        if(sum(probability) != 1 and self.sides != len(probability)) :
            raise Exception("Invalid probability distribution")
        else : 
            self.probability = probability
    
    def roll(self, rolls) -> None :
        if(rolls < 0) :
            raise Exception("Rolls cannot be negative")
        
        actual_results = [random.choices(range(1, self.sides + 1), weights=self.probability)[0] for _ in range(rolls)]
        expected_results = [int(rolls * p) for p in self.probability]

        actual_counts = [actual_results.count(i + 1) for i in range(self.sides)]

        x_pts = [str(i+1) for i in range(self.sides)]
        plt.bar(x_pts, expected_results, width=0.3)
        plt.bar(x_pts, actual_counts, width=0.3)
        plt.show()

def main() :
    n = int(input("Enter number of sides : "))
    d = Dice(n)
    setPr = bool(input("Do you want to set probability : "))
    if(setPr) :
        d.setProb(list(map(int, input("Enter the list : "))))
    rolls = int(input("Enter number of rolls :"))
    d.roll(rolls)

if __name__ == "__main__" :
    main()