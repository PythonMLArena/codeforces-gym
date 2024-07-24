n=int(input()) # Taking an input argument
final_data=[]
for _ in range(n):
    row = list(map(int, input().split()))
    final_data.append(row)
 
 
final_val =[]
 
for i in range(len(final_data)):
    sum1=0
    for j in range(len(final_data[i])):
        sum1+=final_data[j][i]
 
    final_val.append(sum1)
 
 
if sum(final_val)==0:
    print("YES")
else:
    print("NO")
