f, i = input().split()

f = int(f)
i = int(i)
b = 0

if f >= 150 and i >= 12:
    b = b + 1
if f >= 140 and i >= 14:
    b = b + 1
if f >= 170 or i >= 16:
    b = b + 1
print(b)
