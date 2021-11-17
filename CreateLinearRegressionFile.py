def LinearFile(OutputFile: str, NormalizedData = True, TotalNucs = 4):
    if NormalizedData:
        with open('Normalized_'+OutputFile, 'r') as data:
            with open('Normalized_Linear_Regression_'+OutputFile, 'w') as file:
                file.write('context,frequency,fivePrimeA,fivePrimeT,fivePrimeC,fivePrimeG,threePrimeA,threePrimeT,threePrimeC,threePrimeG'+'\n')
                data.readline()
                for line in data:
                    lineColumns = line.strip().split(',')
                    context = lineColumns[0]                    
                    fivePrimeA = 0
                    fivePrimeT = 0
                    fivePrimeC = 0
                    fivePrimeG = 0
                    threePrimeA = 0
                    threePrimeT = 0
                    threePrimeC = 0
                    threePrimeG = 0
                    if context[0] == 'A':
                        fivePrimeA = 1
                    elif context[0] == 'T':
                        fivePrimeT = 1
                    elif context[0] == 'C':
                        fivePrimeC = 1
                    else:
                        fivePrimeG = 1
                    if context[TotalNucs - 1] == 'A':
                        threePrimeA = 1
                    elif context[TotalNucs - 1] == 'T':
                        threePrimeT = 1
                    elif context[TotalNucs - 1] == 'C':
                        threePrimeC = 1
                    else:
                        threePrimeG = 1
                    str1 = lineColumns[0]
                    str2 = lineColumns[1]
                    file.write(','.join([str1,str2,str(fivePrimeA),str(fivePrimeT),str(fivePrimeC),str(fivePrimeG),str(threePrimeA),str(threePrimeT),str(threePrimeC),str(threePrimeG)])+'\n')