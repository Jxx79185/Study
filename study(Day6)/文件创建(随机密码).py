import random
import string

f=open('wenjian.txt','w')
names=['A','B','C','D','E']

for x in names:
    pwd=random.sample(string.ascii_letters+string.digits,10)
    line=f"{x}:{''.join(pwd)}\n"
    print(line.center(100,'-'))   
    f.write(line) 
    f.close

f= open('xxx.txt', "r+")
line=f.readline()

print(line)
    
 

