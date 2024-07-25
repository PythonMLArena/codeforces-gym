exp=input()
 
 
numbers=sorted(exp.split("+"))
 
output=""
 
if len(numbers)==1:
    print(str(numbers[0]))
else:
    for i in range(len(numbers)):
        if i==0:
            output=str(numbers[i])+"+"
        elif i==len(numbers)-1:
            output=output+str(numbers[i])
        else:
            output=output+str(numbers[i])+"+"
    print(output)
