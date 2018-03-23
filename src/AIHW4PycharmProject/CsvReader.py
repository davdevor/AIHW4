import csv
#the 10 attributes im using studytime, failures,paid,higher,freetime,absences,G1,G2,internet,schoolsup
def readCsv(fileName):
    file = open(fileName,mode='r',encoding='UTF-8')
    reader = csv.DictReader(file, delimiter=';')
    attributes = ['studytime','failures','paid','higher','freetime','absences','G1','G2','internet','schoolsup','G3']
    records = []
    tempDict = {}
    for x in reader:
        for y in attributes:
            tempDict[y] = x[y]
        records.append(tempDict)
        tempDict = {}
    return records
