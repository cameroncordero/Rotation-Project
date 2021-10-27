import re
with open('Cutaneous_somatic_mutation_MELA_AU_DNVs_sorted_dinuc_filter.bed', 'r') as MutSeq:
    with open('New_Cutaneous_somatic_mutation.fa', 'r') as FastaReturn:
        with open('Cutaneous_somatic_mutation_post_FASTA.bed', 'w') as MutSeqPostFasta:
            for line in MutSeq:
                lineColumns = line.strip().split('\t')
                pos1 = int(lineColumns[1]) - 1
                pos2 = int(lineColumns[2]) + 1
                mutText = FastaReturn.readline()
                #if str(pos1) in mutText and str(pos2) in mutText and lineColumns[5] in mutText:
                check = re.split(':|-|\(', mutText, maxsplit = 3)
                plusMinus = check[3]
                assert (check[0][1:] == lineColumns[0] and check[1] == str(pos1) and 
                    check[2] == str(pos2) and plusMinus[0] == lineColumns[5]), line + check
                MutSeqPostFasta.write('\t'.join( lineColumns[:3] + 
                    [FastaReturn.readline().strip()] + lineColumns[4:] ) + '\n' )
print ('done.')