1.2) buscamos cuantas veces esta un patron dentro de una secuencia.

text = "CGATATATCCATAG"
pattern = "ATA"
def pattern_count(text, pattern):
    count = 0
    for i in range(0, len(text) - len(pattern) + 1):
        if text[i : len(pattern) + i] == pattern:
            count += 1
    return count
print(pattern_count(text, pattern))

1.2) se buscan las palabras mas repetidas de tamaño k dentro de la secuencia.

text = "GTTGACAGCATTTGAAGTAAGCTAAAGTGTGGACACATTTGAAGTCATTTGAAGTGTTGACAG"
pattern = "GTACAGAGT"
k = 12
def patterncount(text, pattern):
    count = 0
    for i in range(0, len(text) - len(pattern) + 1):
        if text[i : len(pattern) + i] == pattern:
            count += 1
    return count
print(patterncount(text, pattern))


def frequentwords(text, k):
    frequentpatterns = []
    for i in range(0, len(text) - k +1):
        pattern = text[i : k +i]
        count = patterncount(text, pattern)
        if pattern in [i[0] for i in frequentpatterns] :
            continue
        frequentpatterns.append((pattern, count))
    sorted_by_second = sorted(frequentpatterns, key=lambda tup: tup[1], reverse=True)
    clist = []
    for i in sorted_by_second :
        clist.append(i[1])
    maximum = max(clist)
    for i in sorted_by_second :
        if i[1] == maximum:
            print(i)
print(frequentwords(text, k))

1.3) se obtiene la secuencia complementaria de lo que se inserte.

seq = "TTACGCTCGGGTAGA"
seqr = ""
def revcomp(seq, seqr):
    for i in seq:
        if i == "A":
            seqr+="T"
        elif i=="T":
            seqr+="A"
        elif i == "C":
            seqr+="G"
        elif i=="G":
            seqr+="C"
    seqr=seqr[::-1]
    return(seqr)
print(revcomp(seq, seqr)) 

1.3) se imprimen las posiciones en las que se llegue a encontrar el motif ingresado.

def patternposition(text, pattern):
    for i in range(0, len(text) - len(pattern) + 1):
        if text[i : len(pattern) + i] == pattern:
            print(i)
patternposition(text, pattern)

EN BASH: cat Vibrio_cholerae.txt | grep -aob 'CTTGATCAT' | grep -oE '[0-9]+'

1.4) me imprime aquellos motifs de longitud k que se repitan al menos t veces en un espacio de L nucleotidos

text = "TTGCAAATGATGCCTGGGAGGCCGGTTTGTGGGGCTTAACGGAAGAATTCTTTTTAGCGCGGCTCTTAGCGATCCACGATCCACTGTTCCACTGTTCGCGCTTCTAGCCGCGCCCTGACCTTAGGAGTTGCGCCTAACGTAGTTCATAGTCGGAGCTCGGTCGGAGCGAACGAAAATCTTCGCGTAGTATCGCCGATTTGGGGGGTGCACGTAGTACTGATTCGTTTAAACCGTCTAGTTCAGTCATGAAAACCTTCGCTCATCACTTGCTAAACGTTTGCACGATCACCTGCGTGAGCAAAGTTGCTGAGAGAGCGGAATCGCCGCGGTGTTGGCCGCAGATGGACCCTTGTGGGGGACGGATGATTTTAAGTTTGCCCTATCACCTCATACATTAGACAAGAACACACATGTAGCCAACGGACGTAGCACACTTCAACCTGGCTATGTCGACCGCTCCGTAGGTTCATCACGTACAGACGGACCAGTCGGACCAGTATAGTAGAGTTACCCCTTGCCGGGCTTAGGGATGTATACTTTATCTGACTTGTATATGCCGGATAGATACGTCATGCGGCAGAGATAAGACTCCAGTCAACGCGCGGCGAGATCCCTAAGCCCCACCGACGCACGTCGATGGCTATAGCCGATTTTCCAGCCTAAACCTCAGTACCCAGAAGCACGTGGGCGTCTTATCTCACCCAGGGTATAACACGGGCTTCGCGACGGGTCACTAAGTATTTCAGTCAAACAAACGATTGTCCCAGGGGGGGTGATTAACACTACCTTGGAATCTCGTACACGACTTAATCCGCACAAGAGAACTAACATAAAATAGTTGAGGTCATACCGAATACTGAATGTGGATTGAAGCCCTCGACGCTTGGATTATGGTTTTTGCCGCATGTTTTGTTACGTATGCCACTCCTTTGTCTTATTCCGTCTACCGGCCGCTGGGCTTTTGATTTTTTTTTGACCAGAACCAGATTAGCGACACAAACACAGAGGCAGGCAAGAATGCGACTGTAATTATTCTTGGTCTATACGGTCTGTGGGAGGAGACGGGATAGGGCTGGCGCTGTGTGGAGCAATAACGTACAACAGGGCCTATGGCGGATTTCGGATTCGGATTTGCTCTCATTGGCCCTAATGAAACCCTAAAAGATAGCTAGCATGCGCCATAGGCAAACGCGAGTAATCTCTACCATATCCTCGCCTATTCTATATATTTATATGATAAAGGCTGTTTGGGTCTTGTAAGTTGATGCCCTAATAAAAAATGACGAGGATAAACAAGAGTATAGCGTGACGTTGGGTTTGAGACACTTTTTCCCGTACCGTACTTTCCCGTACCGACTCCTCCCCAGTCGCAGACCATCCAACTTGTGGACCTGGGGCATAATCTCGCGCCGGTATAAGACGAGTAATACCCTTCGTGATTTTGCGTCAACCTGAATTTGGAAGCGCTTAGTATCAGACATCCATGTGTGATCATACCAATTTTCCGTGAGCATCTCAGGTCGCGATCCAACTTTGGCCGCTGCCCATACAAGGGCACAAGGGCTGTGTGTCGTAGCTCGCGATCAAATCAAGGCAGAGGATGACGCCTTGTACCGGATTCTCCTTACCGCACCTATCCCCAGATGGACCAGGTTGGGTGGCCAGCAATAAGACGTCTGGGGAGGGTAGAGTCAATTGCGGTAACGTTCAGTGGCTGTTGTGATCAAAAATTTTGGGTTTAAAAATTACCAGAAGCTGGTGTTCGTTGGCCGCTCATGGGCCCACTGTGGACGGGGTAGACAGCACAGTGGCCTCAAATGAGGAATAGTTTATTAACCTGGATCAGTGCGCGTGAACAGACGTGAACAGACGTGAACAGACGTGAACAGACGTGAACAGACGTGAACAGA"
k= 10
L= 30
t= 3
def patterncount(text, pattern):
    count = 0
    for i in range(0, len(text) - len(pattern) + 1):
        if text[i : len(pattern) + i] == pattern:
            count += 1


def frequentwords(text, k, t):
    frequentpatterns = []
    for i in range(0, len(text) - k +1):
        pattern = text[i : k +i]
        count = patterncount(text, pattern)
        if pattern in [i[0] for i in frequentpatterns] :
            continue
        frequentpatterns.append((pattern, count))
    sorted_by_second = sorted(frequentpatterns, key=lambda tup: tup[1], reverse=True)
    seq= ""
    for i in sorted_by_second :
        
        if i[1] >= t:
            
            seq += " " + i[0]
    

def findclumps(text, k, L, t):
    # Patterns ← an array of strings of length 0
    motif=list()
    for i in range(0, len(text)-L):
        Lfragments= text[i : i+L]
        temp= frequentwords(Lfragments, k, t)
        if temp in motif:
            continue
        motif.append(temp)
    print(motif)        
findclumps(text, k, L, t)