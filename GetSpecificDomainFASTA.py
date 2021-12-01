import subprocess
import os
FastaFile = 'hg19.fa'
MutationFile = 'Chromo_Domain_Cutaneous_somatic_mutation_MELA_AU_DNVs_sorted_dinuc_filter.bed'
Domain = 'heterochromatin'
with open(MutationFile):
subprocess.check_call(args=['bedtools', 'getfasta', '-fi', FastaFile, '-bed',
        'Mutation_File_With_Context_Values.bed', '-fo','Expanded_Context.fa', '-s'])