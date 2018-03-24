import GA
import ANN
import CsvReader
import random
import math
if False:
    numAttributes = ['studytime','failures','freetime','absences','G1','G2','G3']
    textAttributes = ['paid','higher','internet','schoolsup']
    weights = [0.8755253954197162, 0.7933074737299409, 0.4060388687709796, 0.49640097363811014, 0.2988049521486095, 0.7317725421885751, 0.7205453921679031, 0.352287739342662, 0.7982645112414873, 0.1397671525214271, 0.8789885102504448, 0.4890336636461206, 0.017120842505644034, 0.39864770445933295, 0.7903416130083821, 0.6930685540109243, 0.7853496439256843, 0.9237066359283476, 0.6241476230055631, 0.5166958058113295, 0.0391600197521525, 0.6068306716244464, 0.431624226711243, 0.6192138566221438, 0.6282085876907267, 0.4915688326187934, 0.6329567508163578, 0.3989468578347914, 0.06511543537747946, 0.21373603018788026, 0.1494376907330493, 0.07488037623597342, 0.01690764298276953]

    data = CsvReader.readCsv('../student-mat.csv',numAttributes,textAttributes)
    nn = ANN.ANN()
    tempattributes = numAttributes
    tempattributes.remove("G3")
    for x in textAttributes:
        tempattributes.append(x)
    for i in range(20):
        output = nn.run(weights, data[i], tempattributes)
        print(output)
        print(data[i]['G3'])
else:
    x = GA.GA()
    x.runGA()