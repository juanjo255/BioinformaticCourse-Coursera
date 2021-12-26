#open txt files
file = open ("file.txt")
out = open ("fileOut.txt", "w")
    
# Function to obtain k-mer composition of a DNA string
def KmerComposition (k, dna):
    dna = dna.strip()
    result = list ()
    for i in range (0, len (dna)-k+1):
        #out.write (dna[i:i+k])
        #out.write ("\n")
        result.append(dna [i:i+k])
    return result
#KmerComposition (int (file.readline()), file.readline())

# Function to obtain a DNA string of its Kmer composition
def DnaFromKmer (entry):
    out.write(entry[0])
    del entry [0]
    for i in entry:
        out.write (i[-1])
#DnaFromKmer (file.read().strip().split("\n"))

# Function to return overlap graph in an adjacency list
def overlapGraph (entry):
    for i in range (0, len(entry)):
        result = list()
        for j in range (0, len(entry)):
            if i == j:
                continue
            elif entry [i][1:] == entry [j][:-1]:
                result.append (entry [j])
                
        if result:
            out.write (entry [i])
            out.write(" -> ")
            out.write(",".join (result))
            out.write("\n")    
#overlapGraph(file.read().strip().split("\n"))

# Function to return debrujin graph as an adjacency list
def debrujin (k, dna):
    kmers = KmerComposition(k,dna)
    nodes = [i[:-1] for i in kmers]
    for i in set (nodes):
        result = list()
        for j in kmers:
            if i == j [:-1]:
                result.append (j[1:])
        out.write (i + " -> ")
        out.writelines (",".join (result))
        out.write ("\n")
#debrujin (int (file.readline()), file.readline())

# Function to return debrujin graph as an adjacency list from Kmers composition
def debrujinFromKmers (entry):
    result = dict()
    for i in entry:
        if not (i [:-1] in result):
            result [ i[:-1] ] = i[1:]
        else:
            result [ i[:-1] ] = result[ i[:-1] ] + "," + i[1:]
            
    for key, val in result.items():
        out.write(key + " -> ")
        out.write (val)
        out.write("\n")
#debrujinFromKmers (file.read().strip().split("\n"))