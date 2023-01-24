rna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
splitted_rna = []

while rna:
    splitted_rna.append(rna[:3])
    rna = rna[3:]

for codon in splitted_rna:
    if codon == 'AUG':
        print('M', end = "")
    elif codon == 'GCC' or codon == 'GCG' or codon == 'GCU' or codon == 'GCA':
        print('A', end = "")
    elif codon == 'CGU' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG' or codon == 'AGA' or codon == 'AGG':
        print('R', end = "")
    elif codon == 'CCC' or codon == 'CCU' or codon == 'CCA' or codon == 'CCG':
        print('P', end = "")
    elif codon == 'ACC' or codon == 'ACU' or codon == 'ACA' or codon == 'ACG':
        print('T', end = "")
    elif codon == 'GAA' or codon == 'GAG':
        print('Z', end = "")
    elif codon == 'GAU' or codon == 'GAC':
        print('D', end = "")
    elif codon == 'AUU' or codon == 'AUC' or codon == 'AUA':
        print('I', end = "")
    elif codon == 'UUC' or codon == 'UUU':
        print('F', end = "")
    elif codon == 'UUA' or codon == 'UUG':
        print('L', end = "")
    elif codon == 'UCU' or codon == 'UCC' or codon == 'UCA' or codon == 'UCG':
        print('S', end = "")
    elif codon == 'UAU' or codon == 'UAC':
        print('Y', end = "")
    elif codon == 'UAA' or codon == 'UAG':
        print('', end = "")
    elif codon == 'UGU' or codon == 'UGC':
        print('C', end = "")
    elif codon == 'UGA':
        print('W', end = "")
    elif codon == 'AAU' or codon == 'AAC':
        print('B', end = "")
    elif codon == 'GUU' or codon == 'GUC' or codon == 'GUA' or codon == 'GUG':
        print('V', end = "")
    elif codon == 'GAA' or codon == 'GAG':
        print('E', end = "")
    elif codon == 'CAA' or codon == 'CAG':
        print('Q', end = "")
    elif codon == 'GGU' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG':
        print('G', end = "")
    elif codon == 'CAU' or codon == 'CAC':
        print('H', end = "")
    elif codon == 'AAG' or codon == 'AAA':
        print('K', end = "")
    
        
print('\n')
