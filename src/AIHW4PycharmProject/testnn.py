# This is just me seeing if I could get the Neural Net to predict the grades using sklearn
# Multi Layer Perceptron Classifier


import CsvReader
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier


def test():
    numAttributes = ['studytime','failures','freetime','absences','G1','G2','G3']
    textAttributes = ['paid','higher','internet','schoolsup']
    data = CsvReader.readCsv('../student-mat.csv',numAttributes,textAttributes)
    ans = []
    tempattributes = numAttributes
    tempattributes.remove("G3")
    for x in textAttributes:
        tempattributes.append(x)
    temp_data = []
    temp_list = []
    temp_ans = []
    for x in data:
        for y in tempattributes:
            temp_list.append(x[y])
        temp_ans.append(x['G3'])
        temp_data.append(temp_list)
        temp_list = []
    ans = temp_ans
    data = temp_data
    scaler = StandardScaler()
    scaler.fit(data)
    data = scaler.transform(data)

    mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=10000)
    mlp.fit(data,ans)

    count = 0
    for x in range(len(data)):
        predict = mlp.predict([data[x]])
        if predict[0] == ans[x]:
            count+=1
        print(predict[0])
        print(ans[x])
    print(count / len(data))