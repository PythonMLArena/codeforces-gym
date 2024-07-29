n=int(input()) 
n+=1
while True:
    n=str(n)
    if str(n[0])!=str(n[1]) and str(n[2])!=str(n[3]) and  str(n[0])!=str(n[2]) and  str(n[0])!=str(n[3]) and  str(n[1])!=str(n[2]) and str(n[1])!=str(n[3]):
        break
    n=int(n)
    n+=1
    
    
print(n)