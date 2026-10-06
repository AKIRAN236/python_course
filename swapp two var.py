m=int(input())
n=int(input())
print("Before swapping: n =", n, "m =", m)
# Swapping the values of n and m
temp=m
m=n
n=temp
print(f"m:{m},n:{n}")
#another technic
a=int(input())
b=int(input())
a=a+b
b=a-b
a=a-b
print(f"a:{a},b:{b}")
a=int(input())
b=int(input())
a=a^b
b=a^b
a=a^b
print(f"a:{a},b:{b}")
#another technic
a=int(input())
b=int(input())
a,b=b,a
print(f"a:{a},b:{b}")