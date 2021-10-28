import time
start_time = time.time()
with open('genomicData.csv', 'w') as gData:
    with open('hg19.fa', 'r') as genome:
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