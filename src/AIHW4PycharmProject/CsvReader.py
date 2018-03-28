import csv

# this method reads in the csv file using DictReader
# it get the attributes you specify
def readCsv(fileName,numattributes,textAttributes):
    file = open(fileName,mode='r',encoding='UTF-8')
    reader = csv.DictReader(file, delimiter=';')
    records = []
    tempDict = {}
    for x in reader:
        for y in numattributes:
            tempDict[y] = float(x[y])
        for y in textAttributes:
            tempDict[y] = 0.0 if x[y] == 'no' else 1.0
        records.append(tempDict)
        tempDict = {}
    return records
