with open("input.txt","r") as f:
    sir=f.readline()
q=0 
r=0 
n=0   
m=0   
for i in sir:
    if ord(i) in range(65,91):
        q+=1
with open("litereA.txt","w") as f:
    f.write(str(q))
for i in sir:
    if ord(i) in range(97,123):
        r+=1
with open("litereB.txt","w") as f:
    f.write(str(r))
for i in sir:
    if ord(i) in range(49,58):
        n+=1
with open("cifre.txt","w") as f:
    f.write(str(n))
for i in sir:
    if ord(i) in range(33,42):
        m+=1
with open("caractere.txt","w") as f:
    f.write(str(m))