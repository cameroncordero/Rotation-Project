import time
import os
import statistics
def NormalizeData(MutationFile, FastaFile):
    start_time = time.time()
    with open('genomicData.csv', 'w') as gData:
        with open(FastaFile, 'r') as genome:
            seqCounts = dict()
            for line in genome:
                if '>' in line:
                    print ('\x1B[3mProcessing...\x1B[0m ' + 
                        line[1:4] + 'omosome ' + line[4:] +
                        '%s seconds since start' % (time.time() - start_time))
                    fullLine = ''
                    leftovers = ''
                    continue
                else:
                    i = 0
                    fullLine = leftovers + line.strip()
                    fourNuc = fullLine[i:i+4]
                    while len(fourNuc) > 3:
                        seqCounts[fourNuc] = seqCounts.setdefault(fourNuc, 0) + 1
                        i += 1
                        fourNuc = fullLine[i:i+4]
                    leftovers = fullLine[i:]
            for key, value in seqCounts.items():
                gData.write('%s,%s\n' % (key, value))
    print('%s seconds to process' % (time.time() - start_time))
    with open(MutationFile, 'r') as mutData:
        with open(FastaFile, 'r') as gData:
            if os.path.exists('GenomicCounts'+FastaFile):
                with open('Genomic_Counts'+FastaFile, 'w') as normData:
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
                    # dividing the frequency of mutation x-mer sequences
                        # by the frequency of genomic x-mer sequences 
                    for mut1, mfreq1 in mutDataDict.items():
                        gfreq = gDataDict.get(mut1)
                        normDataDict[mut1] = int(mfreq1)/int(gfreq)
                    # dividing the data by the median to have a value of 1
                    dataMedian = statistics.median(normDataDict.values())
                    for mut2, mfreq2 in normDataDict.items():
                        finalDataDict[mut2] = mfreq2/dataMedian
                    for key, value in finalDataDict.items():
                        normData.write
                        normData.write('%s,%s\n' % (key, value))