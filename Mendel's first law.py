#Solution

#Given that number of homozygous dominant is k, heterozygous is m and homozygous recessive is n
k=21
m=29
n=29
t = k+m+n

#Two recessives (A) + Two heterzygous (B) + Heterozygous_recessive (C) + recessive_Heterzygous (D)
A = n/t * (n-1)/(t-1)
B = m/t * (m-1)/(t-1) * 0.25
C = m/t * n/(t-1) * 0.5
D = n/t * m/(t-1) * 0.5

#Chance of offspring being recessive
Prob_recessive = A+B+C+D

#Chance of offspring being dominant
Prob_dominant = 1 - Prob_recessive

print(Prob_recessive)
print(Prob_dominant)
