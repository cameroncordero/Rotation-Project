import os
def AttainMutationData(mutation: str, OutputFile, mutationSelection = True,
    MutationCounts = 'Mutation_Context_Counts.csv'):
    """
    Attains counts of each nucleotide context of the mutation.
    Input the mutation in the correct format in the file (ex. 'AC>TT' ).
    """
    with open('Mutation_File_With_Nucleotides.bed', 'r') as MutSeqPostFasta:
        with open(OutputFile, 'w') as mutData:
            contextCounts = dict()
            for line in MutSeqPostFasta:
                lineColumns = line.strip().split('\t')
                Mut = lineColumns[4]
                Seq = lineColumns[3]
                # Only counts specific mutation if mutationSelection == True
                # Otherwise it will count all mutation types
                if mutationSelection == True:
                    if Mut == mutation:
                        contextCounts[Seq] = contextCounts.setdefault(Seq, 0) + 1
                else:
                    break
            #writes dictionary containing mutation context counts into a file
            mutData.write('mutationContext,contextCount' + '\n')
            for key, value in contextCounts.items():
                mutData.write('%s,%s\n' % (key, value))
            os.remove('Mutation_File_With_Nucleotides.bed')