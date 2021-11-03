import re
def CreateNewBedFile(fivePrimeCont: int, threePrimeCont: int):
    """
    This is my function description!
    """
    with open(MutationFile, 'r') as MutSeq:
        with open(FastaFile, 'r') as FastaReturn:
            with open(OutputFile, 'w') as MutSeqPostFasta:
                for line in MutSeq:
                    lineColumns = line.strip().split('\t')
                    pos1 = int(lineColumns[1]) - fivePrimeCont
                    pos2 = int(lineColumns[2]) + threePrimeCont
                    mutText = FastaReturn.readline()
                    #if str(pos1) in mutText and str(pos2) in mutText and lineColumns[5] in mutText:
                    check = re.split(':|-|\(', mutText, maxsplit = 3)
                    plusMinus = check[3]
                    assert (check[0][1:] == lineColumns[0] and check[1] == str(pos1) and 
                        check[2] == str(pos2) and plusMinus[0] == lineColumns[5]), line + check
                    MutSeqPostFasta.write('\t'.join( lineColumns[:3] + 
                        [FastaReturn.readline().strip()] + lineColumns[4:] ) + '\n' )
    print ('done.')