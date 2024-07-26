number=input()
 
luckycount=0
 
for i in number:
    if int(i)==4 or int(i)==7:
        luckycount+=1
 
        
if luckycount==4 or luckycount==7:
    print("YES")
else:
    print("NO")
