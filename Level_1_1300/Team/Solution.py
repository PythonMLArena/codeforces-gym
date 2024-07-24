n=int(input())
matrix=[]
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
    
final_count=0
for i in matrix:
    count=0
    for j in i:
        if j==1:
            count+=1
            
    if count>=2:
        final_count+=1
        
print(final_count)