MutationFile = 'Cutaneous_somatic_mutation_MELA_AU_DNVs_sorted_dinuc_filter.bed'
with open('Chromo_Domain_'+MutationFile, 'r') as chromFile:
    countDic = {}
    mutation = 'AC>TT'
    for line in chromFile:
        lineColumns = line.strip().split('\t')
        domain = lineColumns[6]
        seq = lineColumns[4]
        if mutation == seq:
            countDic[domain] = countDic.setdefault(domain, 0) + 1
        else:
            continue
    print(countDic)