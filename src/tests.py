

import numpy as np


  
""" 
arr = [1, 3, 2, 5, 4]
  
# padding array using CONSTANT mode
pad_arr = np.pad(arr, (3, 2), 'constant', constant_values=1)
  
print(pad_arr)
"""
electric_current = [[["I_1x", "I_1y"], ["I_2x", "I_2y"]], [["I_3x", "I_3y"], ["I_4x", "I_4y"]]]
print(len(electric_current))
position = []
for i in range(2):
    for j in range(2):
        current_x, current_y= electric_current[i][j][0], electric_current[i][j][1]
        print(f"({i}, {j}): {current_x}, {current_y}")
        position.append([i, j, 0])
print(position)
print('\n')
x = np.array([[3, 1, 0], [4, 1, 0], [5, 1, 0]])
# n = len(x) + 1
y = np.array([[1, 1, 0], [1, 1, 0], [1, 1, 0]])
# x = np.append([x], [[5, 1, 0]])
print(x)
x = np.array(x.tolist() + [[0, 0, 0]])

# distance = x- [1, 0, 0]
print('\n')
print(x)
# (distance)

"""
print(x)
# r_norm = (np.linalg.norm(distance, axis=1)) # yields float
(print('\n'))
# print(np.cross(x, y))
z = np.cross(x, y)
print(z)
(print('\n'))
print(np.array(z[:, 2]))
z[:, 2] = [0, 0, 0]
print(z)
# print(np.sum(z))
"""