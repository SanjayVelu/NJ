def power(n):
  
    if n <= 0:
        return False
    else:
        return n & (n - 1) == 0 
n = int(input()) 
if power(n):
    print('yes'.format(n))
else:
    print('no'.format(n))
