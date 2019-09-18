o = open('test.txt', 'r')

seq = o.read()

total = (len(seq))

G = seq.count('G')
T = seq.count('T')
C = seq.count('C')
A = seq.count('A')

total_GC = G+C
total_AT = A+T

total_GC_percentage = ((G+C)/total)*100
total_AT_percentage = ((A+T)/total)*100

print('The total amount of nucleotides is',total_AT+total_GC)
print('This sequence has a GC% of', total_GC_percentage,'%')
print('This sequence has a AT% of', total_AT_percentage,'%')