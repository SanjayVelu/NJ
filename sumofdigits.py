num = int(input())
sum = 0
while num > 0:
    d = num%10
    num = num//10
    sum += d
print(sum)
