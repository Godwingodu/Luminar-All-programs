num=12345
sum=0
for i in range(len(str(num))): #for loop,len str is used to find the num length
    temp=num%10 #mode the variable num by 10
    num=num//10 #floor division the num by 10
    sum+=temp #add the variable temp and sum to variable sum
print(sum)
