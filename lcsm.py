def lcsm(strands):
    strand1=strands[1]
    x=''
    r=''
    for i in range (len(strand1)):
        for j in range (i+1, len(strand1)+1):
            x=strand1[i:j]
            for h in range(1, len(strands)):
                if x not in strands[h]:
                    break
                if h + 1 == len(strands) and len(r) < len(x):
                    r=x
    return re       

with open('rosalind_lcsm.txt') as f:
    A=f.read().split('>Rosalind_')
    l=[]
    for j in A:
        j=j.strip()
        j=j.replace('\n', '')
        l.append(j)  
        
with open('lcsm_out.txt', 'w') as f:
    f.write(lcsm(l))
