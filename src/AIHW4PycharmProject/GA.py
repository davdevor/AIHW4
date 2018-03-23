import random
import ANN
import CsvReader
class GA:

    def __init__(self):
        self.attributes = ['studytime','failures','paid','higher','freetime','absences','G1','G2','internet','schoolsup','G3']
        self.popSize = 200
        self.population = []
        self.children = []
        self.fitness = []
        self.weights = 33;
        self.ANN = ANN()
        self.data = CsvReader.readCsv('../student-mat.csv',self.attributes)
        self.results = []

    def computeFitness(self):
        return
    def offspring(self):
        return
    def createNewPopulation(self):
        return
    def mutation(self):
        return

    def initPopulattion(self):
        tempweights = []
        for x in range(self.popSize):
            for y in range(self.weights):
                tempweights.append(random.uniform(0, 1))
            self.population.append(tempweights)
            tempweights=[]

    def runGA(self):
        self.initPopulattion()
        for x in range(self.popSize):
            self.results.append(self.ANN.run(self.population[x],self.data[0]))
        self.computeFitness()
        self.offspring()
        self.createNewPopulation()
        self.mutation()

