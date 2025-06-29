import pandas as pd
import numpy as np

ser = pd.Series(dtype="object")

print(ser)

data = np.array(['a', 'e', 'i', 'o', 'u'])

ser = pd.Series(data)
print(ser)