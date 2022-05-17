number = 1

print("WHILE LOOP")
while number < 6:
    print(number)
    number += 1

num = 1

print("FOR LOOP")
for num in range(0, 10):
    if num == 5:
        continue
    print(num)