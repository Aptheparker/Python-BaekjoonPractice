#input
T = int(input())
A = 100
B = 100

for i in range(1, T+1):
  a, b = map(int, input().split())
  
#control
  if a > b:
    B -= a
  elif b > a:
    A -= b
  else:
    continue

#output
print(A)
print(B)