

import numpy as np
from math import sqrt, cos, pi


# Début tests Laplace
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

d = np.vstack((a, b, c))

e = np.transpose(d)

potentiel = e
# potentiel = np.array([[[1, 1, 1], [1, 1, 1], [1, 1, 1]],
         # [[1, 1, 1], [1, 1, 1], [1, 1, 1]]])

fact = np.array([])
for i, j in enumerate(potentiel):
    fact = np.array(fact.tolist() + [[[i+1, 2*(i+1), 3*(i+1)]]])
    b = np.multiply(potentiel, fact)

potentiel = np.sum(b,axis = 2)
print(potentiel)

""""
a = np.array([[ 1.,  1.,  1.,  1.,  1.],[ 1.,  1.,  1.,  1.,  1.], [ 1.,  1.,  1.,  1.,  1.]])
print(a.shape)
b = np.pad(a, [(1, 1), (1, 1)], mode='constant')
print(b.shape)
print(b)
"""
# Début tests Biot-Savart  
""" 
arr = [1, 3, 2, 5, 4]
  
# padding array using CONSTANT mode
pad_arr = np.pad(arr, (3, 2), 'constant', constant_values=1)
  
print(pad_arr)

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
r_2 = x[:, 0]
r_1 = 2


diff_theta = pi/3 - x[:, 1]  # pi/3 = angle j
print(diff_theta)
dist_carré = r_1**2 + r_2**2 - 2*r_1*r_2*np.cos(diff_theta)
distance = np.sqrt(dist_carré)
print(distance)
z = distance.copy()
z.fill(0)
print(z)
print(diff_theta.shape, distance.shape, z.shape)
combined = np.vstack((distance, diff_theta, z))
print(combined)
# print(diff_theta)
# print(distance)
# current = np.array([[1, 1, 0], [1, 1, 0], [1, 1, 0]])
# test = np.cross(current, [distance, diff_theta, 0])


r_norm = (np.linalg.norm(distance, axis=0))
print(r_norm)
y = [2, 2, 2]
# y = np.array([y[0]**2, y[1]**2, y[2]**2])
# (x**2)

# print('a')
yy = np.array([y[0]**2, y[1]**2, y[2]**2])
# x[i] == 
dist_carré = y[0]**2 + x[0]**2

#print(dist)
"""




"""
# n = len(x) + 1
y = np.array([[1, 1, 0], [1, 1, 0], [1, 1, 0]])
# x = np.append([x], [[5, 1, 0]])
x[0][0] = 0
print(x)
# x = np.array(x.tolist() + [[0, 0, 0]])

# distance = x- [1, 0, 0]
print('\n')
# print(x)
# (distance)

print(x)
# r_norm = (np.linalg.norm(distance, axis=1)) # yields float
(print('\n'))
# print(np.cross(x, y))
z = np.cross(x, y)
print(z)

print(np.array(z[:, 2]))
z[:, 2] = [0, 0, 0]
print(z)
# print(np.sum(z))

dim_x, dim_y = 4, 4
magnetic_field = np.zeros((dim_x, dim_y, 3))
print(magnetic_field)

(print('\n'))

print(magnetic_field[0])

(print('\n'))
for i in range(4):
    for j in range(4):
        magnetic_field[i][j][2] = 2
print(magnetic_field)
"""