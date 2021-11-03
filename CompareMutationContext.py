def AttainMutationData(mutationSelection = True, mutation: str, ignorePoorlyDefindRegions = True, ):
    """
    Attains counts of each nucleotide context of the mutation.
    Input the mutation in the correct format (ex. 'AC>TT' ).
    """
    with open('Cutaneous_somatic_mutation_post_FASTA.bed', 'r') as MutSeqPostFasta:
        with open('mutationData.csv', 'w') as mutData:
            contextCounts = dict()
            for line in MutSeqPostFasta:
                lineColumns = line.strip().split('\t')
                Mut = lineColumns[4]
                Seq = lineColumns[3]
                # Only counts specific mutation if mutationSelection == true
                # Otherwise it will count all mutation contexts
                if mutationSelection == True:
                    if Mut == mutation:
                        contextCounts[Seq] = contextCounts.setdefault(Seq, 0) + 1
                else:
                    contextCounts[Seq] = contextCounts.setdefault(Seq, 0) + 1
            #writes dictionary containing mutation contexts into a file
            mutData.write('mutationContext,contextCount' + '\n')
            for key, value in contextCounts.items():
                mutData.write('%s,%s\n' % (key, value))