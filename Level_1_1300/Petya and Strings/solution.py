str1=input("")
str2=input("")
checksame=True
i=0
j=0
while i < len(str1) and j < len(str2):
    if str1[i].lower()!=str2[i].lower():
        checksame=False
        break
    i+=1
    j+=1
        
        
if checksame:
    print(0)
else:
    str1=str1.lower()
    str2=str2.lower()
    i=0
    j=0
 
    while i < len(str1) and j < len(str2):
        if ord(str1[i]) > ord(str2[j]):
            print(1)
            break
        elif ord(str1[i]) < ord(str2[j]):
            print(-1)
            break
        i+=1
        j+=1