import GA
import ANN
import CsvReader
import random
import math
if False:
    numAttributes = ['studytime','failures','freetime','absences','G1','G2','G3']
    textAttributes = ['paid','higher','internet','schoolsup']
    weights = [0.4701502836492245, 0.044561420712619246, 0.12844856111853595, -0.22342277034182453, -0.12649673949962623, -0.38236255279786024, 0.31104734643737636, 0.11179174102842844, 0.17690482039896122, 0.365012282203362, -0.11630397836372933, -0.032971488656108924, -0.4317009766145076, 0.2135046280006803, -0.14206749640895586, 0.5660612143525097, 0.10882312284938613, 0.38219272104430174, -0.5354582304817935, 0.1619501166544922, 0.03117843987596275, -0.25656185127914555, -0.1379596023289291, -0.015430053466958341, 0.20302530718283407, 0.6022015779599821, 0.3188119505905276, 0.04944052556014958, 0.13004320060260116, -0.47450320800048906, 0.2864573960306575, 0.06244569296271277, -0.4073041857978574, -0.30583099348628917, 0.3310645964759315, -0.31170136257302505, 0.052277080411689915, -0.3207052109504318, -0.013927568733407829, 0.17832670737960085, -0.3779445345599534, 0.08220828002785713, -0.1168117647076316, 0.16985038510325848, 0.11728818611276338, 0.36455979873242333, -0.1338508624052636, 0.34717120192479267, 0.18103465917645833, -0.2541455370432432, -0.2876834887451234, 0.42231653379475104, -0.3578770274794049, 0.13128144118739207, 0.2760596044129886]

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