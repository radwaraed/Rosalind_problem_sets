"""Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)"""

#Solution

#This exercise was a pain to solve, mainly because Rosalind has such a strict output format. Alas, here it is!

from Bio import SeqIO

A,C,G,T = [],[],[],[]
consensus=""

for i in range(0,len(record.seq)):
    countA,countC,countG,countT=0,0,0,0
    for record in SeqIO.parse("fasta.txt", "fasta"):
        if record.seq[i]=="A":
            countA=countA+1
        if record.seq[i]=="C":
            countC=countC+1
        if record.seq[i]=="G":
            countG=countG+1
        if record.seq[i]=="T":
            countT=countT+1
        length=len(record.seq)

    A.append(countA)
    C.append(countC)
    G.append(countG)
    T.append(countT)


    if countA >= max(countC,countG,countT):
        consensus=consensus+"A"
    elif countC >= max(countA,countG,countT):
        consensus=consensus+"C"
    elif countG >= max(countA,countC,countT):
        consensus=consensus+"G"
    elif countT >= max(countA,countC,countG):
        consensus=consensus+"T"

if len(consensus)==length:
    print("Everything looks good")
    
print(consensus) 
print("A: "+" ".join([str(i) for i in A]))
print("C: "+" ".join([str(i) for i in C]))
print("G: "+" ".join([str(i) for i in G]))
print("T: "+" ".join([str(i) for i in T]))

