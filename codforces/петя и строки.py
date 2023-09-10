a = input().upper()
b = input().upper()

x = ("aaaa")
y = ("aaaA")
x += y

a += b

if a == x:
    print("0")
elif a <= b:
    print("-1")
elif a >= b:
    print("1")
else:
    print("0")