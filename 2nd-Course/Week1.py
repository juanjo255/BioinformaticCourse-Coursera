#open txt files
file = open ("file.txt")
out = open ("fileOut.txt", "w")
    
# Function to obtain k-mer composition of a DNA string
def KmerComposition (k, dna):
    dna = dna.strip()
    for i in range (0, len (dna)-k+1):
        out.write (dna[i:i+k])
        out.write ("\n")
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

