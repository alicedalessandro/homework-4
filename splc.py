rnacodon =  { 'ATA':'I',
    'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T',
    'ACT':'T', 'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S',
    'AGT':'S', 'AGA':'R', 'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L',
    'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CAC':'H',
    'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R',
    'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'GCA':'A',
    'GCC':'A', 'GCG':'A', 'GCT':'A', 'GAC':'D', 'GAT':'D', 'GAA':'E',
    'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S',
    'TCC':'S', 'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L',
    'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'', 'TAG':'', 'TGC':'C',
    'TGT':'C', 'TGA':'', 'TGG':'W', }

def prot(rna):
    aminoseq = ""
    for i in range(0,len(rna)-(3+len(rna)%3), 3):
        aminoseq += rnacodon[rna[i:i+3]]
        if rnacodon[rna[i:i+3]] == "STOP" :
            break
    return aminoseq

def delete(strand,introns):
    while introns:
        return delete(strand.replace(introns.pop(),''),introns)
    return strand
    
def splc(strand,introns):
    codingstrand=delete(strand,introns)
    return prot(codingstrand)
    
with open('rosalind_splc.txt') as f:
    A=f.read().split('>Rosalind_')
    l=[]
    for b in A:
        b=b.strip()
        b=b.replace('\n', '')
        b=''.join([i for i in b if not i.isdigit()])
        l.append(b)     
    strand=str(l[1])
    introns=l[2:]


    
with open('rosalind_splc_out.txt', 'w') as f:
    f.write(splc(strand,introns))

    
