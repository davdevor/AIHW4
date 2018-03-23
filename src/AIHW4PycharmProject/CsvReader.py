import csv
def readCsv(fileName,attributes):
    file = open(fileName,mode='r',encoding='UTF-8')
    reader = csv.DictReader(file, delimiter=';')
    records = []
    tempDict = {}
    for x in reader:
        for y in attributes:
            tempDict[y] = x[y]
        records.append(tempDict)
        tempDict = {}
    return records
