# 2.2 Draw a board
#
rows = 15
cols = 15
line = []

for y in range(0, rows, +1):
    for x in range(0, cols, +1):
        if x > (y + 1) or y > (x + 1):
            line.append("X")
        else:
            line.append(".")
    print(*line)
    line.clear()
