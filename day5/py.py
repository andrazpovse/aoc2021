import numpy as np
from numpy.lib.twodim_base import diag

class VentLine:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return "{x1},{x2} -> {y1},{y2}".format(x1=self.x1, x2=self.x2,
            y1=self.y1, y2=self.y2)


vent_lines = []
max_x = 0
max_y = 0
with open('input.txt') as f:
    for line in f:
        coordinates = [i.split(",") for i in line.strip().split("->")]
        coordinates = [int(coordinate) for sublist in coordinates for coordinate in sublist]
        vent_lines.append(VentLine(
            coordinates[0], coordinates[1],
            coordinates[2], coordinates[3]))

        if max(coordinates[0], coordinates[2]) > max_x:
            max_x = max(coordinates[0], coordinates[2])

        if (max(coordinates[1], coordinates[3])) > max_y:
            max_y = max(coordinates[1], coordinates[3])

diagram = np.zeros((max_x+1, max_y+1))
for vline in vent_lines:
    # print(vline)
    # print(diagram.transpose())

    if (vline.x1 == vline.x2):
        if vline.y1 > vline.y2:
            diagram[vline.x1, vline.y2:(vline.y1+1)] += 1
        else:
            diagram[vline.x1, vline.y1:(vline.y2+1)] += 1

    if (vline.y1 == vline.y2):
        if vline.x1 > vline.x2:
            diagram[vline.x2:(vline.x1+1), vline.y1] += 1
        else:
            diagram[vline.x1:(vline.x2+1), vline.y1] += 1

    # Diagonal
    if (abs(vline.x1 - vline.x2) == abs(vline.y1 - vline.y2)):
        for i in range(abs(vline.x1 - vline.x2) + 1):
            if (vline.y1 < vline.y2):
                if (vline.x1 < vline.x2):
                    diagram[vline.x1 + i, vline.y1 + i] += 1
                else:
                    diagram[vline.x1 - i, vline.y1 + i] += 1
            else:
                if (vline.x1 < vline.x2):
                    diagram[vline.x1 + i, vline.y1 - i] += 1
                else:
                    diagram[vline.x1 - i, vline.y1 - i] += 1

dangerous_points_num = (diagram > 1).sum()
print(dangerous_points_num)
        
print(diagram.transpose())
