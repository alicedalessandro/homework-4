def hamm(strand1,strand2):
    lstrand1=list(strand1)
    lstrand2=list(strand2)
    counter=0
    for i in range(len(lstrand1)):
        if lstrand1[i] !=lstrand2[i]:
            counter+=1
    return counter 
print(hamm('GCTTAATCAGTTAAACTTTTAGATAGGCTTAAAGGGTCCCCTGACCAGCCCTGCTACTGTTCCAGAGGGTCAGCCGTCCTAGTCGATATTTTTGGCATAGAGTAGACAGGATACAGACCAACCCTTTAGTGATACCGGAGATGGTGTCTAAATGGCGTTGCGCCTCGAATCGCAATAACGCAAGCGTCCGGGTTTGAGTCAACATACTTGATAATTATTCATATGTCAGCTTGGTTCATGCTATCAAAGGCTTGATAGCGATTTTTCAATTCTGCACTGCAGGTTGGAAAGTTTATTTCGAAGTTACGTTTCTAATCTCACAACCTACACTAAAATCTACCGCCTAGGTTCTCTGCTGAATCTCTGCGTGCGATTCAATGCCTGATCACCCGAAACCTAACTAGTCCGTTCGCATTACCTGTCTCATTGACGTTAGGTATTGTATACTCCGGGCTTACACGAAGGCCCTCCAATACTTTTGGTTTCGTTAGTAAGCCTACGCGTGTATGGGCACGGTGGAACTCGCTAGAATCCGGCCACATCAACCCTTGTTCCCCGAGCATATGGCCTGCTCTTAAACTATGTCACATAGGTGGCACGACTCATGTTGCCCGAGTTAGCTGCCTTTAGTTAGCACACATTTATGGGATCCCAACGGCGATGACTATAACTCACTTCCTGCTCACAGAGTTGCGATTTTTGCACGGGCTATCCACGACGAGAATTGTACCTAAGGACGCTGCCTGGCTAGCATAAAGCAACATCGAGGGTAGTCCATGATGAGGCGCCATGGAAGCCTGGGGGCACAAATCGCGTTTGAACAACAGTCTTCGTCGGAACAACAATTAGCGCTGCCTCGACATTGGGAACAAGACGATCCTAGAAAGCGGGGCCACCTTCCGAAGTAATCGTCGCATGAAAACGAGGAGCACAAGGGGAGGGG','TCTTAATAAGTTTGGCTAGTAAGTACGCCCAGTGTGTACCCTGAGCCTTGCCCAGCATGTCCCGAAGTGCCAGCAGTCCAGGCTTTCCTTTAAACGATATACGCTACCCTATACAGTACAGTTCATGAAATAGAGCCGCCACAGCATCCAACGGGGTACACTGCCCGCAAGGCTAGACGGCATTCATCCAGGTTAGGTGACCAATTCGTCTAAATTGTCCGTATTTCAGCTCGGGAAAGCCTAGTAGAGAATTGATATTCAATTTTCCCGCCGGTCAGGCCGTGATGATTGACAGTTACGGACGTTCCATTCCATGGTGACTCCCTACTATGAAAACGTTCCTCTAAGGTCTCTGTTTAATCTCTGGGAGGGGCTGATCTCCTGAGCTACCTGAATCTTATGAATGCCTTCGCATAACCGTTTTTGATGACGATGCAACTTGTATACTCCGTACGTAAGGACCGAACAGGCTATATTTTAAGATTCGTAAAATAGACCACGGCTCTATATGCTGCGTCCAAGTCGTTAGCCTCCCCCTGCTGAACCTTGGTCGAATCGAACAGATGGATGGCACTTAAACTATATCACGGACCGCCCATGCCTTACAAGTTAAGTCATAGCGAGCTCGACGTTTAACGGAGTTTTCGAGCGGAGTTACCAACAACCAGTCCTGACTTCATCCTGGCAGACATACAAGATTGACCTGCGCTATGCTCAACCGGAAACGCTGCTTCTCAAATCTCATGCGTAGCATTTATCGAGTGCGAGAGCGTACCATGAGGAGTCGCCCCGTCAGTCGGGGCTCGGAAATCAAGCAATCAACATCGAACTCATGGGCACGCCATGTTGCAACGAATCTACTCGGGGAATAGGACAAGCCTCGATAGTTCCCCTAAGTTCGGCATTCACCAGCGCAGGAAAACGTGGGTACCGAGGCCCGTAG'))