# 1.3 Average Age
#

while True:
    try:
        total_ages = 0
        quantity = int(input("How many people are in the group? "))
        for x in range(quantity, 0, -1):
            age = int(input(f"How old is person number {x}? "))
            total_ages += age
        print(f"The average age of the group is : {total_ages / quantity}")
    except ValueError as e:
        print("Sorry, please enter a valid number.", e)
        continue
    else:
        break
