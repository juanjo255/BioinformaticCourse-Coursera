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