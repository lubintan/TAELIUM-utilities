import urllib2, datetime, csv, os, glob, time, sys

######################################################
# Tests:
# - R calculation is correct
# - reward claculation is correct
# - R is correct for all the blocks in the day
# - interest given out is correct (check change in supplyCurrent)
######################################################

FILE = "data.csv"

def main():
    mainList = []
    headerList = []
    intermediateParser = []

    with open(FILE, 'rb') as f:
        reader = csv.reader(f)

        for each in reader:
            intermediateParser.append(each)

        # print intermediateParser


        for each in intermediateParser[0]:
            headerList.append(each.lstrip().rstrip())





        for x in intermediateParser[1:]:
            newDict = {}


            for y in range(len(x)):
                newDict[headerList[y]] = x[y].lstrip().rstrip()

            mainList.append(newDict)

def createDailyTable(blocks):

    dailyTable = []
    currentDate = None

    for each in blocks:
        if





if __name__ == '__main__':

    this = main()

    for each in this:
        print
        print each
