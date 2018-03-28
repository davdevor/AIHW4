import random
import ANN
import CsvReader
import sys
from sklearn.preprocessing import StandardScaler

class GA:

    def __init__(self):
        self.numAttributes = ['studytime','failures','freetime','absences','G1','G2','G3']
        self.textAttributes = ['paid','higher','internet','schoolsup']
        self.popSize = 20
        self.population = []
        self.children = [0 for x in range(self.popSize)]
        self.fitness = []
        self.weights = 55;
        self.ANN = ANN.ANN()
        self.data = CsvReader.readCsv('../student-mat.csv',self.numAttributes,self.textAttributes)
        self.results = []
        self.averageFitness = 0.0
        self.best = sys.maxsize

    def getOutput(self,num):
        x = .05
        for y in range(1, 20):
            if num < x:
                return y
            else:
                x = .05 * (y+1)
        return 20
    def computeFitness(self):
        i = 0
        for x in self.results:
            fitness = 0.0
            for y in x:

                t1 = y[1]
                t2 = self.getOutput(y[0])
                fitness += abs(float(t1-t2))
            fitness /= (len(x))

            if(fitness < self.best):
                self.best = fitness
                print(self.population[i])
                print(fitness)
            self.averageFitness += fitness
            self.fitness.append(fitness)
            i+=1
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
    # this method randomly mutates the population by adding or subtracting a value to
    def mutation(self):

        for x in self.population:
            numchanges = random.randint(1, 33)
            for y in range(numchanges):
                # popsition to change
                pos = random.randint(0,self.weights-1)
                # how much to change by
                change = random.uniform(0, .001)
                # if 1 add else subtract
                operator = random.randint(0, 1)
                if(operator == 1):
                    x[pos] += change
                else:
                    x[pos] -= change

    # initializes the population to random values
    def initPopulattion(self):
        tempweights = []
        for x in range(self.popSize):
            for y in range(self.weights):
                tempweights.append(random.uniform(-.001, .001))
            self.population.append(tempweights)
            tempweights=[]

    # this method clears data that needs to be reset
    def clearData(self):
        self.fitness.clear()
        self.results.clear()
        for x in range(self.popSize):
            self.children[x] = 0
        self.averageFitness = 0.0

    def runGA(self):
        self.initPopulattion()
        tempattributes = self.numAttributes
        tempattributes.remove("G3")
        for x in self.textAttributes:
            tempattributes.append(x)
        temp_data = []
        temp_list = []
        temp_ans = []
        for x in self.data:
            for y in tempattributes:
                temp_list.append(x[y])
            temp_ans.append(x['G3'])
            temp_data.append(temp_list)
            temp_list = []
        self.ans = temp_ans
        self.data = temp_data
        scaler = StandardScaler()
        scaler.fit(self.data)
        self.data = scaler.transform(self.data)

        for iterations in range(1000):
            output = []
            for x in range(self.popSize):
                for i in range(int(len(self.data) * .7)):
                    output.append([self.ANN.run(self.population[x], self.data[i], tempattributes), self.ans[i]])
                self.results.append(output)
            self.computeFitness()
            self.offspring()
            self.createNewPopulation()
            self.mutation()
            self.clearData()

