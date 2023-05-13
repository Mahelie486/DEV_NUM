import numpy as np
  
  
arr = [1, 3, 2, 5, 4]
  
# padding array using CONSTANT mode
pad_arr = np.pad(arr, (3, 2), 'constant', constant_values=1)
  
print(pad_arr)
