sent=input("Enter the sentence:")
w=sent.split()
m=[]
for i in w:
    if i.lower()=="python":
        m.append("pythons")
    else:
        m.append(i)
se=' '.join(m)
print(se)