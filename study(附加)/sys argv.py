import sys

old_str=sys.argv[1]
new_str=sys.argv[2]
filename=sys.argv[3]

flie_old=open(filename,'r',encoding='utf-8')
file_new=open('newfile.doc','w',encoding='utf-8')

data=flie_old.read()
print(data.count(old_str))
change=data.replace(old_str,new_str)

file_new.write(change)



