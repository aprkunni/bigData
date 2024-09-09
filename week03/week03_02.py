import numpy as np
import pandas as pd

# df = pd.DataFrame(
#     {
#     "a": [14, 51, 6],
#     "b": [72, 8, 72],
#     "c": [100, 11, 12]
#     }
# )
# df2 = pd.DataFrame(
#     {
#     "a": [14, 51, 6],
#     "b": [72, 8, 72],
#     "c": [100, 11, 12]
#     }, index=[1, 2, 3]
# )
df = pd.DataFrame(
[
        [14, 72, 100],
        [51, 8, 11],
        [6, 72, 12]
    ],
    index=[1, 2, 3], columns=['a', 'b', 'c']
)

print(df)

