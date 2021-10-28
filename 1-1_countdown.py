# 1.1 Countdown
#
while True:
    try:
        x = int(input("Please enter a valid number? "))
    except ValueError:
        print("Sorry, please enter a valid number.")
        continue
    else:
        break
x1 = x
x2 = x

print("While loop example:")
while x1 >= 0:
    print(x1)
    x1 -= 1

print("\nFor loop example:")
for i in range(x2, -1, -1):
    print(i)
