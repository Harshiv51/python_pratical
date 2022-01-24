arr=[]
n=int(input())
for i in range(1,n+1):
    arr_element=int(input())
    arr.append(arr_element)

print(sorted(arr)[-2])