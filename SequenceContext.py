def CreateNewBedFile(MutationFile: str, FastaFile: str, OutputFile: str, fivePrimeCont: int, threePrimeCont: int):
    """
    Takes a .bed file and returns another bed file that has increased nucleotide context. (numerical values remain the same)
    The context can be increased by fivePrimeCount and threePrimeCount.
    Input the file names once they're in the same directory.
    """    
    with open(MutationFile, 'r') as MutSeq:
        with open('MutationFileWithContext.bed', 'w') as MutSeqWithContext:
                for line in MutSeq:
                    lineColumns = line.strip().split('\t')
                    # decrease and increase the positional numbers so when
                    # compared to the fasta file, it will return the nucleotides
                    # that are in the newly defined range
                    mutStart = int(lineColumns[1]) - fivePrimeCont
                    mutEnd = int(lineColumns[2]) + threePrimeCont
                    # write those new position numbers to 
                    MutSeqWithContext.write('\t'.join(lineColumns[0] +
                        str(mutStart) + str(mutEnd) + lineColumns[3:] )
                        + '\n')
    # terminal portion to compare with fasta file
    #with open('MutationFileWithContext.bed', 'r') as MutSeqWithContext:
    # output file from terminal fasta comparison
    with open(MutationFile, 'r') as MutSeq:
        with open(OutputFile, 'w') as MutSeqPostFasta:
            with open(FastaFile, 'r') as FastaReturn:
                for line in MutSeq:
                    lineColumns = line.strip().split('\t')
                    mutStart = int(lineColumns[1]) - fivePrimeCont
                    mutEnd = int(lineColumns[2]) + threePrimeCont
                    mutText = FastaReturn.readline()
                    check = re.split(':|-|\(', mutText, maxsplit = 3)
                    plusMinus = check[3]
                    # checks to make sure all lines are present and have accurate counts
                    assert (check[0][1:] == lineColumns[0] and check[1] == str(pos1) and 
                        check[2] == str(pos2) and plusMinus[0] == lineColumns[5]), line + check
                    MutSeqPostFasta.write('\t'.join( lineColumns[:3] + 
                        [FastaReturn.readline().strip()] + lineColumns[4:] ) + '\n' )