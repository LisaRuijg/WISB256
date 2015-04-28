fout=open('output.txt', 'w')
print(fout)
line1='Hallo iedereen, \n'
fout.write(line1)
line2='Alles goed?? \n'
fout.write(line2)
fout.close()
t=[]

import time
T1 = time.perf_counter()

fin=open('output.txt')
for line in fin:
    t=t+[line[0]]
    print(t)
fin.close()

T2 = time.perf_counter()
print('Time required', T2-T1  ,'sec.')
    