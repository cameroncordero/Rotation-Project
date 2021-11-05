import os
import statistics
def NormalizeData(OutputFile, FastaFile, TotalNucleotidesPerContext: int, NormalizeToMedian = True):
    """
    Normalizes data to the genome and median default is true.
    """
    if not os.path.exists('Genomic_Counts_'+FastaFile):
        with open('Genomic_Counts_'+FastaFile, 'w') as gData:
            with open(FastaFile, 'r') as genome:
                seqCounts = dict()
                for line in genome:
                    if '>' in line:
                        print ('\x1B[3mProcessing...\x1B[0m ' + 
                            line[1:4] + 'omosome ' + line[4:])
                        fullLine = ''
                        leftovers = ''
                        continue
                    else:
                        i = 0
                        fullLine = leftovers + line.strip()
                        nucContext = fullLine[i:i+TotalNucleotidesPerContext]
                        while len(nucContext) > (TotalNucleotidesPerContext-1):
                            seqCounts[nucContext] = seqCounts.setdefault(nucContext, 0) + 1
                            i += 1
                            nucContext = fullLine[i:i+4]
                        leftovers = fullLine[i:]
                gData.write('sequenceContext,contextFrequency')
                for key, value in seqCounts.items():
                    gData.write('%s,%s\n' % (key, value))
    with open(OutputFile, 'r') as mutData:
        with open('Genomic_Counts_'+TotalNucleotidesPerContext+'_mer'+FastaFile, 'r') as gData:
            with open('Normalized_'+OutputFile, 'w') as normData:
                mutDataDict = {}
                gDataDict = {}
                normDataDict = {}
                finalDataDict = {}
                # re-writing dictionaries from files
                mutData = mutData.readlines()[1:]
                for line1 in mutData:
                    sepLine = line1.strip().split(',')
                    mutDataDict[sepLine[0]] = sepLine[1]
                gData = gData.readlines()[1:]
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
                if NormalizeToMedian == True:
                    for mut2, mfreq2 in normDataDict.items():
                        finalDataDict[mut2] = mfreq2/dataMedian
                normData.write('sequenceContext,normalizedCounts'+'\n')
                for key, value in finalDataDict.items():
                    normData.write('%s,%s\n' % (key, value))