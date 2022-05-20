r = input("What number? ")
r = int(r)

for x in range(1,r):
    if x == 4 or x == 13:
        print(f"{x} is UNLUCKY")
    elif x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")

num = input("How many? ")
num = int(num)
x = 0
while x < num:
    x += 1
    print("nice" * x)

num = input("How many? ")
num = int(num)
for x in range(num):
	print(" :) " * (x+1))