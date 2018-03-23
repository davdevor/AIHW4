import random
import ANN
import CsvReader


class GA:

    def __init__(self):
        self.attributes = ['studytime','failures','paid','higher','freetime','absences','G1','G2','internet','schoolsup','G3']
        self.popSize = 200
        self.population = []
        self.children = [0 for x in range(self.popSize)]
        self.fitness = []
        self.weights = 33;
        self.ANN = ANN.ANN()
        self.data = CsvReader.readCsv('../student-mat.csv',self.attributes)
        self.results = []
        self.averageFitness = 0.0

    def computeFitness(self):
        for x in range(self.popSize):
            t1 = int(self.results[x][1])
            t2 = self.results[x][0]
            fitness = float(t1-t2)
            self.averageFitness += fitness
            self.fitness.append(fitness)
        self.averageFitness /= self.popSize

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
                index += 1

    def createNewPopulation(self):
        index = 0
        temppopulation = []
        for i in range(self.popSize):
            for j in range(self.children[i]):
                temppopulation.append(self.population[i])
                index += 1
        self.population = temppopulation

    def mutation(self):
        for x in self.population:
            numchanges = random.randint(1, 33)
            for y in range(numchanges):
                # popsition to change
                pos = random.randint(0,self.weights-1)
                # how much to change by
                change = random.uniform(0, 1)
                # if 1 add else subtract
                operator = random.randint(0, 1)
                if(operator == 1):
                    x[pos] += change
                else:
                    x[pos] -= change

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
        self.averageFitness = 0.0

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

