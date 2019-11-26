def revc(strand):
    revstrand=strand[::-1]
    revcomp=""
    
    for i in range(len(revstrand)):
        if revstrand[i]=='A':
            revcomp+='T'
        if revstrand[i]=='T':
            revcomp+='A'
        if revstrand[i]=='C':
            revcomp+='G'
        if revstrand[i]=='G':
            revcomp+='C'
            
    return revcomp