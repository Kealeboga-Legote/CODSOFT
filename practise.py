n = int(input())
arr = list(map(int, input().split()))
    
max_value =arr[0]
sec = float('-inf')

for i in arr:
    if i>max_value:
            sec = max_value
            max_value = i
    elif (i>sec):
        sec = i
        
            
print(sec)