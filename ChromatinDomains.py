MutationFile = 'Cutaneous_somatic_mutation_MELA_AU_DNVs_sorted_dinuc_filter.bed'
with open(MutationFile, 'r') as mutFile:
    with open('wgEncodeBroadHmmNhlfHMM.bed', 'r') as chromDom:
        with open('Chromo_Domain_'+MutationFile, 'w') as newFile:
            heteroDomain = ['12', '13', '14', '15']
            euDomain = ['1_', '2_', '4_', '5_', '6_', '7_', '9_', '10', '11']
            undefinedDomain = [ '3_', '8_']
            mutLocWrite = mutFile.readline().strip()
            mutLoc = mutLocWrite.split('\t')
            for line in chromDom:
                lineColumns = line.strip().split('\t')
                while lineColumns[0] == mutLoc[0] and (int(mutLoc[1])+int(mutLoc[2]))/2 < int(lineColumns[2]):
                    # if on same chromosome, and within range
                    if lineColumns[0] == mutLoc[0] and int(lineColumns[1]) <= int(mutLoc[1]) and int(lineColumns[2]) >= int(mutLoc[2]):
                        chromType = lineColumns[3]
                        if chromType[:2] in heteroDomain:
                            newFile.write(mutLocWrite+'\t'+'heterochromatin'+'\n')
                        elif chromType[:2] in euDomain:
                            newFile.write(mutLocWrite+'\t'+'euchromatin'+'\n')
                        elif chromType[:2] in undefinedDomain:
                            newFile.write(mutLocWrite+'\t'+'other'+'\n')
                        else:
                            print('found unidentified region')
                            break
                        mutLocWrite = mutFile.readline().strip()
                        mutLoc = mutLocWrite.split('\t')
                    # if on same chromosome but mut file needs to catch up to chromosome file
                    elif lineColumns[0] == mutLoc[0] and int(lineColumns[1]) >= int(mutLoc[1]) and int(lineColumns[2]) >= int(mutLoc[2]):
                        mutLocWrite = mutFile.readline().strip()
                        mutLoc = mutLocWrite.split('\t')
                    # if on same chromosome but mut file ahead of chromosome file
                    elif lineColumns[0] == mutLoc[0] and int(lineColumns[1]) <= int(mutLoc[1]) and int(lineColumns[2]) <= int(mutLoc[2]):
                        break
                    # if chromosome file is ahead of mutation file
                    elif lineColumns[0] > mutLoc[0]:
                        mutLocWrite = mutFile.readline().strip()
                        mutLoc = mutLocWrite.split('\t')
                    # if mutation file is ahead of chromosome file
                    elif lineColumns[0] > mutLoc[0]:
                        break
                    else:
                        print('chromosome data is not matching up')
                        break