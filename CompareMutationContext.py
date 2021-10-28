with open('Cutaneous_somatic_mutation_post_FASTA.bed', 'r') as MutSeqPostFasta:
    with open('mutationData.csv', 'w') as mutData:
        contextCounts = dict()
        for line in MutSeqPostFasta:
            lineColumns = line.strip().split('\t')
            Mut = lineColumns[4]
            Seq = lineColumns[3]
            # Define what types of mutations you're looking for
            if Mut == "AC>TT":
                contextCounts[Seq] = contextCounts.setdefault(Seq, 0) + 1
        for key, value in contextCounts.items():
            mutData.write('%s,%s\n' % (key, value))
print ('done.')
