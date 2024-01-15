#deleting 2 characters and reversing the resultant string#

n=input("enter a string:")
char_list=list(n)
m=int(input("enter the number ofcharacters to be deleted:"))
for _ in range(m):
    p=input("enter the characters to be deleted:")
    a=char_list.index(p)
    del char_list[a]
reve_list=char_list[::-1]
res=''.join(reve_list)
print(res)
















