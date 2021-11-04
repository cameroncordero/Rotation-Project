import subprocess
import re
import os
def CreateNewBedFile(fivePrimeCount: int, threePrimeCount: int, MutationFile, FastaFile):
    """
    Takes a .bed file and returns another .bed file that has increased nucleotide context. (numerical values remain the same)
    The context can be increased by fivePrimeCount and threePrimeCount.
    Input the file names once they're in the same directory.
    """  
    with open(MutationFile, 'r') as MutSeq:
        with open('Mutation_File_With_Context_Values.bed', 'w') as MutSeqWithContext:
                for line in MutSeq:
                    lineColumns = line.strip().split('\t')
                    # decrease and increase the positional numbers so when
                    # compared to the fasta file, it will return the nucleotides
                    # that are in the newly defined range
                    mutStart = int(lineColumns[1]) - fivePrimeCount
                    mutEnd = int(lineColumns[2]) + threePrimeCount
                    # write those new position numbers to 
                    MutSeqWithContext.write('\t'.join([lineColumns[0], 
                        str(mutStart), str(mutEnd)] + lineColumns[3:])
                        + '\n')
    # terminal portion to compare with fasta file and return the nuceotides missing
    subprocess.check_call(args=['bedtools', 'getfasta', '-fi', FastaFile, '-bed',
        'Mutation_File_With_Context_Values.bed', '-fo','Expanded_Context.fa', '-s'])
    # with open('MutationFileWithContext.bed', 'r') as MutSeqWithContext:
    # output file from terminal fasta comparison
    with open(MutationFile, 'r') as MutSeq:
        with open('Mutation_File_With_Nucleotides.bed', 'w') as MutSeqPostFasta:
            with open('Expanded_Context.fa', 'r') as FastaReturn:
                for line in MutSeq:
                    lineColumns = line.strip().split('\t')
                    mutStart = int(lineColumns[1]) - fivePrimeCount
                    mutEnd = int(lineColumns[2]) + threePrimeCount
                    mutText = FastaReturn.readline()
                    check = re.split(':|-|\(', mutText, maxsplit = 3)
                    plusMinus = check[3]
                    # checks to make sure all lines are present and have accurate counts
                    assert (check[0][1:] == lineColumns[0] and check[1] == str(mutStart) and 
                        check[2] == str(mutEnd) and plusMinus[0] == lineColumns[5]), line + check
                    MutSeqPostFasta.write('\t'.join( lineColumns[:3] + 
                        [FastaReturn.readline().strip()] + lineColumns[4:] ) + '\n' )
                os.remove('Mutation_File_With_Context_Values.bed')
                os.remove('Expanded_Context.fa')