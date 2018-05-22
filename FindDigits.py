file = open('/home/shiyanlou/Code/String.txt')
f = file.read()
i=0
s2=""
for i in range(len(f)):
    s1 = f[i]
    if s1.isdigit():
        s2=s2+s1
print(s2)


