# Pandas: Select distinct across multiple DataFrame columns

import pandas as pd

df = pd.DataFrame({
    'Animal': ['Cat', 'Cat', 'Cat', 'Dog', 'Dog', 'Dog'],
    'Max Speed': [25, 25, 40, 45, 45, 65]
})

#   Animal  Max Speed
# 0    Cat         25
# 2    Cat         40
# 3    Dog         45
# 5    Dog         65
print(df.drop_duplicates())
