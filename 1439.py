'''
data = input()
groupA =0
groupB =0
num_list = list(map(int,data))
num = num_list[0]
for i in range(1,len(num_list)):
  print("i1",i)
  if num_list[i-1] ==0:  
    groupA +=1
    print("groupA",groupA)
    if num == num_list[i]:
      num = num_list[i+1]
    else:
      groupB+=1
      print("i2",i)
  else:
    groupB +=1
    print("groupB",groupB)
print(groupA if groupA <= groupB else groupB)


나의..돌고도는 바보같은 코드..

'''
s = input()
cnt = 0
for i in range(len(s)-1):
  if s[i] != s[i+1]:
    cnt +=1

print((cnt+1)//2)