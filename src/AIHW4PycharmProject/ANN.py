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
        self.num_layers = 3
        self.nodes_per_layer = 10
        self.layers = self.init_layers()

    def init_nodes(self):
        nodes = []
        for x in range(self.nodes_per_layer):
            weights = []
            for y in range(self.nodes_per_layer):
                weights.append(0)
            node = Perceptron(weights)
            nodes.append(node)
            weights = []
        return nodes

    # ssets up the layers and initilizes nodes in each layer
    def init_layers(self):
        layers = []
        for x in range(self.num_layers):
            layers.append(self.init_nodes())
        layers.append(Perceptron([0  for x in range(self.nodes_per_layer)]))
        return layers

    def run(self,weights,data,attributes):
        temp = []
        tempweights = []
        # get input for first layer
        for y in range(len(attributes)):
            temp.append(data[y])

        output = []
        #execute layers
        for z in range(len(self.layers)-1):
            for x in range(len(self.layers[z])):
                self.layers[z][x].setActivation(temp)
                # get the weights connected to that node
                for i in range(0+x*(z+1),len(weights)-self.nodes_per_layer,self.nodes_per_layer):
                    tempweights.append(weights[i])
                self.layers[z][x].activatePerceptron(tempweights,len(attributes))
                tempweights =[]
                output.append(self.layers[z][x].getOutput())
            temp = output
            output = []

        j = 0
        # output node
        for x in range(len(weights)-1,len(weights)-self.nodes_per_layer-1,-1):
            tempweights.append(weights[x])
            #tempweights.append(weights[x]*output[j])
            j+=1
        self.layers[-1].setActivation(tempweights)
        self.layers[-1].activatePerceptron(tempweights,len(temp))

        # this is sthe output of the final node
        return self.layers[-1].getOutput()
