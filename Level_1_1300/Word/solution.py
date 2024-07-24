name=input()
countofUpper=0
countofLower=0
lowerStr=""
UpperStr=""
for i in name:
    if i==i.upper():
        countofUpper+=1
        lowerStr+=i.lower()
        UpperStr+=i.upper()
    else:
        countofLower+=1
        lowerStr+=i.lower()
        UpperStr+=i.upper()
        
if countofUpper<=countofLower:
    print(lowerStr)
else:
    print(UpperStr)