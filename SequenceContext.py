with open('Cutaneous_somatic_mutation_MELA_AU_DNVs_sorted_dinuc_filter.bed', 'r') as MutSeq:
    with open('Cutaneous_somatic_mutation_with_updown_context.bed', 'w') as MutSeqWithContext:
        for line in MutSeq:
            lineColumns = line.strip().split('\t')
            mutStart = int(lineColumns[1]) - 1
            mutEnd = int(lineColumns[2]) + 1
            MutSeqWithContext.write('\t'.join( [lineColumns[0], str(mutStart), 
                str(mutEnd)] + lineColumns[3:] ) + '\n')
print('done.')

