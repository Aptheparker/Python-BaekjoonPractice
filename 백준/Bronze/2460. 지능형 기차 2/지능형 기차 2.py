ans=0
now=0


for i in range(10):
  a,b=map(int,input().split())
  now=now-a+b
  if now > ans:
    ans=now

print(ans)