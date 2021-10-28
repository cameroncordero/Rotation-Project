import statistics
from decimal import *
with open('mutationData.csv', 'r') as mutData:
    with open('genomicData.csv', 'r') as gData:
        with open('normalizedMutData.csv', 'w') as normData:
            mutDataDict = {}
            gDataDict = {}
            normDataDict = {}
            finalDataDict = {}
            # re-writing dictionaries from files
            for line1 in mutData:
                sepLine = line1.strip().split(',')
                mutDataDict[sepLine[0]] = sepLine[1]
            for line2 in gData:
                sepLine = line2.strip().split(',')
                gDataDict[sepLine[0]] = sepLine[1]
            # dividing the frequency of mutation 4-mer sequences
                # by the frequency of genomic 4-mer sequences 
            for mut1, mfreq1 in mutDataDict.items():
                gfreq = gDataDict.get(mut1)
                normDataDict[mut1] = int(mfreq1)/int(gfreq)
            # dividing the data by the median to have a value of 1
            dataMedian = statistics.median(normDataDict.values())
            print(Decimal(dataMedian))
            for mut2, mfreq2 in normDataDict.items():
                print(mut2)
                print(mfreq2)
                finalDataDict[mut2] = Decimal(int(mfreq2))/Decimal(dataMedian)
            print(finalDataDict)