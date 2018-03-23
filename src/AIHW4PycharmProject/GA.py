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
        for x in range(self.popSize):
            fitness = float(self.results[x][1]-self.results[x][0])
            self.fitness.append(fitness)

    def offspring(self):
        prior = 0.0
        index = 0
        count = 0
        averagefitness = self.averageFitness
        r = random.uniform(0,1)
        prior = self.fitness[0] / averagefitness
        self.fitness[0] = prior
        for i in range(1,self.popSize):
            self.fitness[i] = (float(self.fitness[i])/averagefitness) + prior
            prior = self.fitness[i]

        self.fitness[self.popSize-1] = float(self.popSize+1)
        while(count<self.popSize):
            if(r<self.fitness[index]):
                self.children[index] += 1
                count += 1
                r += 1.0
            else:
                index += 1.0

    def createNewPopulation(self):
        index = 0
        temppopulation = []
        for i in range(self.popSize):
            for j in range(self.children[i]):
                temppopulation[index] = self.population[i]
                index += 1
        self.population = temppopulation

    def mutation(self):
        return

    def initPopulattion(self):
        tempweights = []
        for x in range(self.popSize):
            for y in range(self.weights):
                tempweights.append(random.uniform(0, 1))
            self.population.append(tempweights)
            tempweights=[]

    def clear(self):
        self.fitness.clear()
        self.results.clear()
        self.children.clear()

    def runGA(self):
        self.initPopulattion()

        for x in range(self.popSize):
            output = [self.ANN.run(self.population[x],self.data[0]), self.data[0]['G3']]
            self.results.append(output)
        self.computeFitness()
        self.offspring()
        self.createNewPopulation()
        self.mutation()
        self.clear()

