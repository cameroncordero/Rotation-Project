import subprocess
FastaFile = 'hg19.fa'
MutationFile = 'Chromo_Domain_Cutaneous_somatic_mutation_MELA_AU_DNVs_sorted_dinuc_filter.bed'
DomainFile = 'wgEncodeBroadHmmNhlfHMM.bed'
Domain = 'euchromatin'
with open(DomainFile, 'r') as domFile:
    with open(Domain+'_'+MutationFile, 'w') as outFile:
        heteroDomain = ['12', '13', '14', '15']
        euDomain = ['1_', '2_', '4_', '5_', '6_', '7_', '9_', '10', '11']
        undefinedDomain = [ '3_', '8_']
        for line in domFile:
            lineColumns = line.strip().split('\t')
            dom = lineColumns[3]
            if dom[:2] in euDomain:
                outFile.write(line)
            else:
                continue
subprocess.check_call(args=['bedtools', 'getfasta', '-fi', FastaFile, '-bed',
        Domain+'_'+MutationFile, '-fo',Domain+'_'+FastaFile, '-s'])