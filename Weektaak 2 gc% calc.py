#opens file
o = open('test.txt', 'r')

#reads file from left to right
seq = o.read()

total = (len(seq))

#counts how many times each letter is in the sequence
G = seq.count('G')
T = seq.count('T')
C = seq.count('C')
A = seq.count('A')

total_GC = G+C
total_AT = A+T

#calculates the percentage for both GC and AT
total_GC_percentage = ((G+C)/total)*100
total_AT_percentage = ((A+T)/total)*100

#presents the data
print('The total amount of nucleotides is',total_AT+total_GC)
print('This sequence has a GC% of', total_GC_percentage,'%')
print('This sequence has a AT% of', total_AT_percentage,'%')
