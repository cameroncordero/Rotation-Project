MutSeq = open('Cutaneous_somatic_mutation_MELA_AU_DNVs_sorted_dinuc_filter.bed', 'r')
MutSeqWithContext = open('Cutaneous_somatic_mutation_with_updown_context.bed', 'w')
for i,entry in enumerate(MutSeq):
    lineColumns = entry.strip().split('\t')
    mutStart = int(lineColumns[1]) - 1
    mutEnd = int(lineColumns[2]) + 1
    MutSeqWithContext.write(str(lineColumns[0]))
    MutSeqWithContext.write('\t')
    MutSeqWithContext.write(str(mutStart))
    MutSeqWithContext.write('\t')
    MutSeqWithContext.write(str(mutEnd))
    MutSeqWithContext.write('\t')
    MutSeqWithContext.write(str(lineColumns[3]))
    MutSeqWithContext.write('\t')
    MutSeqWithContext.write(str(lineColumns[4]))
    MutSeqWithContext.write('\t')
    MutSeqWithContext.write(str(lineColumns[5]))
    MutSeqWithContext.write('\n')
print('done.')
