a,b = list(map(int,input().split()))
c = a+b
mod = c% 2
if mod > 0:
  print("odd")
else:
  print("even")
