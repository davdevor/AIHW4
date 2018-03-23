import csv

def readCsv(fileName):
    file = open(fileName,mode='r',encoding='UTF-8')
    reader = csv.DictReader(file, delimiter=';')
    records = []
    for x in reader:
        records.append(x)
    return records