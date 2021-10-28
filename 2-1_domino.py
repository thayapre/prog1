# 1.5 - Music Scale
#
upper_number = 0

while upper_number <= 6:
    # avoid duplicates
    lower_number = upper_number

    while lower_number <= 6:
        print(f"({upper_number}/{lower_number})")
        lower_number += 1
    upper_number += 1
