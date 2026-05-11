import string

source=string.printable#生成代码
output=string.printable[::-1]#反转


password_table=str.maketrans(source,output)

password='Who are you?'

encrypted=password.translate(password_table)
encrypted2=encrypted.translate(password_table)
print(encrypted)
print(encrypted2)

password_f=str.maketrans(output,source)

x=encrypted2.translate(password_f)

y=x.translate(password_f)

print(x)
print(y)
p=len (password)
print(p)