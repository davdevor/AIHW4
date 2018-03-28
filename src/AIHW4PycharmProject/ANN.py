import math
class Perceptron:

    def __init__(self,act):
        self.numInputs = len(act)
        self.activation = [x for x in act]
        self.output = 0.0
        self.threshold = 0.0

    def getOutput(self):
        return self.output

    def setActivation(self,act):
        for i in range(len(act)):
            self.activation[i] = act[i]
        self.output = 0.0

    def sigmoid(self,sum):
        return 1.0 / (1.0 + math.exp(sum*-1))

    def activatePerceptron(self,weights=0, numInputs=0):
        sum = 0.0
        for i in range(0, numInputs):
            sum += weights[i] * self.activation[i]
        self.output = self.sigmoid(sum)


class ANN:
    def __init__(self):
        self.nodes = [Perceptron([0 for x in range(10)]) for x in range(6)]

    def run(self,weights,data,attributes):
        temp = []
        tempweights = []
        numnodes = len(self.nodes)-1
        for x in range(numnodes):
            for y in range(len(attributes)):
                temp.append(data[y])
            self.nodes[x].setActivation(temp)
            for y in range(0+x,len(weights)-numnodes,numnodes):
                tempweights.append(weights[y])
            self.nodes[x].setActivation(temp)
            self.nodes[x].activatePerceptron(tempweights,len(attributes))
            temp = []
            tempweights =[]
        output = []
        for x in range(numnodes):
            output.append(self.nodes[x].getOutput())

        j = 0
        # output node
        for x in range(len(weights)-1,len(weights)-numnodes-1,-1):
            tempweights.append(weights[x])
            #tempweights.append(weights[x]*output[j])
            j+=1
        #output = 0.0
        #for x in tempweights:
            #output+=x
        #return output
        self.nodes[-1].setActivation(output)
        self.nodes[-1].activatePerceptron(tempweights,len(output))

        return self.nodes[-1].getOutput()
